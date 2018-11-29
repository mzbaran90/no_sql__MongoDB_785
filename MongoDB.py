from pymongo import MongoClient
import csv
import json





client = MongoClient('localhost', 27017)

db = client['movieLocationsDB']
collection = db.locations_funFacts

problem_records = []


def create_json():
    fieldnames = ['title', 'release_year', 'locations', 'fun_facts', 'production_company', 'distributor',
                  'director',
                  'writer', 'actor 1', 'actor 2', 'actor 3']
    with open('/Users/MasonBaran/Desktop/nosql_db_785.csv', 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, fieldnames)

        locations_list = []
        fun_facts = []
        all_records = []
        complete_records = []
        temp_title = '180'
        for index, row in enumerate(reader):
            if temp_title == row['title']:
                locations_list.append(row['locations'])
                fun_facts.append(row['fun_facts'])
            elif temp_title != row['title']:
                if index > 1:
                    last_record = all_records[index - 1]
                    document = json.dumps(last_record)
                    write_documents_to_db(last_record)
                    complete_records.append(document)

                    # print(all_records[index-1])

                fun_facts.clear()
                fun_facts.append(row['fun_facts'])
                locations_list.clear()
                locations_list.append(row['locations'])

            document = {"title": row['title'], "release_year": row['release_year'],
                        "productions_company": row['production_company'], "distributor": row['distributor'],
                        "distributor": row['distributor'], "participants": [{"actor 1": row['actor 1']},
                                                                            {"actor 2": row['actor 2']},
                                                                            {"actor 3": row['actor 3']},
                                                                            {"director": row['director']}],
                        "locations": locations_list, "fun_facts": fun_facts}
            all_records.append(document)
            temp_title = row['title']

    return complete_records




def write_documents_to_db(last_record):
    print(last_record)

    try:

        result = collection.insert_one(last_record).inserted_id
        print(result)
    except Exception as e:
        problem_records.append(last_record)
        print('something went wrong')
        pass



def write_to_json(json_array):
    with open('/Users/MasonBaran/Desktop/location_and_funFacts.json', 'w', encoding='utf-8') as outfile:
        for array in json_array:

            outfile.write("%s,\n" %array)



def main():
    json_array = create_json()
    write_to_json(json_array)

    
main()





