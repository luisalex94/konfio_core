import boto3                                # type: ignore
from boto3.dynamodb.conditions import Key   # type: ignore

dynamodb = boto3.resource('dynamodb')


class DynamoDBRepository:
    def __init__(self, table_name: str):
        self.table = dynamodb.Table(table_name)

    def get_user(self, account: str):
        response = self.table.query(
            KeyConditionExpression=Key('account').eq(account)
        )
        items = response.get('Items', [])
        if items:
            return items[0]
        return None

    def update_password(self, account: str, user: str, actual_password: str, old_password: str, new_password: str):
        if actual_password != old_password:
            raise ValueError('Invalid password')
        self.table.update_item(
            Key={'account': account, 'user': user},  # Partition key + Sort key
            UpdateExpression='SET password = :password',
            ExpressionAttributeValues={':password': new_password}
        )
