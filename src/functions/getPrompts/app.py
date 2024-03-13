import json
from logger import setup_logger
from db import list_prompts
import requests

logger = setup_logger(__name__)


def lambda_handler(event, context):
    logger.info(f"Search prompt request")
    # Get prompts from the database
    search_query = event.get("queryStringParameters", {})
    if search_query:
        search_query = search_query.get("search", None)
        logger.info(f"Search parameters: {search_query}")

    try:
        prompts = list_prompts(search_query)
        return {
            "statusCode": 200,
            "body": json.dumps({"prompts": prompts}),
        }
    except Exception as e:
        logger.error(f"Error getting prompts: {e}")

        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"}),
        }
