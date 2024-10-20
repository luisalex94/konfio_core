from utils import get_body, response_200, response_400, response_500, update_user_info
from repository import DynamoDBRepository

database = DynamoDBRepository('user_core_ddbb')


def lambda_handler(event, context):
    
    body = get_body(event)
    
    if body is None:
        return response_400('Invalid JSON')
    
    account = body.get('account')
    name = body.get('name')
    address = body.get('address')
    
    if not account:
        return response_400('Account is requiered')
    
    user = database.get_user(account)
    
    if not user:
        return response_400('User not found')
    
    user = update_user_info(user)
    
    database.update_user(user)
    
    return response_200('User update complete')