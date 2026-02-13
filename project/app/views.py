from django.shortcuts import render ,redirect
from app.models import Employee

# Create your views here.

def index(req):
    return render(req,'index.html')

def Registration(req):
    if req.method == 'POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('contact')
        p=req.POST.get('password')
        cp=req.POST.get('cpassword')
        ph=req.FILES.get('photo')
        a=req.FILES.get('audio')
        v=req.FILES.get('video')
        d=req.FILES.get('resume')
        q=req.POST.getlist('qualification')
        g=req.POST.get('gender')
        ch=req.POST.get('city')
        user = Employee.objects.filter(Email=e)
        print(user)
        if not user:
            if p == cp:
                Employee.objects.create(
                    Name=n,
                    Email=e,
                    Contact=c,
                    Password=p,
                    CPassword=cp,
                    Photo=ph,
                    Audio=a,
                    Video=v,
                    Resume=d,
                    City=ch,
                    Qualification=q,
                    Gender=g
                )
                return redirect('Login')
            else:
                msg = "Password and confirm not matched"
                userdata = {'name':n,'contact':c,'email':e}
                return render(req,'Registration.html',{'pmsg':msg,'data':userdata})
        
        else:
            msg='This email already exist'
            return render(req,'Registration.html',{'msg':msg})
    
    return render(req,'Registration.html')

def Login(req):
    if req.method=='POST':
        e=req.POST.get('email')
        p=req.POST.get('password')
        if e=='admin@gmail.com' and p=='admin':
            a_data={
                'id':1,
                'name':'Admin',
                'email':'admin@gmail.com',
                'password':'admin'
            }
            req.session['a_data']=a_data
            return redirect('admindeshboard')
        else:
            user=Employee.objects.filter(Email=e)
            if not user:
                msg="Register First"
                return redirect('Registration')
            else:
                userdata = Employee.objects.get(Email=e)
                if p==userdata.Password:
                    req.session['user_id']=userdata.id 
                    return redirect('userdeshboard')
                else:
                    msg='Email & password not mach'
                    return render(req, 'Login.html',{'x':msg})
            
    return render(req,'Login.html')

def userdeshboard(req):
    if 'user_id' in req.session:
        x=req.session.get('user_id')
        userdata = Employee.objects.get(id=x)
        return render(req, 'userdeshboard.html',{'data':userdata})
    return render('Login')


def admindeshboard(req):
    if 'a_data' in req.session:
        a_data =req.session.get('a_data')
        return render(req,'admindeshboard.html',{'data':a_data})
    else:
        return redirect('Login')

def logout(req):
    if 'user_id' in req.session:
        req.session.flush()
        return redirect('Login')
    return render('Login')