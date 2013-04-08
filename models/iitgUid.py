dbUid = DAL('mysql://root:@localhost/iitgUidW2P', migrate=False)

dbUid.define_table('allResidents', 
    Field('id', 'id'),                         # (`id` int(11) NOT NULL AUTO_INCREMENT,)
    Field('uid', 'integer', notnull=True),                   # randomINT  (`uid` int(15) NOT NULL COMMENT 'randomINT',)
    Field('name', 'string', notnull=True),                   # (`name` varchar(255) NOT NULL,)
    Field('gender', 'string', notnull=True,requires=IS_IN_SET(['Male','Female']), default=''),                 # (`gender` enum('male','female') NOT NULL,)
    Field('type', 'string', notnull=True,requires=IS_IN_SET(['Student','Faculty','Staff','Other'])),                   # (`type` enum('stud','fac','staff','other') NOT NULL,)
    Field('emergencyPh', 'string', notnull=True),            # (`emergencyPh` varchar(15) NOT NULL,)
    Field('photo', 'upload', notnull=True, autodelete=True, uploadfolder='uploads'),                    # 1 mb max size  (`photo` longblob NOT NULL COMMENT '1 mb max size',)
    Field('dob', 'date', notnull=True),                      # (`dob` date NOT NULL,)
    Field('fbLink', 'string', notnull=False),                 # (`fbLink` varchar(255) DEFAULT NULL,)
    Field('personalPh', 'string', notnull=False),             # (`personalPh` varchar(15) DEFAULT NULL,)
    Field('privilegeNum', 'string', notnull=True),             # (`privilegeNum` binary(60) NOT NULL,)
    Field('interestedIn', 'text', notnull=True),             # (`interestedIn` text NOT NULL,)
    Field('bloodGroup', 'string', requires = IS_IN_SET(['AB+','AB-','O-','O+','A+','A-','B+','B-']), default=''),             # (`bloodGroup` enum('AB+','AB-','O-','O+','A+','A-','B+','B-','other') NOT NULL,)
    )

dbUid.define_table('faculty', 
    Field('id', 'id'),                         # (`id` int(11) NOT NULL AUTO_INCREMENT,)
    Field('uid', 'integer', notnull=True),                   # (`uid` int(15) NOT NULL,)
    Field('webmailId', 'string', notnull=True),              # (`webmailId` varchar(100) NOT NULL,)
    Field('dept', 'string', notnull=True),                   # (`dept` varchar(100) NOT NULL,)
    Field('post', 'string', notnull=True),                   # (`post` enum('assistant prof','associate prof','prof') NOT NULL,)
    Field('homepageLink', 'string'),           # (`homepageLink` varchar(100) DEFAULT NULL,)
    Field('officePh', 'integer', notnull=True),              # (`officePh` int(10) NOT NULL,)
    Field('blockNo', 'string', notnull=True),                # (`blockNo` varchar(10) NOT NULL,)
    Field('houseNo', 'string', notnull=True),                # (`houseNo` varchar(10) NOT NULL,)
    )

dbUid.define_table('loginDetails', 
    Field('id', 'id'),                         # (`id` int(11) NOT NULL AUTO_INCREMENT,)
    Field('uid', 'integer', notnull=True),                   # (`uid` int(15) NOT NULL,)
    Field('password', 'string', notnull=True),               # (`password` varchar(255) NOT NULL,)
    )

dbUid.define_table('post', 
    Field('id', 'id'),                         # for mapping table of privileges  (`id` int(6) NOT NULL AUTO_INCREMENT COMMENT 'for mapping table of privileges',)
    Field('postName', 'string', notnull=True),               # (`postName` varchar(100) NOT NULL,)
    Field('webmailID', 'string'),              # (`webmailID` varchar(100) DEFAULT NULL,)
    Field('holderUid', 'integer', notnull=True),             # (`holderUid` int(15) DEFAULT NULL,)
    Field('postPrivilege', 'blob', notnull=True),            # (`postPrivilege` binary(60) NOT NULL,)
    Field('section', 'string', notnull=True),                # (`section` varchar(100) NOT NULL,)
    )

dbUid.define_table('relationship', 
    Field('id', 'id'),                         # (`id` int(11) NOT NULL AUTO_INCREMENT,)
    Field('uid', 'integer', notnull=True),                   # (`uid` int(15) NOT NULL,)
    Field('relatedtoUid', 'integer', notnull=True),          # (`relatedtoUid` int(15) NOT NULL,)
    Field('relname', 'string', notnull=True),                # (`relname` varchar(100) NOT NULL,)
    Field('relnameInverse', 'string', notnull=True),         # (`relnameInverse` varchar(100) NOT NULL,)
    )

dbUid.define_table('staff', 
    Field('id', 'id'),                         # (`id` int(11) NOT NULL AUTO_INCREMENT,)
    Field('uid', 'integer', notnull=True),                   # (`uid` int(15) NOT NULL,)
    Field('webmailId', 'string', notnull=True),              # (`webmailId` varchar(100) NOT NULL,)
    Field('address', 'string', notnull=True),                # (`address` varchar(1000) NOT NULL,)
    Field('post', 'string', notnull=True),                   # (`post` varchar(100) NOT NULL,)
    Field('section', 'string', notnull=True),                # (`section` varchar(100) NOT NULL,)
    )

dbUid.define_table('student', 
    Field('id', 'id'),                         # (`id` int(11) NOT NULL AUTO_INCREMENT,)
    Field('uid', 'integer', notnull=True),                   # (`uid` int(15) NOT NULL,)
    Field('webmailId', 'string', notnull=True),              # (`webmailId` varchar(100) NOT NULL,)
    Field('hostel', 'string', notnull=True),                 # (`hostel` varchar(32) NOT NULL,)
    Field('roomNo', 'string', notnull=True),                 # (`roomNo` varchar(10) NOT NULL,)
    Field('rollNo', 'string', notnull=True),                 # (`rollNo` varchar(14) NOT NULL,)
    )

dbUid.define_table('vehicle', 
    Field('id', 'id'),                         # (`id` int(11) NOT NULL AUTO_INCREMENT,)
    Field('regNo', 'string', notnull=True),                  # (`regNo` varchar(15) NOT NULL,)
    Field('type', 'string', notnull=True),                   # (`type` varchar(100) NOT NULL,)
    Field('owneruid', 'integer', notnull=True),              # (`owneruid` int(15) NOT NULL,)
    Field('instiRegNo', 'string', notnull=True),             # (`instiRegNo` varchar(15) NOT NULL,)
    )

# Changed by Amogh
'''
Database of localhost (phpMyAdmin) also changed.
Entries like privilegeNum is now a char of 60
Also, some other columns might have been changed, so keep a lookout for them
'''
dbUid.define_table('privilegeTable',
    Field('id', 'id'),
    Field('tableName', 'string', notnull=True),
    Field('field', 'string', notnull=True),
    )

crud2=Crud(dbUid)
crud2.messages.submit_button = 'Save changes'
crud2.messages.record_updated = 'Record updated'


dbUid.allResidents.uid.requires = IS_NOT_IN_DB(dbUid, dbUid.allResidents.uid)
dbUid.student.webmailId.requires = IS_NOT_IN_DB(dbUid, dbUid.student.webmailId)
dbUid.faculty.webmailId.requires = IS_NOT_IN_DB(dbUid, dbUid.faculty.webmailId)
dbUid.staff.webmailId.requires = IS_NOT_IN_DB(dbUid, dbUid.staff.webmailId)
dbUid.student.rollNo.requires = IS_NOT_IN_DB(dbUid, dbUid.student.rollNo)
dbUid.student.webmailId.requires = [IS_EMAIL(error_message=auth.messages.invalid_email),IS_NOT_IN_DB(db, 'auth_user.email')]
