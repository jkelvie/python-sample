from Printer import Printer
from TestAPI import TestAPI

import json
import math
import os
import sys
import threading
import time

class TestRunner:
    def __init__(self, concurrency = 1):
        self.concurrency = concurrency
        self.results = []

    def add_result(self, result):
        self.results.append(result)
        print('captured result for: ', result.scenario.test_name)
        printer = Printer('output/out.csv')
        try:
            printer.print(self.results)
        except:
            print('error')

    def start(self):
        threads = []
        for i in range(0, self.concurrency):
            scenarios_per_thread = len(TEST_SCENARIOS) / 2
            start_index = int(i * scenarios_per_thread)
            end_index = int(math.ceil((i+1) * scenarios_per_thread))
            print('Starting thread: ', i, ' Scenarios Per Thread: ', scenarios_per_thread, ' start: ', start_index, ' end: ', end_index)
            
            scenarios = TEST_SCENARIOS[start_index:end_index]
            thread = TestThread(self, scenarios)
            thread.start()
            threads.append(thread)
            

class TestThread:
    def __init__(self, runner, scenarios):
        self.runner = runner
        self.scenarios = scenarios

    def start(self): 
        self.thread = threading.Thread(target=self.run, args={})
        self.thread.start()

    def run(self): 
        testAPI = TestAPI(API_KEY)
        for scenario in self.scenarios:
            print('Running scenario: ', scenario.test_name, ' With variables: ', json.dumps(scenario.test_variables))
            result_json = testAPI.run_test(scenario.test_name, scenario.test_variables)
            print('Ran scenario: ', scenario.test_name)
            result = TestResult(scenario, result_json)
            self.runner.add_result(result)
            try:
                print('last response: ', result.last_response())
            except:
                print('error getting last response')
            

class TestScenario:
    def __init__(self, test_name, test_variables):
        self.test_name = test_name
        self.test_variables = test_variables


class TestResult:
    def __init__(self, scenario, json):
        self.scenario = scenario
        self.json = json

    def last_response(self):
        last_result = self.json['results'][0]
        print('last result: ', json.dumps(last_result))
        last_interaction = last_result['interactions'][len(last_result['interactions']) - 1]
        print('interaction length: ', len(last_result['interactions']))
        print('last interaction: ', json.dumps(last_interaction))
        last_value = last_interaction['actualValue']
        print('last value: ', last_value)
        
        return last_value


TEST_SCENARIOS = [
    TestScenario('Dun and Bradstreet - Location', {
        'COMPANY_NAME': 'Pfizer',
        'EXPECTED_LOCATION': 'New York',
    }),
    # TestScenario('945d7cd8-c782-4fea-8af6-eddede757f9f', {}),
    # TestScenario('945d7cd8-c782-4fea-8af6-eddede757f9f', {}),
    # TestScenario('945d7cd8-c782-4fea-8af6-eddede757f9f', {})
]

API_KEY = None
if __name__ == "__main__":
    API_KEY = os.environ.get('BESPOKEN_API_KEY')
    if API_KEY is None:
        raise Exception('Environment variable BESPOKEN_API_KEY must be set')
    
    concurrency = int(sys.argv[1])
    print('Starting running with concurrency: ', concurrency)
    runner = TestRunner(concurrency)
    runner.start()
