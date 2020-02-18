from cloudant.client import Cloudant
import cloudant.database

def req_my_data():
    USERNAME = "ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix"
    PASSWORD = "7108e823e027096171ab2aefae53613ad95af2cbd59affb32147980d2546e550"
    cloudant_url = "https://ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix:7108e823e027096171ab2aefae53613ad95af2cbd59affb32147980d2546e550@ba62d85b-fc08-4706-8a9e-ba91bfbf6174-bluemix.cloudant.com"
    my_cl_db_name = 'my_cl_db'

    client = Cloudant(USERNAME, PASSWORD, url=cloudant_url)
    client.connect()  # Connect to the server
    my_cl_db_handler = cloudant.database.CloudantDatabase(client, my_cl_db_name)

    # Assignment Q1: Find all reviews from member A1004AX2J2HXGL.
    selector = {'member_id': {'$eq': 'A1004AX2J2HXGL'}}
    docs_collection = my_cl_db_handler.get_query_result(selector)
    for each_doc in docs_collection:
        print(each_doc)

    # Assignment Q2: Find the number of reviews by each member.
    resp = my_cl_db_handler.get_search_result(ddoc_id='py_ddoc', index_name='py_index', query='*:*', counts=["member_id"])
    print('Number of reviews by each member: ',resp['counts'])

    # Assignment Q3: Find the product ids of all products with at least one review rating less than 3.
    selector = {'rating': {'$lt': 3}}
    fields = ['product id']
    docs_collection = my_cl_db_handler.get_query_result(selector, fields)
    for each_doc in docs_collection:
        print(each_doc)

    client.disconnect()

req_my_data()