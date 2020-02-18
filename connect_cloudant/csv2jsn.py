__author__ = 'ASR'

import csv

csvfile = open('file1.csv', 'r')

fieldnames = ("member id", "product id", "date", "number of helpful feedbacks", "number of feedbacks", "rating", "title", "body")
reader = csv.DictReader(csvfile, fieldnames, delimiter='\t')  # Create a dictionary object using the field names

for row in reader:  # Take each row from dictionary and convert as needed and prepare another dictionary object
    data = {'member id': row['member id'], 'product id': row['product id'], 'date': row['date'],
            'number of helpful feedbacks': int(row['number of helpful feedbacks']),
            'number of feedbacks': int(row['number of feedbacks']), 'rating': round(float(row['rating']), 1), 'title': row['title'],
            'body': row['body']}

    # Send data to database..
