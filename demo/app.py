import os
import json
import boto3
# import requests
# a sample demo code to obtain id item from DynamoDB Table

table_name = os.environ.get('TABLE_NAME', 'ap-northeast-1')

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    try:
        region = os.environ.get('AWS_DEFAULT_REGION', 'ap-northeast-1')
        dynamodb = boto3.resource ("dynamodb", region_name=region)

        query = event['queryStringParameters']
        item_id = query['id'] # obtain querystring id
        table = dynamodb.Table(table_name) # set a DynamoDB table
        res = table.get_item(Key={'id': item_id}) # obtain an item from the table
        res = res['Item']
        print(res)
        
        return {
            "statusCode": 200,
            "body": json.dumps(res),
            "headers": {
                'content-type': 'application/json'
            },
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": e.args
            }),
            "headers": {
                'content-type': 'application/json'
            },
        }

if __name__ == "__main__":
    lambda_handler(json.loads(sys.args[1]), {})

