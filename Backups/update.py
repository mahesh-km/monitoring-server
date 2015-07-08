#!/usr/bin/python
#
import sys
import json
import urllib2
import os
from subprocess import Popen
import gdata.docs.service
import gdata.spreadsheet.service
import gdata.spreadsheets.data
#----read json from url
#url = Popen(['curl', 'http://59.90.236.95:8080/status/hosts/list'])
#url = "http://59.90.236.95:8080/status/hosts/list"
#data = urllib2.urlopen(url).read()
#data = json.loads(data)
#
#------ read from file
json_file = open('Formatted-mmonit.json')
data = json.load(json_file)
json_file.close()
# print data
#
#---Both dict store led  and status information separately;
dict1 = {}
dict2 = {}
s = {}
for record in data['records']:
    store = record['hostname']
    dict1[store] = record['led']
    dict2[store] = record['status']

#print dict1
#print dict2
#--email and pwd ,currently am using my id;   
email = 'mahesh@vyoma-media.in'
password = 'yokoma2012'
spreadsheet_key = '0Ap1cvRKx4murdG5uQkFuR2lpNC1lN3BCeU8xT1F5UGc'
worksheet_id = 'od6'
#
#---here declare all station name ,this for testing,
#   and will be change;
P1 = unicode(dict1['KaCity0Plasma'])
C1 = unicode(dict1['KaCity0UtsF0001'])
C2 = unicode(dict1['KaCity0UtsF0002'])
C3 = unicode(dict1['KaCity0UtsF0003'])
C4 = unicode(dict1['KaCity0UtsF0004'])
C5 = unicode(dict1['KaCity0UtsF0005'])
C6 = unicode(dict1['KaCity0UtsF0006'])
C7 = unicode(dict1['KaCity0UtsF0007'])
C8 = unicode(dict1['KaCity0UtsF0008'])
C9 = unicode(dict1['KaCity0UtsF0009'])
C10 = unicode(dict1['KaCity0UtsF0010'])
C11 = unicode(dict1['KaCity0UtsF0011'])
C12 = unicode(dict1['KaCity0UtsF0012'])
C13 = unicode(dict1['KaCity0UtsF0013'])
#
spr_client = gdata.spreadsheet.service.SpreadsheetsService()
spr_client.email = email
spr_client.password = password
spr_client.source = 'dev'
spr_client.ProgrammaticLogin()
#---all the data that send to change the cells,(this for testing),this will 
#   be change;
#---updating each cells.
spr_client.UpdateCell('7', '5', P1,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '6', C1,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '7', C2,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '8', C3,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '9', C4,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '10', C5,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '11', C6,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '12', C7,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '13', C8,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '14', C9,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '15', C10,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '16', C11,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '17', C12,spreadsheet_key, worksheet_id)
spr_client.UpdateCell('7', '18', C13,spreadsheet_key, worksheet_id)
#spr_client.UpdateRow(entry, s)
#--------successfully updating.


















































