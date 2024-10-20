from repository import DynamoDBRepository
from movement_strategy import ChargeMovementStrategy
from utils import get_body, generate_movement_id, response_200, response_400, response_500, has_sufficient_founds

database = DynamoDBRepository('bank_core_ddbb')


def lambda_handler(event, context):

    body = get_body(event)

    '''
        In this section is where the code ask to user_core_valid_user_info lambda function if the user is valid
        '''

    account = body.get('account')
    concept = body.get('concept')
    amount = body.get('amount')
    date = body.get('date')

    movement_id = generate_movement_id()

    movements = database.get_movements(account)

    if not movements:
        return response_400('Account not found')

    if not has_sufficient_founds(movements, amount):
        return response_400('Insufficient funds')

    add_movement(database, account, movements,
                 movement_id, concept, amount, date)

    return response_200('Charge movement successfully added')


def add_movement(database, account, movements, movement_id, concept, amount, date):
    ChargeMovementStrategy().add_movement(
        movements, movement_id, concept, amount, date)
    database.update_account_movements(account, movements)
