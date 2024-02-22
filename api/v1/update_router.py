from logging import getLogger

from fastapi import APIRouter
from fastapi import Query

from config.settings import settings
from db.es import es_conn

LOGGER = getLogger(__name__)
es = es_conn()
index_name = settings["index_name"]

update_router = APIRouter()


@update_router.post("/", response_model=dict)
async def update(
    id: str = Query(None),
    question: str = Query(None),
    answer: str = Query(None),
) -> dict:
    """
    Update record in Elasticsearch cluster by id parameter
    :param id: str
    :param question: str
    :param answer: str
    :return: dict
    """
    document = {
        "question": question,
        "answer": answer,
    }
    return es.index(index=index_name, document=document, id=id)
