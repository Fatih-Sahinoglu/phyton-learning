#datetime---------------------------------------------------------------------------------------------
import datetime

#year-month-day hours:minutes:second:microsecond
datetime.datetime.now()
#BUT this contains all datetime library and writing is hard

from datetime import datetime
#from library import class
#also can use for one function  (from math import factorial)

datetime.now() #this is enough now

datetime(2025,3,1,13,23,5)
#year-month-day hours:minutes:second

mydate=datetime.now()

mydate.year #hour minute day... also okey

datetime.weekday(mydate) #monday=0 ... sunday=6
datetime.ctime(mydate) #sun Jan 12(day) 16:39:18 2026


#----------------------------------------------------------------------
mydate.strftime("%a %A") 
#short weekday %A long weekday
#%b %B short and long month name
#%y %Y short and long year number
#%H %I hours but 24 and 12
#%w sunday=0 monday=1.... -> give a number
#%m number of month
#%d day of months
#%p PM or AM
#%M %S minute and second
#%f microsecond
#%j day of year
#----------------------------------------------------------------------


import locale
locale.setlocale(locale.LC_TIME,"tr-TR.UTF-8") #setting Turkish locale

print(mydate.strftime("%d.%B.%Y %A")) #Now answers will Turkish


text="20 September 2009 hour 14:35:21"
dat=datetime.strptime(text,"%d %B %Y hour %H:%M:%S") #Transform text to time


date1=datetime(2025,1,1)
date2=datetime(2026,1,1)

(date1-date2).days #(get entire datetime thing) just day number


from datetime import timedelta
date1=date2+timedelta(year=2,minutes=59,hours=8) #We can increase or dicrease time


from datetime import time,date
date1=time(14,58,55) #creating just time and just date
date2=date(2026,2,28)
mydate=datetime.combine(date2,date1) #combine them first date second time


mydate.replace(hour=7,minute=23) #Changed time


#time module--------------------------------------------------------------------------------------
import time

time.sleep(5) #wait 5 second and after that continue

