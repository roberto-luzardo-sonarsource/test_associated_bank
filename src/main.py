def lambda_handler(event, context):

    # Placeholder Code

    print('Placeholder code')
    
    var = "test value"

    print("Event Contents")
    print(event)
    # print("Context Contents")
    # print(context)
    
    return {

        'statusCode': 200,

        'body': json.dumps('Hello from Lambda!')

    }
