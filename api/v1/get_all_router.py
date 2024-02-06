from logging import getLogger
from fastapi import APIRouter, Query

from config.settings import settings
from db.es import es_conn, search_result

get_all_router = APIRouter()

LOGGER = getLogger(__name__)
es = es_conn()
index_name = settings["index_name"]


@get_all_router.get("/", response_model=list)
async def get_all(
        pagination_size: int = Query(None, description="кол-во ответов на странице"),
        pagination_from: int = Query(None, description="номер начального ответа"),
) -> list:
    """Getting all data from the database"""
    body = {
        "size": pagination_size,
        "from": pagination_from,
    }
    return await search_result(body)
