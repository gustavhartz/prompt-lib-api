import json


def lambda_handler(event, context):
    # Sample prompts data
    sample_data = {
        "prompts": [
            {
                "id": 1,
                "title": "The Time Traveler",
                "description": "Write a story about a time traveler.",
            },
            {
                "id": 2,
                "title": "The Lost City",
                "description": "Describe the discovery of a lost city.",
            },
            {
                "id": 3,
                "title": "AI Utopia",
                "description": "Imagine a world where AI has created a utopia.",
            },
        ]
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(sample_data),
    }
