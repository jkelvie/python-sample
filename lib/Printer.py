import csv  
import json

class Printer:
    def __init__(self, output_file):
        self.output_file = output_file

    def print(self, results):
        header = ['Test', 'Variables', 'Result', 'URL']
        #data = ['Afghanistan', 652090, 'AF', 'AFG']

        with open(self.output_file, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            for result in results:
                data = [result.scenario.test_name, json.dumps(result.scenario.test_variables), '', '']
                # write the data
                writer.writerow(data)
