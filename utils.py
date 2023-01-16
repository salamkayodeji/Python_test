import json
import pprint

#function that gets all the keys and values in the dictionary
def get_v_k(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from get_v_k(value)
        elif type(value) is list:
            yield (key, value)
            for i in value:
                if type(i) is dict:
                    yield from get_v_k(i)
        else:
            yield (key, value)
           
#function that checks all the values data types  
def check_type(value):
        if value == True or value == False : return None
        if isinstance(value, str) : return "string" 
        if isinstance(value, int) : return "integer" 
        if all(isinstance(x, str) for x in value) and value != [] and not isinstance(value, dict) : return "enum" 
        if isinstance(value, dict) : return "array" 


def create_json(file_name, output_name):
    output = {}
    with open(f'data/{file_name}.json', 'r') as f:
        data = json.load(f)
    message = data.get("message", {})
    for i in get_v_k(message):
        value_type = check_type(i[1])
        output[i[0]] = {"type": value_type,
                    "tag": "",
                    "description": "",
                    "required": False
                                    }
    with open(f'schema/{output_name}.json', 'w') as json_file:
        json.dump(output, json_file, indent = 4)

