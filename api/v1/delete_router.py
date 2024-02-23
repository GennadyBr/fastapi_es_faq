"""
api/v1/delete_router.py

Delete record from Elasticsearch cluster by id parameter

"""
from logging import getLogger

from fastapi import APIRouter
from fastapi import Query

from config.settings import settings
from db.es import es_conn

LOGGER = getLogger(__name__)
es = es_conn()
index_name = settings["index_name"]

delete_router = APIRouter()


@delete_router.delete("/", response_model=dict)
async def delete(
    id: str = Query(None),
) -> dict:
    """
    Delete record from Elasticsearch cluster by id parameter

    :param id: str

    :return: dict
    """
    response = es.delete(index=index_name, id=id)
    return response
