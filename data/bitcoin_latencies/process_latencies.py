# This file should be ran once all node data is inside the latencies directory (via download_latencies.py).
# This file converts the dataset into a simple CSV file names "bitcoin_latencies.csv".

import os
import re
import json

outputFile = open(f'bitcoin_latencies.csv', 'w', newline='')

line = 'Address,'
line += 'Latency (ms)'

outputFile.write(line + '\n')

# List the files with a regular expression
def listFiles(regex, directory):
	path = os.path.join(os.curdir, directory)
	return [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and bool(re.match(regex, file))]

files = listFiles(r'', 'latencies')
for file in files:
	print(f'Processing {file}')
	latency_sum = 0
	latency_num = 0
	with open(file) as json_file:
		data = json.load(json_file)
		if 'monthly_latency' in data:
			try:
				for month in data['monthly_latency']:
					if month['v'] > 0:
						latency_sum += month['v']
						latency_num += 1
			except:
				pass
	if latency_num != 0:
		address = os.path.splitext(os.path.basename(file))[0]
		last_char_index = address.rfind('-')
		address = address[:last_char_index] + ':' + address[last_char_index+1:]


		latency = latency_sum / latency_num
		line = address + ','
		line += str(latency)
		outputFile.write(line + '\n')

outputFile.close()
	
