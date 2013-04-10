# controller for search

def index():
    userOptions = ['student', 'faculty', 'staff', 'others' ]
    form = SQLFORM.factory(
            Field( 'userOptions',widget=SQLFORM.widgets.checkboxes.widget, requires=[IS_IN_SET(userOptions, multiple=True), IS_NOT_EMPTY()] ), keepvalues=True)
    if form.process().accepted:
        redirect( URL( requestQuery, args=form.vars['userOptions'] ) )
    #return dict( message = T( "Welcome to search" ) )
    return dict(message =T("Select database") , form=form)


# function to return a dictionary of all fields which are allowed
# to be accessed by the user
# Parameters taken in order: stud, fac, staff, other
@auth.requires_login()
def getFieldList( stud, fac, staff, other ):
    query = dbUid.allResidents.uid == auth.user.username
    rows = dbUid ( query ).select()
    userPrivilegeNum = 0
    for row in rows:
        userPrivilegeNum = row.privilegeNum
    #response.flash = T("UID of logged in user is" + str(userPrivilegeNum) )
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
            if ( stud and ( row.tableName == 'student' or row.tableName == 'allResidents' or row.tableName == 'post' or row.tableName == 'relationship' or row.tableName == 'vehicle') ):
                tempNameConstruct = row.tableName + "." + row.field + "\n"
                fieldNameList.append ( tempNameConstruct )
            if ( staff and ( row.tableName == staff or row.tableName == 'allResidents' or row.tableName == 'post' or row.tableName == 'relationship' or row.tableName == 'vehicle') ):
                tempNameConstruct = row.tableName + "." + row.field + "\n"
                fieldNameList.append ( tempNameConstruct )
            if ( fac and ( row.tableName == 'faculty' or row.tableName == 'allResidents' or row.tableName == 'post' or row.tableName == 'relationship' or row.tableName == 'vehicle') ):
                tempNameConstruct = row.tableName + "." + row.field + "\n"
                fieldNameList.append ( tempNameConstruct )
            if ( other and ( row.tableName == 'allResidents' or row.tableName == 'post' or row.tableName == 'relationship' or row.tableName == 'vehicle') ):
                tempNameConstruct = row.tableName + "." + row.field + "\n"
                fieldNameList.append ( tempNameConstruct )
    fieldNameList = list( set( fieldNameList ) )
    return fieldNameList

def requestQuery():
    tableSelect = { 'student':0, 'faculty':0, 'staff':0, 'others':0 }
    for index in  request.args :
        tableSelect[ index ] = 1;
    response.flash = str( tableSelect['others'] );
    fields = getFieldList( tableSelect['student'], tableSelect['faculty'], tableSelect['staff'], tableSelect['others'])
    return dict(fields=fields)

#################################################################
# Amogh's code for query generation
################################################################
# Add argument to the function call
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

    query = reduce ( lambda a,b: (a&b), queries )
    rows = dbUid( query ).select()
    tempOut = ''
    for row in rows:
        tempOut += str(row.id) + " , "
    return tempOut


