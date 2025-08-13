from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.to_do_list
users_collection = db.users
tasks_collection = db.tasks

def home(request):
    return render(request, "index.html")

@csrf_protect
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = users_collection.find_one({"email": email, "password": password})

        if user:
            request.session["name"] = user.get("name")
            request.session["email"] = user.get("email")
            return redirect('tasks_page')
        else :
            return redirect('register')
    return render(request, "index.html")
    
@csrf_protect
def register(request):
    if request.method == "POST":
        name = request.POST.get("fullname")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if users_collection.find_one({"email": email}):
            return HttpResponse("Email already registered", status=400)
        
        users_collection.insert_one({"name": name, "email": email, "password":password})
        return redirect('login')
    return render(request, "register.html")
@csrf_protect
def tasks_page(request):
    fullname = request.session["name"]
    email = request.session["email"]
    tasks = []
    for task in tasks_collection.find({"email": email}):
        tasks.append({
            "id": str(task["_id"]),
            "task": task["task"]
        })
    return render(request, 'tasks_page.html',{"name": fullname, "email": email, "tasks": tasks})

@csrf_protect
def add_task(request):
    if request.method == "POST":
        task = request.POST.get("task")
        email = request.session.get("email")

        if email and task:
            tasks_collection.insert_one({
                "email": email,
                "task": task
            })

    return redirect('tasks_page')

@csrf_protect
def delete_task(request, task_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    email = request.session.get("email")
    # use task_id (string) -> ObjectId conversion
    try:
        tasks_collection.delete_one({"_id": ObjectId(task_id), "email": email})
    except Exception:
        pass
    return redirect('tasks_page')