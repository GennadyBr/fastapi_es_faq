import csv
import json
from logging import getLogger

from dotenv import load_dotenv
from elasticsearch import ApiError
from elasticsearch import NotFoundError, Elasticsearch

from config.logging_setup import LoggerSetup
from config.settings import settings
from db.es import es_conn

load_dotenv()
logger_setup = LoggerSetup()
LOGGER = getLogger(__name__)


def _load_data(es: Elasticsearch, index_name: str) -> None:
    """
    Load data from csv file to Elasticsearch cluster by index_name parameter
    :param es: Elasticsearch
    :param index_name: str
    :return: None
    """
    try:
        with open(settings["csv_file"], "r") as f:
            reader = csv.reader(f, delimiter=settings["delimiter"])
            LOGGER.info("LOADING STARTED")
            for i, line in enumerate(reader):
                document = {
                    "question": line[0],
                    "answer": line[1],
                }
                es.index(index=index_name, document=document)
    except FileNotFoundError as err:
        LOGGER.error(f"""CAN'T FIND {settings["csv_file"]}, {err=}""")

    LOGGER.info("LOADING COMPLETED")


def _check_index(index_name: str) -> None:
    """
    Check index in Elasticsearch cluster by index_name parameter
    :param es: Elasticsearch
    :param index_name: str
    :return: None
    """
    if not es.indices.exists(index=index_name):
        try:
            with open(settings["index_file"], "r") as index_file:
                data = json.load(index_file)
                es.indices.create(index=index_name, body=data)
        except FileNotFoundError as err:
            LOGGER.error(f"""CAN'T FIND {settings["index_file"]}, {err=}""")


def _check_is_data(index_name: str, es: Elasticsearch) -> None:
    """
    Check is data in Elasticsearch cluster by index_name parameter
    :param es: Elasticsearch
    :param index_name: str
    :return: None
    """
    try:
        doc_count = es.count(index=index_name)["count"]
    except NotFoundError as err:
        LOGGER.error(
            f'No existing index {settings["index_name"]} '
            f"lets start loading new data into new index "
            f"{err}"
        )
        _load_data(es=es, index_name=index_name)
    except AttributeError as err:
        LOGGER.error(f"doc_count {err}")
    except ApiError as err:
        LOGGER.error(
            f"Something wrong with ES elastic_2_volume. "
            f"Lets delete volume and start again {err}"
        )
    else:
        if not doc_count:
            _load_data(es=es, index_name=index_name)
        else:
            LOGGER.info(f"Elasticsearch contains {doc_count} docs")


if __name__ == "__main__":
    es = es_conn()
    index_name = settings["index_name"]
    _check_index(index_name=index_name)
    _check_is_data(index_name=index_name, es=es)

    # docker exec elastic_5 curl -X DELETE 'http://localhost:9200/faq'
