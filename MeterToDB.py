#!/usr/bin/env python3

import time
import sys
import time
import pymysql
from subprocess import Popen, PIPE

_DBSERVER_ = "address"
_DBUSER_   = "user"
_DBPASS_   = "pass"
_DBNAME_   = "dbname"

_RTLAMRPATH_ = "/path/to/rtlamr"

_METERID_ = "00000000"

class PostToDB(object):
        
    def ReadMeter(self):
        with Popen([_RTLAMRPATH_,'-filterid=' + _METERID_,'-quiet=true','-format=csv','-unique=true'],universal_newlines=True, stdout=PIPE, bufsize=1) as p:
            for line in p.stdout:
                csv = line.split(",")
                reading = int(csv[7])
                timefull = csv[0]
                tempA = timefull[:19]
                timestamp = tempA.replace("T"," ")
                connection = pymysql.connect(_DBSERVER_,_DBUSER_,_DBPASS_,_DBNAME_)
                try:
                    with connection.cursor() as cursor:
                        sql = "INSERT INTO powermeter_data (kWH,ReadingTime) VALUES (%s, %s)"
                        cursor.execute(sql, (reading,timestamp))
                        print(reading, " ", timestamp)
                    connection.commit()
                finally:
                    connection.close()                    
                    
        return
            
def main():
    poster = PostToDB()
    while True:
        poster.ReadMeter()
        print("Made it to main loop - something broke")

if __name__ == "__main__":
    main()
    