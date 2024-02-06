from logging import getLogger

from fastapi import APIRouter, Query

from config.settings import settings
from db.es import es_conn, search_by_field

LOGGER = getLogger(__name__)

search_router = APIRouter()

LOGGER = getLogger(__name__)
es = es_conn()
index_name = settings["index_name"]


@search_router.get("/question", response_model=list)
async def search_question(
        question_text=Query(..., description="задайте вопрос"),
        pagination_size: int = Query(None, description="кол-во ответов на странице"),
        pagination_from: int = Query(None, description="номер начального ответа"),

) -> list:
    """Search by question"""
    result = await search_by_field(question_text, pagination_size, pagination_from, search_field="question")
    return result


@search_router.get("/answer", response_model=list)
async def search_answer(
        question_text=Query(..., description="задайте поиск по ответам"),
        pagination_size: int = Query(None, description="кол-во ответов на странице"),
        pagination_from: int = Query(None, description="номер начального ответа"),

) -> list:
    """Search by answer"""
    result = await search_by_field(question_text, pagination_size, pagination_from, search_field="answer")
    return result
