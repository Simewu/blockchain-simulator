# This file should be ran once all node data is inside the latencies directory (via download_latencies.py).
# This file converts the dataset into a simple CSV file names "bitcoin_latencies.csv".

import os
import re
import json

outputFile = open(f'bitcoin_latencies.csv', 'w', newline='')

line = 'Address,'
line += 'Port,'
line += 'Address Type,'
line += 'Latency (ms),'
line += 'Latest fetch,'
line += 'Online since'

outputFile.write(line + '\n')

# List the files with a regular expression
def listFiles(regex, directory):
	path = os.path.join(os.curdir, directory)
	return [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and bool(re.match(regex, file))]

files = listFiles(r'', 'latencies')
for file in files:
	latency_sum = 0
	latency_num = 0

	latest_fetch = 0
	online_since = 0
	with open(file) as json_file:
		data = json.load(json_file)

		if 'daily_latency' in data:
			latest_fetch = data['daily_latency'][-1]['t']

		if 'monthly_latency' in data:
			online_since = data['monthly_latency'][0]['t']

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
		port = address[last_char_index+1:]
		address = address[:last_char_index]
		address_full = address + ':' + port
		
		address_type = ''
		#match_ipv4 = re.match(r'^([^:]+):([0-9]+)$', address_full)
		match_ipv4 = re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', address)
		match_ipv6 = re.match(r'^\[?([0-9A-Fa-f:\-]+)\]?$', address_full)
		match_onion = re.match(r'^([^\.]+\.onion):([0-9]+)$', address_full)
		if match_ipv4 != None: address_type = 'IPv4'
		elif match_ipv6 != None: address_type = 'IPv6'
		elif match_onion != None:
			if len(address) == 16 + 6: address_type = 'Onion v2'
			elif len(address) == 56 + 6: address_type = 'Onion v3'
			else: address_type = 'Onion'
		else: address_type = 'Unknown'

		latency = latency_sum / latency_num
		line = address + ','
		line += port + ','
		line += address_type + ','
		line += str(latency) + ','
		line += str(latest_fetch) + ','
		line += str(online_since)
		outputFile.write(line + '\n')


	print(f'Processed {address_type} {file}')
	# if address_type == 'Unknown':
	# 	print('Unknown address type:')
	# 	sys.exit()

outputFile.close()
	
