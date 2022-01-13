# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")
found = False
# Set path for file
file_name = "../Resources/netflix_ratings.csv"

# Open the CSV
with open(file_name) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvreader)

	for row in csvreader:
		if (row[0] == video) and (found == False):
			print(f'{row[0]} is rated {row[1]} with a rating of {row[5]}')
			found = True

