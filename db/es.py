import os
from logging import getLogger
from time import sleep

from dotenv import load_dotenv
from elastic_transport import ConnectionError
from elasticsearch import Elasticsearch

from config.settings import settings

load_dotenv()
LOGGER = getLogger(__name__)
index_name = settings["index_name"]


def es_conn() -> Elasticsearch:
    url = f"http://{os.getenv('ES_HOST')}:{int(os.getenv('ES_PORT'))}"
    for i in range(10):
        try:
            es = Elasticsearch(url)
            LOGGER.info(
                f"Connecting to Elasticsearch cluster "
                f'`{es.info().body["cluster_name"]}`'
            )
        except ConnectionError as err:
            LOGGER.error(f"es_conn#{i}; {err}")
            sleep(5)
        else:
            LOGGER.info(f"es_conn#{i} CONNECTION ESTABLISHED")
            return es


async def search_result(body):
    es = es_conn()

    response = es.search(index=index_name, body=body)
    sorted_response = sorted(
        response["hits"]["hits"], key=lambda k: k["_score"], reverse=True
    )
    result = [
        {
            "_id": d["_id"],
            "_source": d["_source"],
            "score": d["_score"],
        }
        for d in sorted_response
    ]
    LOGGER.info(f"Найдено {len(result)=} записей")
    return result


async def search_by_field(
    question_text, pagination_size, pagination_from, search_field
):
    body = {
        "size": pagination_size,
        "from": pagination_from,
        "query": {"match": {search_field: question_text}},
    }
    return await search_result(body)
