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

        # Return the movements
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
        

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error querying the database: {str(e)}")
        }