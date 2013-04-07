# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

import random

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    #response.flash = T("Welcome to our portal!")
    return dict(message=T('IITG Mini UID Project'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    if request.args(0)=='profile':
        redirect(URL(profile))
    return dict(form=auth())

"""
crud is defined in 'db.py' and crud2 is defined in 'iitgUid.py'
"""
@auth.requires_login()
def profile():
    form=SQLFORM(db.auth_user,auth.user.id, fields=['first_name','last_name'])
    resident=dbUid.allResidents
    uid=resident.uid
    q = uid==auth.user.username
    s = dbUid(q)
    rows = s.select()
    for row in rows:
        residentId = row.id
        residentType = row.type
        residentType = "Student"
        response.flash = T("Hello "+row.name)
    form.append(SQLFORM(dbUid.allResidents,residentId,deletable=False))
    if( residentType == "Student" ):
        resident=dbUid.student
        uid=resident.uid
        q = uid==auth.user.username
        s = dbUid(q)
        rows = s.select()
        for row in rows:
            studentId = row.id
        form.append(SQLFORM(dbUid.student,studentId,deletable=False))
    if( residentType == "Faculty" ):
        resident=dbUid.faculty
        uid=resident.uid
        q = uid==auth.user.username
        s = dbUid(q)
        rows = s.select()
        for row in rows:
            facultyId = row.id
        form2.append(crud2.update(dbUid.faculty,facultyId,deletable=False))
    if( residentType == "Staff" ):
        resident=dbUid.staff
        uid=resident.uid
        q = uid==auth.user.username
        s = dbUid(q)
        rows = s.select()
        for row in rows:
            staffId = row.id
        form2.append(crud2.update(dbUid.staff,staffId,deletable=False))
    if( residentType == "Other" ):
        resident=dbUid.relationship
        uid=resident.uid
        q = uid==auth.user.username
        s = dbUid(q)
        rows = s.select()
        for row in rows:
            relationshipId = row.id
        form2.append(crud2.update(dbUid.relationship,relationshipId,deletable=False))
    return dict(form=form)

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

#modified codes below

def register():
    return dict()

# generate uid after all the field has been filled
# modify this function to support your format of the UIDs
def generateUid(form):
    form.vars.uid='123456789'

def type():
    return dict()

def next():
    return dict()

def typeError():
    return dict(message=T("Invalid Type selected"))

# dbUid.allResidents,dbUid.student,
def register_student():
    form2=SQLFORM.factory(dbUid.allResidents,dbUid.student, db.auth_user, keepvalues=True,
    fields=['first_name','last_name', 'password', 'gender','emergencyPh','dob','fbLink','personalPh',
    'interestedIn','bloodGroup','photo','webmailId','hostel','roomNo','rollNo'])
    form2.vars['type']='student'
    if form2.process().accepted:

        # filling up so called redundant field
        form2.vars['uid'] = getNewUID()
        form2.vars['username']=form2.vars['uid']
        form2.vars['registration_key']='pending'
        form2.vars['email']=form2.vars['webmailId']
        form2.vars['name']=str(form2.vars['first_name'])+' '+str(form2.vars['last_name'])

        id = dbUid.allResidents.insert(**dbUid.allResidents._filter_fields(form2.vars))
        form2.vars.allResidents=id
        id = dbUid.student.insert(**dbUid.student._filter_fields(form2.vars))
        form2.vars.student=id
        id = db.auth_user.insert(**db.auth_user._filter_fields(form2.vars))
        response.flash='Thanks for filling the form2'
        redirect(URL('next'))
    elif form2.errors:
        response.flash = 'form2 has errors'
    else:
        response.flash = 'please fill the form for student'
    return dict(form2=form2)

def register_faculty():
    form2=SQLFORM.factory(dbUid.allResidents,dbUid.faculty, db.auth_user, keepvalues=True,
	fields=['first_name','last_name', 'password','gender','emergencyPh','dob','fbLink','personalPh',
	'interestedIn','bloodGroup','photo','webmailId','dept','post','homepageLink','officePh','blockNo','houseNo'])
    form2.vars['type']='faculty'	#need to make this field readonly
    #if form2.process(onvalidation=generateUid).accepted:
    if form2.process().accepted:

        # filling up so called redundant field
        form2.vars['uid'] = getNewUID()
        form2.vars['username']=form2.vars['uid']
        form2.vars['registration_key']='pending'
        form2.vars['email']=form2.vars['webmailId']
        form2.vars['name']=str(form2.vars['first_name'])+' '+str(form2.vars['last_name'])

        id = dbUid.allResidents.insert(**dbUid.allResidents._filter_fields(form2.vars))
        form2.vars.allResidents=id
        id = dbUid.faculty.insert(**dbUid.faculty._filter_fields(form2.vars))
        form2.vars.student=id
        id = db.auth_user.insert(**db.auth_user._filter_fields(form2.vars))
        response.flash='Thanks for filling the form for faculty'
        redirect(URL('next'))
    elif form2.errors:
        response.flash = 'form for faculty has errors'
    else:
        response.flash = 'please fill the form for faculty'
    return dict(form2=form2)

def register_staff():
    form2=SQLFORM.factory(dbUid.allResidents,dbUid.staff, db.auth_user, keepvalues=True,
	fields=['first_name','last_name', 'password','gender','emergencyPh','dob','fbLink','personalPh',
	'interestedIn','bloodGroup','photo','webmailId','address','post','section'])
    form2.vars['type']='staff'	#need to make this field readonly
    #if form2.process(onvalidation=generateUid).accepted:
    if form2.process().accepted:

        # filling up so called redundant field
        form2.vars['uid']=getNewUID()
        form2.vars['username']=form2.vars['uid']
        form2.vars['registration_key']='pending'
        form2.vars['email']=form2.vars['webmailId']
        form2.vars['name']=str(form2.vars['first_name'])+' '+str(form2.vars['last_name'])

        id = dbUid.allResidents.insert(**dbUid.allResidents._filter_fields(form2.vars))
        form2.vars.allResidents=id
        id = dbUid.staff.insert(**dbUid.staff._filter_fields(form2.vars))
        form2.vars.student=id
        id = db.auth_user.insert(**db.auth_user._filter_fields(form2.vars))
        response.flash='Thanks for filling the form for staff'
        redirect(URL('next'))
    elif form2.errors:
        response.flash = 'form for staff has errors'
    else:
        response.flash = 'please fill the form for staff'
    return dict(form2=form2)

def register_other():
    form2=SQLFORM.factory(dbUid.allResidents,dbUid.relationship, db.auth_user, keepvalues=True,
	fields=['first_name','last_name', 'password','gender','emergencyPh','dob','fbLink','personalPh','interestedIn',
	'bloodGroup','photo','relatedtoUid','relname','relnameInverse'])
    form2.vars['type']='other'	#need to make this field readonly
    #if form2.process(onvalidation=generateUid).accepted:
    if form2.process().accepted:

        # filling up so called redundant field
        form2.vars['uid']=getNewUID()
        form2.vars['username']=form2.vars['uid']
        form2.vars['registration_key']='pending'
        form2.vars['email']='admin@gmail.com'
        form2.vars['name']=str(form2.vars['first_name'])+' '+str(form2.vars['last_name'])

        id = dbUid.allResidents.insert(**dbUid.allResidents._filter_fields(form2.vars))
        form2.vars.relationship=id
        id = dbUid.relationship.insert(**dbUid.relationship._filter_fields(form2.vars))
        form2.vars.student=id
        id = db.auth_user.insert(**db.auth_user._filter_fields(form2.vars))
        response.flash='Thanks for filling the form for others'
        redirect(URL('next'))
    elif form2.errors:
        response.flash = 'form for others has errors'
    else:
        response.flash = 'please fill the form for others'
    return dict(form2=form2)


# Amogh's code add to generate a random UID which is not present in the DB
def getNewUID():
    allUid = []
    for row in db().select(db.auth_user.username):
        allUid.append ( row.username )

    random.seed()
    newUid = random.randint ( 1, 89999 ) + 10000
    for newUid in allUid:
        newUid = random.randint ( 1, 89999 ) + 10000
    return str( newUid )
