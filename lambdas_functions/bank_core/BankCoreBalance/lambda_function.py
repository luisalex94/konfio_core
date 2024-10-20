from repository import DynamoDBRepository
from utils import get_body, calculate_balance, response_200, response_400, response_500

database = DynamoDBRepository('bank_core_ddbb')

def lambda_handler(event, context):

    body = get_body(event)

    '''
    In this section is where the code ask to user_core_valid_user_info lambda function if the user is valid
    '''

    account = body.get('account')

    movements = database.get_movements(account)

    if not movements:
        return response_400('Account not found')
    
    balance = calculate_balance(movements)
    
    return response_200(balance)