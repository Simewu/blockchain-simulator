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
