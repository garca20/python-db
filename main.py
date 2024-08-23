import json
from appendLine import getHeaders

information = json.load(open('info.json'))

fileName = information["fileName"]
lines = information["lines"]
lists = information["lists"]

print(getHeaders(lists))