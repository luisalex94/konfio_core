from repository import send_email
from utils import get_body, response_200, response_400, response_500, message_constructor, mail_body_constructor


def lambda_handler(event, context):

    body = get_body(event)

    if body is None:
        return response_400('Invalid JSON')

    source = body.get('source')
    destination_email = body.get('destination_email')
    subject = body.get('subject')
    mail_body = body.get('body')
    name = body.get('user_name')
    account = body.get('account')

    destination = {"ToAddresses": [destination_email]}
    
    mail_body = mail_body_constructor(name, account)
    
    message = message_constructor(subject, mail_body)

    response = send_email(source, destination, message)

    return response_200(response)
