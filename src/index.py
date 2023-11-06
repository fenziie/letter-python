import xmltodict

with open('letter.xml') as fd:
    doc = xmltodict.parse(fd.read())

from_name = doc['root']['from']
to_name = doc['root']['to']
message = doc['root']['message']

print(f"Dear {to_name},\n    {message}\nFrom {from_name}.")
