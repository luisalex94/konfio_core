import json
from lambdas_functions.bank_core.BankCoreJwtTesting import lambda_function

def test_lambda():
    event = {
        "key": "value1"
    }
    context = None
    
    response = lambda_function.lambda_handler(event, context)
    print("Respuesta lambda_handler: ", json.dumps(response, indent=2))
    
if __name__ == "__main__":
    test_lambda()