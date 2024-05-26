import json
import os

def read_file(path):
    try:
        with open(path,"r") as file:
            return file.readlines()
    except:
        print("[-] File is not exist")
        return None

def transform_string(input_string):
    no_spaces = input_string.replace(" ", "_")
    lower_case_string = no_spaces.lower()
    return lower_case_string

def append_to_json_file(dictionary, file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r+') as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError("JSON file does not contain a list at the root level.")
            except json.JSONDecodeError:
                data = []

            data.append(dictionary)
            
            file.seek(0)
            json.dump(data, file, indent=4)
    else:
        with open(file_name, 'w') as file:
            json.dump([dictionary], file, indent=4)
