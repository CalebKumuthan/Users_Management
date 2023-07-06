from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import autocall
from .models import callhistory
from twilio.rest import Client
import time
from datetime import timedelta

# Create your views here.
def home(request):
    mydata = autocall.objects.all()
    if(mydata!=''):
        return render(request, 'myapp/home.html', {'mydatas' : mydata})
    else:
        return render(request,'myapp/home.html')
    
def updateData(request,id):
    mydata = autocall.objects.get (id=id)
    name = mydata.Name
    account_sid = "AC0826429264e697b99488ba2c5ea35115"
    auth_token = "1017a35a3ea4364af5ea6c08ee41a4f0"
    client = Client(account_sid, auth_token)
    contact = mydata.Contact

    
    call = client.calls.create(
        record = True,
          twiml = (
                    f'<Response>'
                    f'<Say voice="alice">Hi there! Welcome, {name}!</Say>'
                    f'<Dial>+1 833-545-3149</Dial>'
                    f'</Response>'
                ),
        to = f"+{contact}",
        from_="+14124656255"
    )

    print(call.sid)
    messages.success(request, "Call finished suxxessfully...!!!")
    while call.status not in ['completed', 'answered', 'failed', 'busy', 'no-answer']:
        time.sleep(1)
        call = client.calls(call.sid).fetch()

    duration_seconds = call.duration
    duration_timedelta = timedelta(seconds=int(duration_seconds))
    duration_formatted = str(duration_timedelta)
    call_status = call.status

    o = callhistory()
    o.Name = name
    o.Contact = contact
    o.Status = call_status
    o.Callduration = duration_formatted
    o.save()

    call_sid = call.sid
    recording_list = client.recordings.list(call_sid=call_sid)

    if recording_list:
        recording = recording_list[0]  # Assuming there is only one recording
        recording_sid = recording.sid
        o.Recording_url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}.mp3'
        o.save()

    return redirect('myapp:home')

def addcustomer(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']

        obj = autocall()
        obj.Name = name
        obj.Contact = contact
        obj.Email = email
        obj.save()

        mydata = autocall.objects.all()
        return redirect('myapp:home')
    return render(request,'myapp/addcustomer.html')

def login(request):
    if request.method == 'POST':
        mydata = autocall.objects.all()
        email = request.POST['exampleInputEmail1']
        password = request.POST['exampleInputPassword1']

        if(email == "admin@movex.ai" and password == "123admin"):
            mydata = autocall.objects.all()
            if(mydata!=''):
                return render(request, 'myapp/home.html', {'mydatas' : mydata})
            else:
                return render(request,'myapp/home.html')
        else:
            messages.error(request, "Incorrect Details")
            return redirect('myapp:login')
        
        
    
    else:
        return render(request, 'myapp/login.html')
    
def customerdetails(request):
    mydata = autocall.objects.all()
    if(mydata!=''):
        return render(request, 'myapp/customer_detail.html', {'mydatas' : mydata})
    else:
        return render(request,'myapp/customer_detail.html')
    
def call_history(request):
    mydata = callhistory.objects.all()
    if(mydata!=''):
        return render(request, 'myapp/callhistory.html', {'mydatas' : mydata})
    else:
        return render(request,'myapp/callhistory.html')
    
