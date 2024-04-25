# Standard Library
from urllib.parse import unquote_plus

# Third Party Library
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.data_classes import S3Event, event_source
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(level="DEBUG")
tracer = Tracer()


@tracer.capture_lambda_handler
@logger.inject_lambda_context(log_event=True)
@event_source(data_class=S3Event)
def lambda_handler(event: S3Event, context: LambdaContext) -> None:
    logger.debug(event)
    for record in event.records:
        logger.debug(record)
        object_key = unquote_plus(record.s3.get_object.key)
        logger.debug(object_key)
    return
