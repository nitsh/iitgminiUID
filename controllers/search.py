# controller for search

def index():
	return dict( message = T( "Welcome to search" ) )


# function to return a dictionary of all fields which are allowed
# to be accessed by the user
@auth.requires_login()
def getFieldList():
    query = dbUid.allResidents.uid == auth.user.username
    rows = dbUid ( query ).select()
    userPrivilegeNum = 0
    for row in rows:
        userPrivilegeNum = row.privilegeNum
    response.flash = T("UID of logged in user is" + str(userPrivilegeNum) )
# Now, the variable userPrivilegeNum contains the string corresponding to the
# logged in user's privilege number.
# now, for each number 1, get the name of table and field name from the table
    index = 0
    bitSetField = []
    while index < len ( userPrivilegeNum ):
        index = userPrivilegeNum.find( '1', index )
        if index == -1:
            break
        bitSetField.append( index + 1 ) # appending index + 1 because index starts from 0 but table ID starts from 1
        index += 1   # +1 because len('1') == 1
    tempOut = ""
    fieldNameList = []
    for elem in bitSetField:
        queryGetField = dbUid.privilegeTable.id == elem
        rows = dbUid ( queryGetField ).select()
        for row in rows:
            tempNameConstruct = row.tableName + "." + row.field + "\n"
            fieldNameList.append ( tempNameConstruct )
    for i in fieldNameList:
        tempOut = tempOut + i
    return dict ( message = T("DEBUGGING OUTPUT = " + tempOut ) )
