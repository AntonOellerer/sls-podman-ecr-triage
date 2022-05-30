import logging

from aws_lambda_typing import context as context_, events


logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)

def test(event: events.S3Event, context: context_.Context) -> None:
    print("Hello world")