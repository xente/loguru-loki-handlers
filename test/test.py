from loki_handler import loki_handler
from loguru import logger
import os

os.environ[
    "LOKI_URL"
] = "https://138074:eyJrIjoiMWVlYzcyNzU3MTk0YTQ4NjRkMTg3ZTBlYWY1ZTZlN2NhMzc4ZDZlOCIsIm4iOiJrZW5rbyIsImlkIjo1NzY5NDh9@logs-prod-eu-west-0.grafana.net/loki/api/v1/push"


def run():
    
    logger.info("Starting service")
    
    logger.info(
        "Request return {code} HTTP/1.1 GET {url}",
        code=200,
        url="https://loki_handler.io",
    )


logger.configure(
    handlers=[
        {
            "sink": loki_handler(
                os.environ["LOKI_URL"],
                {"application": "Test", "envornment": "develop"},
                {"thread"},
            ),
            "serialize": True,
        }
    ]
)
run()

