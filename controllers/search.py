# controller for search

def index():
    #field = getFieldList()
    field=['stud','fac','staff']
    userOptions = ['student', 'faculty', 'staff', 'others' ]
    form = SQLFORM.factory(
            Field( 'userOptions',widget=SQLFORM.widgets.checkboxes.widget, requires=[IS_IN_SET(userOptions, multiple=True), IS_NOT_EMPTY()] ), keepvalues=True)
    if form.process().accepted:
        redirect( URL( requestQuery, args=[form.vars['userOptions'][0] ] ) )
    #return dict( message = T( "Welcome to search" ) )
    return dict( message = field[0] , form=form)


# function to return a dictionary of all fields which are allowed
# to be accessed by the user
# Parameters taken in order: stud, fac, staff, other
@auth.requires_login()
def getFieldList( ):
#################################################################
# COMMENT THIS WHEN YOU DEPLOY THE APPLICATION
################################################################
    stud = 1
    fac = 1
    staff = 1
    other = 1
###############################################################
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
#############################################################################
# REMOVE THIS WHILE DEPLOYING
# THEN RETURN LIST AS IT IS
############################################################################
    for i in fieldNameList:
        tempOut = tempOut + i
############################################################################
    return dict ( message = T("DEBUGGING OUTPUT = " + tempOut ) )

def requestQuery():
    request.vars._formname = 'queryform'
    fields=['student.name', 'student.rollno', 'faculty.room', 'student.webmail']
    #form = SQLFORM.factory(
    #Field('where', 'string', notnull=True,requires=IS_IN_SET(fields)) )
    #if form.accepts(request.vars, formname='myform'):
    #return 'success'
    return dict(fields=fields)

def generateQuery():
    #name="saurav";
    #name = request.vars['where0'];
    #response.flash = T( str(name) );
    return dict()
