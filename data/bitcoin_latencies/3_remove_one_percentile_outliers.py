#! This file should be ran once all node data is inside the latencies directory (via download_latencies.py).
#! This file converts the dataset into a simple CSV file names "bitcoin_latencies.csv".

import csv
import numpy

# Return the threshold separating the top 99% of the data
def getQuantiles():
	readerFile = open('bitcoin_latencies.csv', 'r')
	reader = csv.reader(x.replace('\0', '') for x in readerFile)
	latencies = []
	tempHeader = next(reader)
	for row in reader:
		latencies.append(float(row[1]))
	readerFile.close()
	return [numpy.percentile(latencies, 1), numpy.percentile(latencies, 99)]

quantiles = getQuantiles()
print('Top 1% quantiles: ', quantiles)

# Re-read the file, but this time save the ones within the percentile
readerFile = open('bitcoin_latencies.csv', 'r')
reader = csv.reader(x.replace('\0', '') for x in readerFile)

writerFile = open(f'bitcoin_latencies_removed_1_percentile.csv', 'w', newline='')
writer = csv.writer(writerFile)

# Copy over the header
writer.writerow(next(reader))

numRows = 0
numRemovedRows = 0

for row in reader:
	latency = float(row[1])
	if latency > quantiles[0] and latency < quantiles[1]:
		writer.writerow(row)
	else:
		numRemovedRows += 1
	numRows += 1

readerFile.close()
writerFile.close()

print('\nRows removed:', numRemovedRows, 'out of', numRows)
print('Success.')