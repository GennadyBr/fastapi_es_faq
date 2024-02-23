"""
api/v1/get_all_router.py

Get all records from Elasticsearch cluster by pagination parameters

"""
from logging import getLogger

from fastapi import APIRouter
from fastapi import Query

from config.settings import settings
from db.es import es_conn
from db.es import search_result

get_all_router = APIRouter()

LOGGER = getLogger(__name__)
es = es_conn()
index_name = settings["index_name"]


@get_all_router.get("/", response_model=list)
async def get_all(
    pagination_size: int = Query(None, description="кол-во ответов на странице"),
    pagination_from: int = Query(None, description="номер начального ответа"),
) -> list:
    """
    Get all records from Elasticsearch cluster by pagination parameters

    :param pagination_size: int

    :param pagination_from: int

    :return: list of dicts
    """
    body = {
        "size": pagination_size,
        "from": pagination_from,
    }
    return await search_result(body)
