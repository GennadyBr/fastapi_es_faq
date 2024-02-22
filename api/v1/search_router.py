from logging import getLogger

from fastapi import APIRouter
from fastapi import Query

from config.settings import settings
from db.es import es_conn
from db.es import search_by_field

LOGGER = getLogger(__name__)

search_router = APIRouter()

es = es_conn()
index_name = settings["index_name"]


@search_router.get("/question", response_model=list)
async def search_question(
    question_text=Query(..., description="задайте вопрос"),
    pagination_size: int = Query(None, description="кол-во ответов на странице"),
    pagination_from: int = Query(None, description="номер начального ответа"),
) -> list:
    """
    Search by question
    :param question_text:
    :param pagination_size:
    :param pagination_from:
    :return: list
    """
    result = await search_by_field(
        question_text, pagination_size, pagination_from, search_field="question"
    )
    return result


@search_router.get("/answer", response_model=list)
async def search_answer(
    question_text: str = Query(..., description="задайте поиск по ответам"),
    pagination_size: int = Query(None, description="кол-во ответов на странице"),
    pagination_from: int = Query(None, description="номер начального ответа"),
) -> list:
    """
    Search by answer
    :param question_text: str
    :param pagination_size: int
    :param pagination_from: int
    :return: list
    """
    result = await search_by_field(
        question_text, pagination_size, pagination_from, search_field="answer"
    )
    return result
