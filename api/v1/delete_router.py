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
):  # body: UserCreate, db: AsyncSession = Depends(get_db)) -> str:
    """Delete by id"""
    response = es.delete(index=index_name, id=id)
    return response
