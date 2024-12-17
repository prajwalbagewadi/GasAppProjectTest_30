from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .models import CustReq
import random
# Create your views here.
uid=0

def sign_view(request):
    if  request.method == 'POST':
        print(request.POST) 
        if 'signup' in request.POST:
            username=request.POST.get('username')
            Email=request.POST.get("Email")
            password=request.POST.get('password')
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists. Please choose a different username.")
            user = User.objects.create_user(username=username, password=password, email=Email)
            user.save()
            print("Sign up clicked")
            return redirect('successuser')
        # user=authenticate(request,username=use,password=pas)
        # if user is not None:
        #     login(request,user)
        #     return HttpResponse("invalid login")
        # else:
        #     return redirect('login')
        elif 'login' in request.POST:
            return redirect('login')
        elif 'admin' in request.POST:
            return redirect('servicelogin')
    return render(request,'signup.html')    

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("invalid login")
    return render(request,'login.html')    

def service_login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username="user",password="123")
        if user is not None:
            login(request,user)
            return redirect('service')
        else:
            return HttpResponse("invalid login")
    return render(request,'servicelogin.html') 

#service_view
# def service_view(request):
#     #return render(request,'home.html')
#     if request.method == 'GET':
#         return render(request,'service.html') 

def home_view(request):
    #return render(request,'home.html')
    global uid
    if request.method == 'GET':
        cusname=request.user.username
        #return render(request,'home.html')
        requests = CustReq.objects.filter(user=cusname).all()
        return render(request, 'home.html', {'requests': requests})
    
    elif request.method == 'POST':
        userid=uid
        username=request.user.username
        phoneno=request.POST.get('phone')
        addr=request.POST.get('address')
        iss=request.POST.get('dropdown')
        CustReq.objects.create(
            #usid=userid,
            user=username,
            phone=phoneno,
            add=addr,
            issue=iss,
            stat="",
            reqid=random.randint(1,4000)
        )
        uid+=1
        return redirect('success')
    else:
        return HttpResponse("Request issue")

def successuser_view(request):
    return render(request,'usersuccess.html')    
    
def success_view(request):
    return render(request,'success.html')

def service_view(request):
    requests=CustReq.objects.all()
    
    if request.method == 'POST':
        if 'submit' in request.POST:
            # Fetch all requests including their statuses
            requests = CustReq.objects.all()
            # Process the form data to update the status of each request
            for req in CustReq.objects.all():
                #requests = CustReq.objects.all()
                status = request.POST.get(f"stat_{req.reqid}")  # Fetch status by request ID
                if status:
                    req.stat = status
                    req.save()  # Save the updated status to the database
            return render(request, 'home.html', {'requests': requests})
        else:
            delete_ids=request.POST.getlist('delete_requests')
            for req_id in delete_ids:
               req=CustReq.objects.filter(reqid=req_id)
               req.delete()
            return render(request, 'home.html', {'requests': requests})
    return render(request, 'service.html', {'requests': requests})