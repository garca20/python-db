def getHeaders(data):
    headerArray = []

    for header in data:
        headerArray.append(header["name"])

    headerLine = arrayToLine(headerArray)
    return headerLine

def createLine(lists):
    valuesArray = []
    for list in lists:
        valuesArray.append(  (returnValue(list))   )



def returnValue(list):
    return 

def checkListType(listType):





def arrayToLine(element):
    return str(element).replace(", ", ";").replace("[", "").replace("]", "").replace("'", "")