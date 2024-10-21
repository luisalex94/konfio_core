from repository import send_email
from utils import get_body, response_200, response_400, response_500


def lambda_handler(event, context):

    body = get_body(event)

    if body is None:
        return response_400('Invalid JSON')

    print('body of lambda function: ', body)

    source = body.get('source')
    destination_email = body.get('destination_email')
    body = body.get('body')

    destination = {"ToAddresses": [destination_email]}

    subject = "test subject from lambda"
    body = body
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}

    response = send_email(source, destination, message)

    return response_200(response)
