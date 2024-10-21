from repository import send_email
from utils import get_body, response_200, response_400, response_500, message_constructor


def lambda_handler(event, context):

    body = get_body(event)

    if body is None:
        return response_400('Invalid JSON')

    source = body.get('source')
    destination_email = body.get('destination_email')
    body = body.get('body')
    subject = body.get('subject')

    destination = {"ToAddresses": [destination_email]}
    
    message = message_constructor(subject, body)

    response = send_email(source, destination, message)

    return response_200(response)
