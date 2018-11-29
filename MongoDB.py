from pymongo import MongoClient
import json_creater
import json



client = MongoClient('localhost', 27017)

db = client['movieLocationDB']
collection = db['locations_and_funFacts']

problem_records = []

def write_documents_to_db(json_array):
    for document in json_array:
        json_doc = json.dumps(document)
        try:
            collection.insert_one(json_doc)
        except Exception as e:
            problem_records.append(json_doc)
            pass
    print(db.collection.count_documents)



def main():
    json_array_instance = json_creater.JSONToCSV()
    json_array = json_array_instance.create_json()

    print(json_array)
    #write_documents_to_db(json_array)
main()





