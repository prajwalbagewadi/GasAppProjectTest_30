from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .models import CustReq
# Create your views here.
uid=0
def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username="abc",password="123")
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("invalid login")
    return render(request,'login.html')    


def home_view(request):
    #return render(request,'home.html')
    global uid
    if request.method == 'GET':
        #return render(request,'home.html')
        requests = CustReq.objects.all()
        return render(request, 'home.html', {'requests': requests})
    
    elif request.method == 'POST':
        userid=uid
        username=request.user.username
        phoneno=request.POST.get('phone')
        addr=request.POST.get('address')
        iss=request.POST.get('dropdown')
        CustReq.objects.create(
            usid=userid,
            user=username,
            phone=phoneno,
            add=addr,
            issue=iss,
            stat=""
        )
        uid+=1
        return redirect('success')
    else:
        return HttpResponse("Request issue")
    
    
def success_view(request):
    return render(request,'success.html')

def service_view(request):
    requests=CustReq.objects.all()
    
    if request.method == 'POST':
        # Fetch all requests including their statuses
        requests = CustReq.objects.all()
        # Process the form data to update the status of each request
        for req in CustReq.objects.all():
            #requests = CustReq.objects.all()
            status = request.POST.get(f"stat_{req.id}")  # Fetch status by request ID
            if status:
                req.stat = status
                req.save()  # Save the updated status to the database
        return render(request, 'home.html', {'requests': requests})
    else:
        return render(request,'service.html',{'requests':requests})