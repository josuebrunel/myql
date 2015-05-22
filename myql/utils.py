import json
from xml.dom import minidom
from xml.etree import cElementTree as tree

def pretty_json(data):
    data = json.loads(data.decode('utf-8'))
    return json.dumps(data, indent=4, sort_keys=True)

def pretty_xml(data):
    parsed_string = minidom.parseString(data.decode('utf-8'))
    return parsed_string.toprettyxml(indent='\t', encoding='utf-8')

def prettyfy(response, format='json'):

    if format=='json':
        return pretty_json(response.content)
    else :
        return pretty_xml(response.content)

def json_write_data(json_data, filename):
    with open(filename, 'w') as fp:
        json.dump(json_data, fp, indent=4, sort_keys=True, ensure_ascii=False)
        return True
    return False

def json_get_data(filename):
    with open(filename, 'r') as fp:
        json_data = json.load(fp)
    return json_data
 
