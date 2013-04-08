'''
    Author: Amogh Tolay
    This is a backup code for understanding
    queries given by the user and mapping them into SQL queries
    This might use NLP in the future, as of now mainly uses regex
    matching for fetching data from the query
'''
import nltk
import re
from nltk.parse import *
from nltk.tokenize import *

def regexMatch ( nlQuery ):
    pattern = re.compile ( r"""(find|search|display|show|list|give)\s
                            (faculty|student|staff|other|or|\s)+ # either or all of these
                            (where|such\sthat|whose)\s # the constraint names
                            (date of birth|dob|birthdate|birthday)\s
                            (is|between|on|such that)+
                            """, re.VERBOSE )
    result = pattern.search ( nlQuery )
    if result:
        print 'Match found at: ', result.group(), result.groups()
    else:
        print 'No match found.'

def cfgMatch ( nlQuery ):
    terminalList = [ 'find','search','display','tell','faculty','student','staff','other' ]
    grammar = nltk.parse_cfg("""
                    S -> A B
                    A -> 'find'|'search'|'display'|'tell'
                    B -> 'faculty'|'student'|'staff'|'other'
                    """)
# Since grammar crashes if a non term not in grammar is used.
# We have to check and report error if such a word is used anywhere
##################################################################
# Check and errors reporting here
    tokenizedList = list( word_tokenize( nlQuery  ) )
    for word in tokenizedList:
        if word not in terminalList:
            print "ERROR"
            return -1
##################################################################
    parser = nltk.RecursiveDescentParser ( grammar )
    parseTree = parser.nbest_parse ( tokenizedList, 1 )

    for tree in parseTree:
        print tree
        for elem in tree:
            for i in tree.node:
                print i
##################################################################
# FUNCTIONS THAT WILL ACTUALLY BE USED IN THE DEPOYED WEBSITE
# For eg. things like searching database with similar entries for
# certain things.....
#################################################################

def main():
    nlQuery = raw_input()
    regexMatch ( nlQuery )
    cfgMatch ( nlQuery )
main()
