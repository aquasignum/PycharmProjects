import datetime
from datetime import datetime
import random
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import json
from json import dumps


co2_file = open("co2.txt","a")

#print(datetime.now())

#print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def default(obj):
    """Default JSON serializer."""
    import calendar, datetime

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        millis = int(
            calendar.timegm(obj.timetuple()) * 1000 +
            obj.microsecond / 1000
        )
        return millis
    raise TypeError('Not sure how to serialize %s' % (obj,))

co2 = (random.randint(400,1000))
i=1
while i==1:
    print (co2, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    co2 = (random.randint(400,1000))
    co2_file.write(str(co2) +"," + datetime.now().strftime("%Y-%m-%d %H:%M:%S")+ '\n')
    co2_file.flush()


    scope = ' '.join(['https://www.googleapis.com/auth/drive'])

    credentials = ServiceAccountCredentials.from_json_keyfile_name('aquasignum-3e9afbfcf88c.json', scope)

    gc = gspread.authorize(credentials)

    wks = gc.open('test').sheet1
    wks.append_row([datetime.now().isoformat(), (co2)])
   # print (json.dumps(datetime.now()), default=default)
    #wks.append_row()
   #wks.append_row([datetime.now().isoformat(), (co2)])

#print(wks.get_all_records())
    time.sleep(5)