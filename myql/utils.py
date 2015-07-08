import json
from xml.dom import minidom


def pretty_json(data):
    """Return a pretty formatted json
    """
    data = json.loads(data.decode('utf-8'))
    return json.dumps(data, indent=4, sort_keys=True)


def pretty_xml(data):
    """Return a pretty formated xml
    """
    parsed_string = minidom.parseString(data.decode('utf-8'))
    return parsed_string.toprettyxml(indent='\t', encoding='utf-8')


def prettyfy(response, format='json'):
    """A wrapper for pretty_json and pretty_xml
    """
    if format == 'json':
        return pretty_json(response.content)
    else:
        return pretty_xml(response.content)

