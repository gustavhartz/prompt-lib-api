import json
from libs.db import list_prompts
from libs.logger import setup_logger

logger = setup_logger(__name__)


def lambda_handler(event, context):

    # Get prompts from the database
    query_params = event.get("queryStringParameters", {})
    search_query = query_params.get("search", None)

    # Sample prompts data
    try:
        prompts = list_prompts(search_query)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {"prompts": prompts}, default=str
            ),  # Use default=str to handle datetime serialization
        }
    except Exception as e:
        logger.exception(e)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"}),
        }
