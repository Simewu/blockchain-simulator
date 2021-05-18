# This script downloads the latest bitnodes_nodes.json file off Bitnodes, then goes through each address and individually requests its latency data, saving it into the latencies directory.
# To prevent DoS attacks, Bitnodes only enables a certain amount of queries per day, so the entire dataset may take several days to fully complete.

import re
import json
import os
import random
import urllib.request
import sys

print('Downloading IP addresses...')
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve('https://bitnodes.io/api/v1/snapshots/latest', 'bitnodes_nodes.json')
print('Done. Addresses updated!')


# Read the addresses file
file = open('bitnodes_nodes.json', 'r', encoding = 'utf8')
data = json.load(file)
addresses = []

for item in data:
	if item == 'nodes':
		nodes = data[item]
		print(f'Nodes ({len(nodes)}):')
		for address in nodes:
			match_ipv4 = re.match(r'^([^:]+):([^:A-Za-z]+)$', address)
			match_ipv6 = re.match(r'^\[?([0-9A-Fa-f:]+)\]?:([^:A-Za-z]+)$', address)
			match_onion = re.match(r'^([^\.]+\.onion):([^:A-Za-z]+)$', address)

			if match_ipv4 != None:
				ip = match_ipv4.group(1)
				port = match_ipv4.group(2)
				addresses.append([ip, port])

			elif match_ipv6 != None:
				ip = match_ipv6.group(1)
				port = match_ipv6.group(2)
				addresses.append([ip, port])

			elif match_onion != None:
				ip = match_onion.group(1)
				port = match_onion.group(2)
				addresses.append([ip, port])
	else:
		print(f'{item.capitalize()}: {data[item]}')

file.close()
#random.shuffle(addresses)

if not os.path.exists('latencies'):
	os.makedirs('latencies')

for i, address in enumerate(addresses):
	ip = address[0]
	port = address[1]
	filePath = 'latencies/' + re.sub('[^A-Za-z0-9\.]', '-', f'{ip}-{port}') + '.json'

	if not os.path.exists(filePath):
		print(f'Fetching latency for {ip}:{port}...')

		url = f'https://bitnodes.io/api/v1/nodes/{ip}-{port}/latency/'
		
		try:
			opener = urllib.request.build_opener()
			opener.addheaders = [('User-agent', 'Mozilla/5.0')]
			urllib.request.install_opener(opener)
			urllib.request.urlretrieve(url, filePath)
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			pass
	else:
		print(f'Latency for {ip}:{port} already cached.')





