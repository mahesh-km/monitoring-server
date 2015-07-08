#!/usr/bin/python
#-------------------------------------------------------------------------------------#
#Using gdata ,here updating google spread sheet with the ddis media update log        #                                                                                     #
#collected from the host systems.                                                     #                               #
#-------------------------------------------------------------------------------------#
import sys
import json
import urllib2
import os
from datetime import datetime
from subprocess import Popen
import gdata.docs.service
import gdata.spreadsheet.service
import gdata.spreadsheets.data

