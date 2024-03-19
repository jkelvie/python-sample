


s = 'Select an optionApple Inc.(060704780-Cupertino CA)Open menu\nApple Inc.\'s diversity and inclusion score is 70 out of 100. However, the data does not provide specific details about the number of female or minority employees in business management.\nAs for individual investors and ownership, the data does not provide any information on this topic.\nWas this helpful?\nYesNo'
s = s.split('Open menu')[1]
print('1', s)
s = s.split('Was this helpful?')[0]
print('2', s)