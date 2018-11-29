import os
import json
import csv


os.chdir('/Users/MasonBaran/Desktop')

class JSONToCSV():

    def __init__(self):
        self.file = 'nosql_db_785.csv'

    def create_json(self):

        fieldnames = ['title', 'release_year', 'locations', 'fun_facts', 'production_company', 'distributor',
                      'director',
                      'writer', 'actor 1', 'actor 2', 'actor 3']
        with open(self.file, 'r', encoding='utf-8') as infile:
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
                        last_record = all_records[index-1]
                        document = json.dumps(last_record)
                        complete_records.append(document)



                        #print(all_records[index-1])

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

