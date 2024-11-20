from django.shortcuts import render
from django.http import HttpResponse

tasks = ["Go shopping", "Buy Car", "Eat Lunch"]
def index(request):
    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })