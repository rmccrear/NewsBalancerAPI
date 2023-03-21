#Copyright (c) Microsoft Corporation. All rights reserved. #Licensed under the MIT License.
# -*- coding: utf-8 -*-
import json
import os
import requests
''' This sample makes a call to the Bing Web Search API with a query and returns relevant web search. Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview '''
# Add your Bing Search V7 subscription key and endpoint to your environment variables.

subscription_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
endpoint = os.environ['BING_SEARCH_V7_ENDPOINT'] + "/v7.0/news/search"

# Query term(s) to search for.
# query = "Microsoft"
query = "Will Smith Chris Rock"
# Construct a request
mkt = 'en-US'
params = {'q': query, 'mkt': mkt}
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
# Call the API

# try:
response = requests.get(endpoint, headers=headers, params=params)
# response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
response.raise_for_status()
# print(" Headers: ")
#print(response.headers)
json_data = response.json()
#print(" JSON Response: ")
print(json.dumps(json_data, indent=2))
#except Exception as ex:
#  raise ex
