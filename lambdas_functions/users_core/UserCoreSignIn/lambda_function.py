from utils import get_body, response_200, response_400, response_500
from repository import DynamoDBRepository

database = DynamoDBRepository('user_core_ddbb')


def lambda_handler(event, context):

    body = get_body(event)

    if body is None:
        return response_400('Invalid JSON')

    account = body.get('account')
    password = body.get('password')

    if not account:
        return response_400('account is required')

    if not password:
        return response_400('password is required')

    user = database.get_user(account)

    if not user:
        return response_400('User not found')

    if user['password'] != password:
        return response_400('Invalid password')

    return response_200(user)
