import json

import requests


def getCreds():
    creds = dict()  # dictionary - holds all relevant data that we need to access API in an index
    creds['access_token'] = 'EAAEV0sTioxgBAMDkEROFDrECPWFESlJ6hY5ZAIJBhoIXP6TyFJNd7tZBIwye8y1Kn6yNTxUwllrezxBgZC87gQLqnZCFk3iis6xU7uy0vNJQ2xZA232myZB78XcO1cZCYzgHp3Ht8EdxVGmZAgngwshhHZAxSxfETKinmx71WHYmByHc3fhiD68NPUoH6GB7NCGOndIKgUKFNHgZDZD'
    creds['client id'] = '305469967213336'
    creds['client secret'] = ''
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v10.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'

    return creds


def makeApiCall(url, endpointParams, debug='no'):
    data = requests.get(url, endpointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['enpoint_params_pretty'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

    if ('yes' == debug):
        displayApiCallData(response)

    return response


def displayApiCallData(response):
    # prints out all data regarding the API call, if

    print("\nURL: ")  # title
    print(response['url'])  # display url hit
    print("\nEndpoint Params: ")  # title
    print(response['endpoint_params'])  # display params passed to the endpoint
    print("\nResponse: ")  # title
    print(response['json_data_pretty'])
