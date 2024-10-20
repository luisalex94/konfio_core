import json

def get_body(event):
    if 'body' in event:
        try:
            return json.loads(event['body'])
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON')
    return event

def calculate_balance(movements):
    return sum(item['amount'] for item in movements['movements'])

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