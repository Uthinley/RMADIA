from django.shortcuts import render, redirect
from .models import report
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def verify(request, id):
    if id:
        details = report.objects.get(id=id)
       
        return render(request, "details.html", {'details':details})


def verify_drop(request):
    if 'drop' in request.POST:
        id = request.POST['id']
        t = report.objects.get(id=id)
        t.status = "D"
        t.save()
        
        return redirect('login_submit_page')

    elif 'verify'in request.POST:
        id = request.POST['id']
        v = report.objects.get(id=id)
        v.status="V"
        v.save()

        return redirect('login_submit_page')


def loginsubmit(request):
    if request.session.has_key('user'):
        context = report.objects.all()
        total = report.objects.all().count()
        print("session is there.********************************")
        
        return render(request, "admindashboard.html", {'context':context, 'total':total})
        
    else:
        if request.method == 'POST':
            username =  request.POST['login_user']
            password = request.POST['passwd']

            user = auth.authenticate(username=username, password=password)
        
            if user is not None:
                auth.login(request, user)
                context = report.objects.all()
                total = report.objects.all().count()
                request.session['user'] = username
                print("sesssion just stated &&&&&&&")
                return render(request, "admindashboard.html", {'context':context, 'total':total})
            else:
                messages.info(request, "Invalid Credentials")
                print('here in invalid')
                return render(request,'login.html')
        else:
            pass
        #     return render(request, "login.html")

def logout(request):
    if request.session.has_key('user'):
        auth.logout(request)
        request.session.flush()
        return redirect("login_page")


def submit(request):
    if request.method ==  'POST':
        Eid = request.POST['Eid']
        email = request.POST['email']
        sname = request.POST['sname']
        sjob = request.POST['sjob']
        sphone = request.POST['sphone']
        saddress = request.POST['saddress']
        whatwrong = request.POST['whatwrong']
        whowrong = request.POST['whowrong']
        wherewrong = request.POST['wherewrong']
        whoenabled = request.POST['whoenabled']
       # location = request.POST['location']
        incident_date = request.POST['incident_date']
        solution = request.POST['solution']

        #file upload
        uploaded_file = request.FILES['a_file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)
        
        report_info = report(Employee_Id=Eid, Employee_email=email, S_name=sname, s_job_pos=sjob, s_phone= sphone, 
        s_address= saddress, what_wrong=  whatwrong, who_wrong= whowrong, where_wrong= wherewrong, enabled_wrong= whoenabled, solution= solution,
        incident_date= incident_date, documents=uploaded_file_url)

        report_info.save()

        print(report_info.save())
        messages.info(request, "Information has been submitted successfully!!")


        return redirect('index_page')
    else:
         messages.info(request, "There was problem submitting the information. please contact the system administrator.")
        

