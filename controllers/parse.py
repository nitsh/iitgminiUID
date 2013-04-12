###############################################################
# Amogh's code for
# This is the page having only one text box and will get the
# query and proceed appropriately
##############################################################
import json
from types import *
def generateQuery():
    filterNum = (len(request.vars)) /2;
    index = 0;
    queries = []
    queries.append ( dbUid.allResidents.id > 0 )
    while index < filterNum:
        for table in dbUid:
            for field in table:
                if ( index < filterNum ):
                    key = request.vars['where'+str(index)].strip('\r\n')
                    value = request.vars['input'+str(index)].strip('\n\r')
                    if ( key == str ( field ) ):
                        queries.append( field.contains( value ) )
                        index+=1
    queryAnd = reduce ( lambda a,b: ( a&b ), queries )
    rows = dbUid( queryAnd ).select()

def parseAndQueryGenerate():
    rawStringTemp = """
                    [
                        {
                            "atrName": "allResidents.name",
                            "atrVal": "Amogh",
                            "comparisonOp": "contains",
                            "logicalOp": "AND"
                        },
                        {
                            "atrName": "allResidents.uid",
                            "atrVal": "0",
                            "comparisonOp": ">",
                            "logicalOp": "OR"
                        },
                        {
                            "1":
                                {
                                    "atrName": "allResidents.fbLink",
                                    "atrVal": "facebook",
                                    "comparsionOp": "contains",
                                    "logicalOp": "OR"
                                },
                            "2":
                                {
                                    "atrName" : "allResidents.type",
                                    "atrVal": "Student",
                                    "comparisonOp": "==",
                                    "logicalOp": "OR"
                                }
                        }
                    ]
                    """
    rawStringTempSimple = """
                    [
                        [
                            "allResidents.name",
                            "Amogh",
                            "contains",
                            "AND"
                        ],
                        [
                            "allResidents.uid",
                            "0",
                            ">",
                            "OR"
                        ],
                        [
                            "allResidents.fbLink",
                            "amogh",
                            "contains",
                            "X"
                        ]
                    ]
                    """
    rawQuery = json.loads ( rawStringTempSimple )
# Now, got the rawQuery in RAM in the form of dicts of dicts
# now, gnerate the query
    queryList = []
    for listElem in rawQuery:
        if type( listElem[0] ) is ListType:
            print "Is list"
            pass
            # call itself function over here to ensure nesting is taken care of
        else:
            for table in dbUid:
                for field in table:
                    if listElem[0] == str(field):
                        if listElem[2] == "contains":
                            queryList.append( field.contains( listElem[1] ) )
                        if listElem[2] == "==":
                            queryList.append( field == listElem[1] )
                        if listElem[2] == ">":
                            queryList.append( field > listElem[1] )
                        if listElem[2] == "<":
                            queryList.append( field > listElem[1] )
                        if listElem[2] == ">=":
                            queryList.append( field >= listElem[1] )
                        if listElem[2] == "<=":
                            queryList.append( field <= listElem[1] )
                        if listElem[2] == "like":
                            queryList.append( field.like( listElem[1] ) )
                        if listElem[2] == "startswith":
                            queryList.append( field.startswith( listElem[1] ) )
# Now, queryList contains all independent queries
# Now, get the operator precedence and other stuff from rawQuery
            for i in range( len( queryList )-1 ):
                if rawQuery[i][3] == "AND":
                    queryCreate = queryList[i] & queryList[i+1]
                if rawQuery[i][3] == "OR":
                    queryCreate = queryList[i] | queryList[i+1]

    rows = dbUid( queryCreate ).select()
    tempOut = ""
    for row in rows:
        tempOut += str(row.id) + ", "
    print queryList
    return tempOut
