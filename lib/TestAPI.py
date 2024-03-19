import json
import os
import requests
import time

BASE_URL = "https://monolith.bespoken.io"
if os.environ.get('BESPOKEN_API_BASE_URL') is not None:
    BASE_URL = os.environ.get('BESPOKEN_API_BASE_URL')

class TestAPI:
    
    def __init__(self, api_key):
        self.api_key = api_key


    def run_test(self, test_suite_name, variables={}):
        # The API endpoint
        url = "{base_url}/api/test-suite/{test_suite_name}/run?api-key={api_key}".format(
            api_key=self.api_key,
            base_url=BASE_URL,
            test_suite_name=test_suite_name
        )
        print("Running test with URL: ", url, " Data: ", json.dumps(variables))


        # # The API endpoint to communicate with
        # url_post = "https://jsonplaceholder.typicode.com/posts"

        # A POST request to tthe API
        post_response = requests.post(url, json=variables)

        # Print the response
        response_json = post_response.json()
        print('Initial response: ', response_json)

        run_id = response_json['id']
        while response_json['status'] == 'IN_PROGRESS':
            time.sleep(1)
            status_url = "{base_url}/api/test-run/{test_run_id}?api-key={api_key}".format(
                api_key=self.api_key,
                base_url=BASE_URL,
                test_run_id=run_id
            )
            print("Run status URL: ", status_url)

            status_response = requests.get(status_url)
            response_json = status_response.json()
            print('Status response: ', response_json)
        
        print('Final response received!')


if __name__ == "__main__":
    api_key = os.environ.get('BESPOKEN_API_KEY')
    if api_key is None:
        raise Exception('Environment variable BESPOKEN_API_KEY must be set')
    
    testAPI = TestAPI(api_key)
    testAPI.run_test('Dun and Bradstreet - Location', {
        'COMPANY_NAME': 'Pfizer',
        'EXPECTED_LOCATION': 'New York'
    })