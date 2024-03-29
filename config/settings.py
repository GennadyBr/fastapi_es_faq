"""
config/settings.py

Settings for ElasticSearch cluster and CSV file
"""


settings = {
    "index_file": "es_index.json",
    "index_name": "faq",
    "max_size": 5000,
    "csv_file": "faq.csv",
    "delimiter": ";",
}
