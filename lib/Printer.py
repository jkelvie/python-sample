import csv  
import json
import os

class Printer:
    def __init__(self, output_file):
        self.output_file = output_file
        
        # Create the output directory if it does not exist
        if not os.path.exists('output'):
            os.makedirs('output')

    def print(self, results):
        header = ['Test', 'Variables', 'Result']
        #data = ['Afghanistan', 652090, 'AF', 'AFG']

        with open(self.output_file, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            for result in results:
                variables = self.variables_to_string(result.scenario.test_variables)
                data = [result.scenario.test_name, variables, result.last_response()]
                # write the data
                writer.writerow(data)

    def variables_to_string(self, variables):
        s = ''
        for key in variables.keys():
            value = variables[key]
            s += key + ': ' + value + ';'
        return s
