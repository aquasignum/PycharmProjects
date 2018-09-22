from datetime import datetime
import random
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import calendar

def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()



def main():
    co2 = (random.randint(400, 1000))
    i = 1
    while i == 1:
        print(co2, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        co2 = (random.randint(400, 1000))
       # co2_file.write(str(co2) + "," + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
       # co2_file.flush()

        scope = ' '.join(['https://www.googleapis.com/auth/drive'])

        credentials = ServiceAccountCredentials.from_json_keyfile_name('aquasignum-3e9afbfcf88c.json', scope)

        gc = gspread.authorize(credentials)

        wks = gc.open('test').sheet1
        #wks.append_row([(co2), json.dumps(datetime.now(), default=myconverter)])
        #print(json.dumps(datetime.now(), default=myconverter))
        # wks.append_row()
        wks.append_row([datetime.now().strftime("%Y/%m/%d %H:%M:%S"), (co2)])

        # print(wks.get_all_records())
        time.sleep(.5)
if __name__ == '__main__':
    main()
