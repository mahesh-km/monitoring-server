#!/usr/bin/python
#This script will update google spreadsheet with led value from m/monit server json response
import sys
import json
import urllib2
import os
from datetime import datetime
from subprocess import Popen
import gdata.docs.service
import gdata.spreadsheet.service
import gdata.spreadsheets.data
from KAhostNameDict import kahost_dict
from DLhostNameDict import dlhost_dict
#
date = str(datetime.now())
#----read json from url
try:
    url = "http://mmonit.vyoma-media.com:10001/status/hosts/list"
    data = urllib2.urlopen(url).read()
    data = json.loads(data)
except:
    #print "server busy or not responding!"
    with open('dashboard.log','a') as f:
         f.write(date)
         f.write(' server not responding or no host data avilable!\n')
         f.close()  
    quit()
#
#------ read from local file
#json_file = open('Formatted-mmonit.json')
#data = json.load(json_file)
#json_file.close()
# print data
#
#---dict for store led values(eg:0,1,2,3)
dict_led = {}
dict_status = {}
for record in data['records']:
    store = record['hostname']
    dict_led[store] = record['led']
    dict_status[store] = record['status']
#print dict_led
#print dict_status
#--email and pwd
email = 'mahesh@vyoma-media.in'
password = 'yokoma2gmail2013'
#email = 'autobot@vyoma-media.in' 
#password = 'aIMBYa8D0ojk'  
spreadsheet_key = '0AqVK32zw_dAldDVicGRsWWxxM1lYT3dQVmxSakduVGc'
#spreadsheet_key_status = '0AqVK32zw_dAldDVicGRsWWxxM1lYT3dQVmxSakduVGc'
spreadsheet_key_delhi = '0Aukv4_xbTzv-dFNQdXJxLWE2djV3LWdzSGFOd29pVVE'
spreadsheet_key_delhi_status = '0AqVK32zw_dAldDVicGRsWWxxM1lYT3dQVmxSakduVGc'
worksheet_id = 'od6'
worksheet_id_delhi = 'od7'
#worksheet_id_status = 'od9'
worksheet_id_delhi_status = 'ocw'
#
spr_client = gdata.spreadsheet.service.SpreadsheetsService()
spr_client.email = email
spr_client.password = password
spr_client.source = 'Vyoma Media Remote Monitoring|Dashboard'
spr_client.ProgrammaticLogin()
#
#for key, value in kahost_dict.items():
#     print  key, value
#    try:
        #led = unicode(dict_led[key])
        #status = dict_status[key]
        #row = unicode(value["row"])
        #col = unicode(value["col"])
        #rows = unicode(value["rows"])
        #cols = unicode(value["cols"])
        #screen = unicode(value["screen"])
	#print led, status, row, col, rows, cols, screen
	#checking for duel screen or single
        #if screen == '2':
            #if key.startswith("Dl"):
           # rowsec = unicode(value["rowsec"])
	   # colsec = unicode(value["colsec"])
	   # rowsecs = unicode(value["rowsecs"])
	   # colsecs = unicode(value["colsecs"])
	    #updating cell value
        #spr_client.UpdateCell(row, col, led,spreadsheet_key, worksheet_id)
	   # spr_client.UpdateCell(rowsec, colsec, led,spreadsheet_key, worksheet_id)
           # spr_client.UpdateCell(rows, cols, status,spreadsheet_key_status, worksheet_id_status)
           # spr_client.UpdateCell(rowsecs, colsecs, status,spreadsheet_key_status, worksheet_id_status)
       # else:
            #updating cell value
           # spr_client.UpdateCell(row, col, led,spreadsheet_key, worksheet_id)
           # spr_client.UpdateCell(rows, cols, status,spreadsheet_key_status, worksheet_id_status)
            #print key, row, col
   # except:
   #     print key," ,host not avilable on server!"
#
for key, value in dlhost_dict.items():
        print  key, value
    #try:
#        led = unicode(dict_led[key])
	#print led
        status = dict_status[key]
	#print status
        row = unicode(value["row"])
        col = unicode(value["col"])
        rows = unicode(value["rows"])
        cols = unicode(value["cols"])
        #updating cell value
        spr_client.UpdateCell(row, col, led,spreadsheet_key_delhi, worksheet_id_delhi)
        #spr_client.UpdateCell(rows, cols, status,spreadsheet_key_delhi_status, worksheet_id_delhi_status)
        #print key, row, col
   # except:
   #     print key," ,host not avilable on server!"
#logging, time UTC standerd.
#with open('dashboard.log','a') as f:
 #   f.write(date)
 #   f.write(' sucessfully updated!\n')
 #   f.close()
#'KaYasvaUtsB0005': {'row':17,'col':11,'rows':51,'cols':3,'screen':1},







































