import math
import sys
import threading
import time

class TestRunner:
    def __init__(self, concurrency = 1):
        self.concurrency = concurrency

    def start(self):
        threads = []
        for i in range(0, self.concurrency):
            scenarios_per_thread = len(TEST_SCENARIOS) / 2
            start_index = int(i * scenarios_per_thread)
            end_index = int(math.ceil((i+1) * scenarios_per_thread))
            print('Starting thread: ', i, ' Scenarios Per Thread: ', scenarios_per_thread, ' start: ', start_index, ' end: ', end_index)
            
            scenarios = TEST_SCENARIOS[start_index:end_index]
            thread = TestThread(scenarios)
            thread.start()
            threads.append(thread)
            

class TestThread:
    def __init__(self, scenarios):
        self.scenarios = scenarios

    def start(self): 
        self.thread = threading.Thread(target=self.run, args={})
        self.thread.start()

    def run(self): 
        for scenario in self.scenarios:
            print('Running scenario: ', scenario.test_name)
            time.sleep(5)
            print('Ran scenario: ', scenario.test_name)
            

class TestScenario:
    def __init__(self, test_name, test_variables):
        self.test_name = test_name
        self.test_variables = test_variables


TEST_SCENARIOS = [
    TestScenario('945d7cd8-c782-4fea-8af6-eddede757f9f', {}),
    # TestScenario('945d7cd8-c782-4fea-8af6-eddede757f9f', {}),
    # TestScenario('945d7cd8-c782-4fea-8af6-eddede757f9f', {}),
    # TestScenario('945d7cd8-c782-4fea-8af6-eddede757f9f', {})
]

if __name__ == "__main__":
    # api_key = os.environ.get('BESPOKEN_API_KEY')
    # if api_key is None:
    #     raise Exception('Environment variable BESPOKEN_API_KEY must be set')
    
    concurrency = int(sys.argv[1])
    print('Starting running with concurrency: ', concurrency)
    runner = TestRunner(concurrency)
    runner.start()
