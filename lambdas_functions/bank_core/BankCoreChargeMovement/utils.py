import json
import random


def get_body(event):
    if 'body' in event:
        try:
            return json.loads(event['body'])
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON')
    return event


def has_sufficient_founds(movements, amount):
    balance = sum(item['amount'] for item in movements['movements'])
    return balance >= amount


def generate_movement_id():
    return random.randint(0000000000, 9999999999)


def response_200(message):
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }


def response_400(message):
    return {
        'statusCode': 400,
        'body': json.dumps(message)
    }


def response_500():
    return {
        'statusCode': 500,
        'body': json.dumps('Internal server error')
    }
