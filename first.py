from datetime import datetime
from os import sys
from os import getcwd
from os import environ
odds = [1,3,5]
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("odd")
else:
    print("even")

print(right_this_minute)
where_am_I = getcwd()

print(where_am_I)
print(sys.platform)
print(environ)
print(('HOME'))
print(datetime.today())
#print(datetime.date.isoformat(today()))
