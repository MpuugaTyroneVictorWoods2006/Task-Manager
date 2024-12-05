from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

tasks = {}
task_counter = 0
def index(request):
    global task_counter
    global tasks_list
    if request.method == 'POST':
        task_item = request.POST.get('task')
        if task_item:  # Only add if it's not empty
            task_counter += 1
            tasks[task_item] = task_counter
            tasks_list = list(tasks.values())
    return render(request, 'tasks/index.html', {'tasks': tasks})
