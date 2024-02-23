"""
api/v1/register_router.py

Add new record of question and answer to Elasticsearch cluster

"""

from logging import getLogger

from fastapi import APIRouter
from fastapi import Query

from config.settings import settings
from db.es import es_conn

LOGGER = getLogger(__name__)
es = es_conn()
index_name = settings["index_name"]

register_router = APIRouter()


@register_router.post("/", response_model=dict)
async def register(
    question: str = Query(None),
    answer: str = Query(None),
) -> dict:
    """
    Add new record to Elasticsearch cluster

    :param question: str

    :param answer: str

    :return: dict
    """
    document = {
        "question": question,
        "answer": answer,
    }
    return es.index(index=index_name, document=document)
