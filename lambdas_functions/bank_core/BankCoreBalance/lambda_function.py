# Lambda function to access to dynamodb table bank_core_ddbb, get the movements of an account, sum the movements and return the balance of the account.

import json
import boto3                                # type: ignore
from boto3.dynamodb.conditions import Key   # type: ignore

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bank_core_ddbb')

def lambda_handler(event, context):

    if 'body' in event:
        try:
            body = json.loads(event['body'])
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON')
            }
        
    else:
        body = event

    '''
    In this section is where the code ask to user_core_valid_user_info lambda function if the user is valid
    '''

    # Get the movements from the dynamodb database with the account number as the key

    account = body.get('account')

    try:
        response = table.query(
            KeyConditionExpression=Key('account').eq(account)
        )
        items = response.get('Items', [])

        if not items:
            return {
                'statusCode': 404,
                'body': json.dumps('Account not found')
            }
        
        print('items001', items)

        # convert json to dict
        items = json.loads(json.dumps(items))

        print('items002', items)

        # access to the movements and sum them
        balance = 0
        for item in items.get('movements'):
            print('item:', item)    
            balance += item.get('amount')

        # Return the balance
        return {
            'statusCode': 200,
            'body': json.dumps(balance)
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error querying the database: {str(e)}")
        }