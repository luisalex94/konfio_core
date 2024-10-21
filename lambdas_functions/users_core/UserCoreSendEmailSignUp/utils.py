import json


def get_body(event):
    if 'body' in event:
        try:
            return json.loads(event['body'])
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON')
    return event


def message_constructor(subject, body):
    return {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}


def mail_body_constructor(name, account):
    return f"""
        <html>
        <head>
          <style>
            body {{
              font-family: Arial, sans-serif;
              color: #333333;
            }}
            h1 {{
              color: #1a73e8;
            }}
            p {{
              font-size: 16px;
            }}
            .footer {{
              margin-top: 20px;
              font-size: 12px;
              color: #777777;
            }}
          </style>
        </head>
        <body>
          <h1>Correo enviado desde Lambda</h1>
          <p>Hola <strong>{name}</strong>,</p>
          <p>Te enviamos este mensaje a la dirección: <strong>{account}</strong></p>
          <p><strong>{account}</strong></p>
          <div class="footer">
            <p>Este correo fue enviado automáticamente. No respondas a este mensaje.</p>
          </div>
        </body>
        </html>
    """


def response_200(body):
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }


def response_400(body):
    return {
        'statusCode': 400,
        'body': json.dumps(body)
    }


def response_500(body):
    return {
        'statusCode': 500,
        'body': json.dumps(body)
    }
