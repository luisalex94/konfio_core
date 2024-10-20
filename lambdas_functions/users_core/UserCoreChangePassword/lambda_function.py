from utils import get_body, response_200, response_400, response_500
from repository import DynamoDBRepository

database = DynamoDBRepository('user_core_ddbb')


def lambda_handler(event, context):

    body = get_body(event)

    if body is None:
        return response_400('Invalid JSON')

    account = body.get('account')
    old_password = body.get('password')
    new_password = body.get('new_password')

    if not account:
        return response_400('Account is requiered')

    if not old_password:
        return response_400('Password is requiered')

    if not new_password:
        return response_400('New password is requiered')

    user = database.get_user(account)

    user_alias = user['user']
    actual_password = user['password']

    if not user:
        return response_400('User not found')

    database.update_password(
        account, user_alias, actual_password, old_password, new_password)

    return response_200('Password update complete')
