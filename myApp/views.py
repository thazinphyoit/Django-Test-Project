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

        res_data = collection.find_one()
        print("******** ", res_data)

        # return render(request, 'home.html', {"id": data['_id'], "name": data['name'], 'age': data['age'], 'hobby': data['hobby']})
        return render(request, 'home.html', {"data":res_data})
    
    except Exception as error :

        print(error)
        return render(request, 'home.html', {'error': error})

def result (request) :

    try :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        return render(request, 'result.html', {"name": username, "email": email, "password": password})
    
    except Exception as error :

        print(error)
        return render(request, 'result.html', {'error': error})
