__author__ = 'ASR'

from cloudant.client import Cloudant
import csv
import time


def main():
    USERNAME = "ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix"
    PASSWORD = "7108e823e027096171ab2aefae53613ad95af2cbd59affb32147980d2546e550"
    cloudant_url = "https://ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix:7108e823e027096171ab2aefae53613ad95af2cbd59affb32147980d2546e550@ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix.cloudant.com"
    my_cl_db_name = 'my_cl_db'
    count_doc = 0

    client = Cloudant(USERNAME, PASSWORD, url=cloudant_url)
    client.connect()  # Connect to the server
    my_cl_db = client.create_database(my_cl_db_name)  # Create db

    if my_cl_db.exists():
        print("Database Created.")
    else:
        print("Error# 1: Databse Creation Failed.")
        exit(True)

    # Read Data and Send to Database
    data_file = open('Data.txt', 'r')

    fieldnames = ("member_id", "product id", "date", "number of helpful feedbacks", "number of feedbacks", "rating", "title", "body")
    reader = csv.DictReader(data_file, fieldnames, delimiter='\t')  # Create a dictionary object using the field names

    for row in reader:  # Take each row from dictionary and convert as needed and prepare another dictionary object
        my_data_doc = {'member_id': row['member_id'], 'product id': row['product id'], 'date': row['date'],
                'number of helpful feedbacks': int(row['number of helpful feedbacks']),
                'number of feedbacks': int(row['number of feedbacks']), 'rating': round(float(row['rating']), 1),'title': row['title'],
                'body': row['body']}
        my_cl_db.create_document(my_data_doc)  # Send the data to database
        count_doc += 1
        print("Total Document sent: ", count_doc)
        time.sleep(0.5) #  Otherwise server raises Too many requests error

    print("Data Store Complete.")
    client.disconnect()

main()