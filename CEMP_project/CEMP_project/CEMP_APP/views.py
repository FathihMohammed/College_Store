from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import department,course,detailsclass
from .forms import detailsform


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def details(request):
    c=course.objects.all()
    d=department.objects.all()
    det=detailsclass.objects.all()
    if request.method=='POST':
        s_name=request.POST.get('name','')
        dob=request.POST.get('dob','')
        age=request.POST.get('age','')
        phno=request.POST.get('phno','')
        mail=request.POST.get('email','')
        address=request.POST.get('address', '')
        t1=detailsclass(s_name=s_name,dob=dob,age=age,phno=phno,email=mail,address=address)
        t1.save();
        messages.info(request, "Order Placed")
        def clean(self):
            cleaned_data = super().clean()
            required_fields = ['s_name', 'dob', 'age','phno','mail','address']
            for field_name in required_fields:
                if not cleaned_data.get(field_name):
                    self.add_error(field_name, "This field is required")
    return render(request,'details.html',{'course':c,'department':d})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('CEMP_APP:about')
        else:
            messages.info(request, 'Inavild Credentials')
            return redirect('CEMP_APP:login')
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        try:
            if pass1 == pass2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Already Taken")
                    return redirect('CEMP_APP:register')
                else:
                    user = User.objects.create_user(username=username,password=pass1)
                    user.save();
                    messages.info(request, "user created")
                    return redirect('CEMP_APP:login')
            else:
                messages.info(request, "Password Mismatch")
                return redirect('CEMP_APP:register')
                return redirect('/')
        except:
            pass
            return redirect('CEMP_APP:register')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')