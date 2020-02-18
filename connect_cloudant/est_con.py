__author__ = 'ASR'

from cloudant.client import Cloudant
import cloudant.database
import csv
import time


def main():
    USERNAME = "ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix"
    PASSWORD = "7108e823e027096171ab2aefae53613ad95af2cbd59affb32147980d2546e550"
    cloudant_url = "https://ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix:7108e823e027096171ab2aefae53613ad95af2cbd59affb32147980d2546e550@ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix.cloudant.com"

    my_database_name_in_cloudant = 'abc'

    #client = Cloudant(USERNAME, PASSWORD, account=ACCOUNT_NAME)
    client = Cloudant(USERNAME, PASSWORD, url=cloudant_url)
    # or using url
    # client = Cloudant(USERNAME, PASSWORD, url='https://acct.cloudant.com')

    # Connect to the server
    client.connect()

    # Perform client tasks...
    session = client.session()
    print('Username: {0}'.format(session['userCtx']['name']))
    print('Databases: {0}'.format(client.all_dbs()))


    # Connection Established....Open My Database Now
    my_database = client[my_database_name_in_cloudant]
    # my_document = my_database['0ee5818002b8302e815f619a1521679f']
    # print(my_document)

    '''
    # Send Data document in Database by reading the input CSV file using my_database object
    csvfile = open('file1.csv', 'r')

    fieldnames = ("member_id", "product id", "date", "number of helpful feedbacks", "number of feedbacks", "rating", "title", "body")
    reader = csv.DictReader(csvfile, fieldnames, delimiter='\t')  # Create a dictionary object using the field names

    for row in reader:  # Take each row from dictionary and convert as needed and prepare another dictionary object
        my_data_doc = {'member_id': row['member_id'], 'product id': row['product id'], 'date': row['date'],
                'number of helpful feedbacks': int(row['number of helpful feedbacks']),
                'number of feedbacks': int(row['number of feedbacks']), 'rating': round(float(row['rating']), 1),'title': row['title'],
                'body': row['body']}
        time.sleep(0.7) #  Otherwise server raises Too many requests..10 per second can accept
        my_database.create_document(my_data_doc)  # Send the data to database


    #Use Get Method
    # Define the end point and parameters
    retrieve_target = '_all_docs'
    end_point = '{0}/{1}/{2}'.format(cloudant_url, my_database_name_in_cloudant, retrieve_target)
    #print(end_point)
    params = {'include_docs': 'true'}

    # Issue the request
    #response = client.r_session.get(end_point, params=params)

    # Display the response content
    #print(response.json())
'''

    # Create Index
    database_handler = cloudant.database.CloudantDatabase(client, my_database_name_in_cloudant)
    # index_response = database_handler.create_query_index(design_document_id='py_ddoc', index_name='py_index', index_type='json', fields=['member id'])
    # print(index_response)
    # print(database_handler.get_query_indexes(raw_result=True))
    # Disconnect from the server

    '''
    # Start Query :: Select Query # Assignment Query: 1
    selector = {'member_id': {'$eq': 'A1004AX2J2HXGL'}}
    docs_collection = database_handler.get_query_result(selector)
    # for each_doc in docs_collection:
    #    print(each_doc)

    # JSON output
    docs_collection = database_handler.get_query_result(selector, raw_result=True)
    # for each_doc in docs_collection['docs']:
    #   print(each_doc)


    # Start Query :: Select Query # Assignment Query: 3
    selector = {'rating': {'$lt': 3}}
    fields = ['product id']
    docs_collection = database_handler.get_query_result(selector, fields)
    for each_doc in docs_collection:
        print(each_doc)
'''

    # Search and Group Query:: Assignment Query 2/3
    # resp = database_handler.get_search_result(ddoc_id='py_ddoc', index_name='py_index', query='member_id:A*', group_field='member_id', counts=["member_id"])
    resp = database_handler.get_search_result(ddoc_id='py_ddoc', index_name='py_index', query='*:*', counts=["member_id"])
    print(resp['counts'])



    client.disconnect()


main()
