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

