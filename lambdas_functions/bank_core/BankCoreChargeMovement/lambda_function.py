# LambdaFunction to charge a movement in dynamodb, this call first check if the balance is enough to do the movement, if it is enough, the movement is added to the account movements.

import json
import boto3                                # type: ignore
from boto3.dynamodb.conditions import Key   # type: ignore
import random

from repository import DynamoDBRepository
from utils import get_body

database = DynamoDBRepository('bank_core_ddbb')

def lambda_handler(event, context):
    
        body = get_body(event)
    
        '''
        In this section is where the code ask to user_core_valid_user_info lambda function if the user is valid
        '''
    
        # Get the movements from the dynamodb database with the account number as the key
    
        account = body.get('account')
        concept = body.get('concept')
        amount = body.get('amount')
        date = body.get('date')

        # genrate a random id de 10 digits
        id = random.randint(0000000000, 9999999999)

        # type of movement: deposit
        movement_type = 'charge'
    
        try:
            items = database.get_movements(account)
    
            balance = 0
            for item in items.get('movements'):
                balance += item.get('amount')
    
            if balance - amount < 0:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Insufficient funds')
                }
    
            items['movements'].append({
                'id': id,
                'type': movement_type,
                'concept': concept,
                'amount': -amount,
                'date': date
            })
            
            database.update_account_movements(account, items)
    
            return {
                'statusCode': 200,
                'body': json.dumps('Charge movement successfully added')
            }
        
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f"Error querying the database: {str(e)}")
            }