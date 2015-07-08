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

def get_json(url):

    try:
        #url = "http://mmonit.vyoma-media.com:8080/status/hosts/list"
        data = urllib2.urlopen(url).read()
        data = json.loads(data)
        return data
    except:
    #print "server busy or not responding!"
        with open('dashboard.log','a') as f:
            f.write(date)
            f.write(' server not responding or no host data avilable!\n')
            f.close()  
            quit()


def update_sheet(data):


    dict_led = {}
    for record in data['records']:
        store = record['hostname']
        dict_led[store] = record['led']


    #print dict_led


#--email and pwd
    email = 'mahesh@vyoma-media.in'
    password = 'yokoma2012'
    spreadsheet_key = '0Ap1cvRKx4murdG5uQkFuR2lpNC1lN3BCeU8xT1F5UGc'
    worksheet_id = 'od6'
#
    spr_client = gdata.spreadsheet.service.SpreadsheetsService()
    spr_client.email = email
    spr_client.password = password
    spr_client.source = 'dev'
    spr_client.ProgrammaticLogin()
#hostname data
    host_dict = {'KaCity0Plasma': {'row':7,'col':5},'KaCantoPlasma': {'row':16,'col':5},
                 'KaCity0UtsF0001': {'row':7,'col':6},'KaCantoUtsB0002': {'row':16,'col':7},
                 'KaCity0UtsF0002': {'row':7,'col':7},'KaCantoUtsB0003': {'row':16,'col':8},
                 'KaCity0UtsF0003': {'row':7,'col':8},'KaCantoUtsB0004': {'row':16,'col':9},
                 'KaCity0UtsF0004': {'row':7,'col':9},'KaCantoUtsB0005': {'row':16,'col':10},
                 'KaCity0UtsF0005': {'row':7,'col':10},'KaCantoPrsF0001':{'row':15,'col':6},
                 'KaCity0UtsF0006': {'row':7,'col':11},'KaCantoPrsF0002':{'row':15,'col':7},
                 'KaCity0UtsF0007': {'row':7,'col':12},'KaCantoPrsF0003':{'row':15,'col':8},
                 'KaCity0UtsF0008': {'row':7,'col':13},'KaCantoPrsF0004':{'row':15,'col':9},
                 'KaCity0UtsF0009': {'row':7,'col':14},'KaCantoPrsF0005':{'row':15,'col':10},
                 'KaCity0UtsF0010': {'row':7,'col':15},'KaCantoPrsF0006':{'row':15,'col':11},
                 'KaCity0UtsF0011': {'row':7,'col':16},
                 'KaCity0UtsF0012': {'row':7,'col':17},
                 'KaCity0UtsF0013': {'row':7,'col':18},
             }
    for key, value in host_dict.items():
    #    print  key, value
        try:
            led = unicode(dict_led[key])
            row = unicode(value["row"])
            col = unicode(value["col"])
            #updating cell value
            spr_client.UpdateCell(row, col, led,spreadsheet_key, worksheet_id)
            #print key, row, col
        except:
            print key," ,host not avilable on server!"
    #logging, time UTC standerd.
    with open('dashboard.log','a') as f:
        f.write(str(datetime.now()))
        f.write(' sucessfully updated!\n')
        f.close()

def main_loo():
    data = get_json("http://mmonit.vyoma-media.com:8080/status/hosts/list")
    update_sheet(data)

