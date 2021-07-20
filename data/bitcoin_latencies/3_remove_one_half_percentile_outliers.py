# Given the bitcoin_latencies.csv file, this file will strip off the top 1 percentile and bottom 1 percentile of the data
# The data will be outputted to bitcoin_latencies_removed_1_percentile.csv

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
	return [numpy.percentile(latencies, 0.5), numpy.percentile(latencies, 99.5)]

quantiles = getQuantiles()
print('Top 0.5% quantiles: ', quantiles)

# Re-read the file, but this time save the ones within the percentile
readerFile = open('bitcoin_latencies.csv', 'r')
reader = csv.reader(x.replace('\0', '') for x in readerFile)

writerFile = open(f'bitcoin_latencies_removed_0.5_percentile.csv', 'w', newline='')
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