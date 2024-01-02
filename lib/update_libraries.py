import requests
import os
import json
import sys

def main():

	if input('Update Bootstrap? This may mess up the application. (y/n) ').lower() in ['y', 'yes']:
		print()
		print('Updating Bootstrap...')
		jsonData = fetchJsonFromUrl('https://api.cdnjs.com/libraries/bootstrap/')
		if jsonData is not None and 'error' not in jsonData:
			splitUrl = jsonData['latest'].split('/')
			otherFiles = ['bootstrap.js', 'bootstrap.js.map', 'bootstrap.min.js', 'bootstrap.min.js.map', 'bootstrap.css', 'bootstrap.css.map', 'bootstrap.min.css', 'bootstrap.min.css.map', 'bootstrap.bundle.js', 'bootstrap.bundle.js.map', 'bootstrap.bundle.min.js', 'bootstrap.bundle.min.js.map']
			for fileName in otherFiles:
				splitUrl[-1] = fileName
				splitUrlBackup = ''
				if fileName.endswith('.css') or fileName.endswith('css.map'):
					if splitUrl[-2] == 'js':
						splitUrlBackup = splitUrl[-2]
						splitUrl[-2] = 'css'
				downloadFile(fileName, '/'.join(splitUrl))	
				# Restore the splitUrl
				if splitUrlBackup != '':
					splitUrl[-2] = splitUrlBackup
		else:
			print('An error occurred while fetching the JSON data.')

	if input('Update JQuery? (y/n) ').lower() in ['y', 'yes']:
		print()
		print('Updating JQuery...')
		jsonData = fetchJsonFromUrl('https://api.cdnjs.com/libraries/jquery/')
		if jsonData is not None and 'error' not in jsonData:
			splitUrl = jsonData['latest'].split('/')
			otherFiles = ['jquery.slim.js', 'jquery.slim.min.js', 'jquery.slim.min.map']
			for fileName in otherFiles:
				splitUrl[-1] = fileName
				downloadFile(fileName, '/'.join(splitUrl))
		else:
			print('An error occurred while fetching the JSON data.')


	if input('Update the VIS Network? This will likely mess up the application since they have API changes frequently. (y/n) ').lower() in ['y', 'yes']:
		print()
		print('Updating VIS Network...')
		jsonData = fetchJsonFromUrl('https://api.cdnjs.com/libraries/vis/')
		if jsonData is not None and 'error' not in jsonData:
			splitUrl = jsonData['latest'].split('/')
			otherFiles = ['vis.js', 'vis.css', 'vis.map', 'vis.js.map', 'vis.min.js', 'vis.min.css', 'vis-network.min.js', 'vis-network.min.css']
			for fileName in otherFiles:
				splitUrl[-1] = fileName
				downloadFile(fileName, '/'.join(splitUrl))
		else:
			print('An error occurred while fetching the JSON data.')


	print()
	print('Updating JSON Editor...')
	jsonData = fetchJsonFromUrl('https://api.cdnjs.com/libraries/jsoneditor/')
	if jsonData is not None and 'error' not in jsonData:
		splitUrl = jsonData['latest'].split('/')
		otherFiles = ['jsoneditor.js', 'jsoneditor.css', 'jsoneditor.map', 'jsoneditor.min.js', 'jsoneditor.min.css']
		for fileName in otherFiles:
			splitUrl[-1] = fileName
			downloadFile(fileName, '/'.join(splitUrl))
	else:
		print('An error occurred while fetching the JSON data.')


	print()
	print('Updating LZ-String...')
	jsonData = fetchJsonFromUrl('https://api.cdnjs.com/libraries/lz-string/')
	if jsonData is not None and 'error' not in jsonData:
		splitUrl = jsonData['latest'].split('/')
		otherFiles = ['lz-string.js', 'lz-string.min.js']
		for fileName in otherFiles:
			splitUrl[-1] = fileName
			downloadFile(fileName, '/'.join(splitUrl))
	else:
		print('An error occurred while fetching the JSON data.')


	if input('Update the Popper.js? Update this alongside Bootstrap to ensure dropdown menus work properly. (y/n) ').lower() in ['y', 'yes']:
		print()
		print('Updating Popper.js...')
		jsonData = fetchJsonFromUrl('https://api.cdnjs.com/libraries/popper.js/')
		if jsonData is not None and 'error' not in jsonData:
			splitUrl = jsonData['latest'].split('/')
			otherFiles = ['popper.min.js', 'popper.min.js.map']
			for fileName in otherFiles:
				splitUrl[-1] = fileName
				downloadFile(fileName, '/'.join(splitUrl))
		else:
			print('An error occurred while fetching the JSON data.')


	print()
	print('Updating NoSleep...')
	jsonData = fetchJsonFromUrl('https://api.cdnjs.com/libraries/nosleep/')
	if jsonData is not None and 'error' not in jsonData:
		splitUrl = jsonData['latest'].split('/')
		otherFiles = ['NoSleep.js', 'NoSleep.min.js']
		for fileName in otherFiles:
			splitUrl[-1] = fileName
			downloadFile(fileName, '/'.join(splitUrl))
	else:
		print('An error occurred while fetching the JSON data.')


	print()
	print('Updating Image-Map-Resizer...')
	jsonData = fetchJsonFromUrl('https://api.cdnjs.com/libraries/image-map-resizer/')
	if jsonData is not None and 'error' not in jsonData:
		splitUrl = jsonData['latest'].split('/')
		otherFiles = ['imageMapResizer.js', 'imageMapResizer.map', 'imageMapResizer.min.js']
		for fileName in otherFiles:
			splitUrl[-1] = fileName
			downloadFile(fileName, '/'.join(splitUrl))
	else:
		print('An error occurred while fetching the JSON data.')

	print()
	print('Files successfully updated.')
	print('Please ensure that the application works with no errors before accepting these updated files.')

# Fetches the JSON data from the specified URL
def fetchJsonFromUrl(url):
	try:
		# Send a GET request to the URL
		response = requests.get(url)
		response.raise_for_status()  # Check if the request was successful
		# Parse the JSON content directly
		json_data = response.json()
		return json_data
	except Exception as e:
		print(f"An error occurred: {str(e)}")
		return None

# Downloads the file from the specified URL and saves it to the specified path
def downloadFile(filePath, url):
	print(f'\tDownloading {url} to {filePath}...')
	try:
		# Send a GET request to the URL
		response = requests.get(url, stream=True)
		response.raise_for_status()  # Check if the request was successful

		# Open the file for binary writing
		with open(filePath, 'wb') as file:
			# Iterate through the response content and write it to the file
			for chunk in response.iter_content(chunk_size=8192):
				file.write(chunk)
	except Exception as e:
		print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
	main()