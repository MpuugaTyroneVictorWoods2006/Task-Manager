from django.shortcuts import render
from django.http import HttpResponse

tasks = []
def index(request):
    if request.method == 'POST':
        # Get the text from the form input
        task_item = request.POST.get('task')
        if task_item:  # Only add if it's not empty
            tasks.append(task_item)
    return render(request, 'tasks/index.html', {'tasks': tasks})