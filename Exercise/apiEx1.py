import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True :
    address = input("Enter location : ")
    if len(address) < 1 : break

<<<<<<< HEAD
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ urllib.parse.urlencode({'address':address}) + '&'
=======
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ urllib.parse.urlencode({'address':address}) + ''
>>>>>>> 4284d1dec72f3351305d0e21580c6e0c1b66f13e

    print('Retriving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived',len(data),'characters')

    try :
        js = json.loads(data)
        print(js["results"][0]["geometry"]["location"]["lat"])
        print(js["results"][0]["geometry"]["location"]["lng"])
        print(js["results"][0]["geometry"]["location_type"])
        print(js["results"][0]["geometry"]["viewport"]["northeast"]["lat"])
    except :
        js = None

    if not js or 'status' not in js or js['status']!='OK' :
        print('Fail')
        print(data)
        continue
