from logging import getLogger

from fastapi import APIRouter, Query

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
):  # body: UserCreate, db: AsyncSession = Depends(get_db)) -> str:
    """Creates new document"""
    document = {
        "question": question,
        "answer": answer,
    }
    return es.index(index=index_name, document=document)
