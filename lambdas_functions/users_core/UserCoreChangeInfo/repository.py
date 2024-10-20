import json
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

    def update_user(self, account: str, user: str, name: str, address: str):
        self.table.update_item(
            Key={'account': account, 'user': user},  # Partition key + Sort key
            UpdateExpression='SET #nm = :name, address = :address',
            ExpressionAttributeNames={'#nm': 'name'},
            ExpressionAttributeValues={':name': name, ':address': address}
        )
