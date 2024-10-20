from repository import DynamoDBRepository
from utils import get_body, create_accout_data, create_bank_data, response_200, response_400, response_500

user_database = DynamoDBRepository('user_core_ddbb')
bank_database = DynamoDBRepository('bank_core_ddbb')


def lambda_handler(event, context):

    body = get_body(event)

    if body is None:
        return response_400('Invalid JSON')

    user = body.get('user')
    name = body.get('name')
    address = body.get('address')
    password = body.get('password')

    if not user or not name or not address or not password:
        return response_400('User, name, address and password are requiered')

    account_data = create_accout_data(user, name, address, password)

    user_database.create_user_users(account_data)

    bank_data = create_bank_data(account_data['account'])

    bank_database.create_user_bank(bank_data)

    return response_200('User created')
