def lambda_handler(event, context):
    token = event['authorizationToken']
    effect = 'Deny'
    if token == 'cs':
        effect = 'Allow'
        
    return {
        'principalId': '*',
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': event['methodArn']
                }
            ]
        }
    }
