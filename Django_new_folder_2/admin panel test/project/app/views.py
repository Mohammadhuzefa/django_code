from django.shortcuts import render,redirect
from .models import User,Todo
from django.contrib import messages
# Create your views here.



# def admindash(req):
#      return render(req,'admindash.html')


def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        if e == 'admin@gmail.com' and p == 'admin':
                req.session['admin_e'] = e
                req.session['admin_p'] = p
                req.session['admin_n'] = 'admin'
                return render(req,'dashboard.html')
        

        else:
            x={'g':"wrong passord or username"}
            return render(req,'login.html',{'data':x})
        
            
    return render(req, 'login.html')


def dashboard(req):
    user_details = {
    "user_name" : req.session.get("user_name"),
    "user_email" : req.session.get("user_email")
    }

    return render(req,"dashboard.html",{"dashboard_content":True,"user_detail":user_details})

def todo_list(req):
    task_detail = Todo.objects.all()
    return render(req,"dashboard.html",{"todo_list":True , "task_detail":task_detail})

def add_task(req):
    if req.method == 'POST':
        task = req.POST.get("task")
        task_exist = Todo.objects.filter(task = task).first()

        if task_exist:
            messages.error(req, "Task already exists")
            return redirect("todo_list")
        else:
            Todo.objects.create(task = task)
            messages.success(req, "Task Added succesfull..!")
            return redirect("todo_list")
        
    messages.warning("Not empty task can't be listed !")
    return redirect("todo_list")
            
def delete_task(req,task_id):   
    deleted_task = Todo.objects.get(id = task_id)
    deleted_task.delete()
    return redirect("todo_list")

def edit_task(req,task_id):
    task = Todo.objects.get(id=task_id)
    task_detail = Todo.objects.all()

    return render(req, "dashboard.html", {
        "todo_list": True,
        "task_detail": task_detail,
        "edit_task_obj": task
    })

def update_task(req, task_id):
    if req.method == "POST":
        task = Todo.objects.get(id=task_id)
        task.task = req.POST.get("task")
        task.save()
        messages.success(req, "Task updated successfully.")

    return redirect("todo_list")


