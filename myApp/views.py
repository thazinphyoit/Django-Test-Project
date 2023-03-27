from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import pymongo
connection = pymongo.MongoClient('localhost', 27017)
database = connection['django_db']
collection = database['django_col']
# collection.insert_one({"_id": 1, "name": "phyo", "age": 27, "hobby": "coding"})

def home (request) :

    try :
        # return HttpResponse("Hello World !")
        # return render(request, 'home.html', {'user': '"THAZIN"'})

        data = collection.find_one()
        print("******** ", data)

        return render(request, 'home.html', data)
    
    except Exception as error :

        print(error)
        return render(request, 'home.html', {'error': error})
