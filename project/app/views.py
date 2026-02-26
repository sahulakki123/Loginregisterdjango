from django.shortcuts import render ,redirect
from app.models import Employee , Department,AddEmployee,Query
from django.contrib import messages
from django.core.mail import send_mail

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
                'name':'Admin Lakki',
                'email':'admin@gmail.com',
                'password':'admin',
                'image':'images/admin.png'
            }
            req.session['a_data']=a_data
            return redirect('admindeshboard')
        else:
            em = AddEmployee.objects.filter(Email=e)
            if em:
                emp_data=AddEmployee.objects.get(Email=e)
                if p==emp_data.Code:
                    req.session['emp_id']=emp_data.id
                    return redirect('empdeshbord')
                else:
                    messages.warning(req,'Email & password not match')
                    return redirect('Login')
            else:
                messages.warning(req,'Employee dose not esist')
                return redirect('Login')
            
            # user=Employee.objects.filter(Email=e)
            # if not user:
            #     msg="Register First"
            #     return redirect('Registration')
            # else:
            #     userdata = Employee.objects.get(Email=e)
            #     if p==userdata.Password:
            #         req.session['user_id']=userdata.id 
            #         return redirect('userdeshboard')
            #     else:
            #         msg='Email & password not mach'
            #         return render(req, 'Login.html',{'x':msg})
            
    return render(req,'Login.html')


def empdeshbord(req):
    if 'emp_id' in req.session:
        eid=req.session.get('emp_id')
        emp_data = AddEmployee.objects.get(id=eid)
        return render(req, 'empdeshbord.html',{'data':emp_data})
    else:
        return redirect('Login')
    
def profile(req):
   if 'emp_id' in req.session:
      eid = req.session.get('emp_id')
      emp_data = AddEmployee.objects.get(id=eid)
      return render(req,'empdeshbord.html',{'data':emp_data , 'profile':True})
   return redirect('Login')

def setting(req):
   if 'emp_id' in req.session:
      eid = req.session.get('emp_id')
      emp_data = AddEmployee.objects.get(id=eid)
      return render(req,'empdeshbord.html',{'data':emp_data , 'setting':True})
   return redirect('Login')

def empquery(req):
    if 'emp_id' in req.session:
        eid = req.session.get('emp_id')
        emp_data = AddEmployee.objects.get(id=eid)
        emp_dept = Department.objects.all()
        return render(req,'empdeshbord.html',{'data':emp_data , 'empquery':True, 'emp_dept':emp_dept})
  
    else:
        return redirect('Login')
        

def querydata(req):
    if req.method =='POST':
        if 'emp_id' in req.session:
            n = req.POST.get('name')
            e = req.POST.get('email')
            d = req.POST.get('department')
            q = req.POST.get('query')
            Query.objects.create(Name=n,Email=e,Departments=d,Query=q)
            messages.success(req, "Query created....")
            e_id = req.session.get('emp_id')
            emp_data = AddEmployee.objects.get(id=e_id)
            emp_dept = Department.objects.all()
            return render(req,'empdeshbord.html',{'data':emp_data , 'empquery':True, 'emp_dept':emp_dept})
        else:
            return redirect('Login')
        
        
def allquery(req):
    if 'emp_id' in req.session:
        e_id = req.session.get('emp_id')
        emp_data = AddEmployee.objects.get(id=e_id)
        all_query = Query.objects.filter(Email=emp_data.Email)
        return render(req,'empdeshbord.html',{'data':emp_data , 'allquery':True, 'all_query':all_query})
    else:
        return redirect('Login')   
    
    
    
def pendingquery(req):
    if 'emp_id' in req.session:
        e_id = req.session.get('emp_id')
        emp_data = AddEmployee.objects.get(id=e_id)
        all_query = Query.objects.filter(Email=emp_data.Email, Status=False)
        return render(req, 'empdeshbord.html', {'data':emp_data,'pendingquery':True , 'all_query':all_query})
    else:
        return redirect('Login')
    
def donequery(req):
    if 'emp_id' in req.session:
        e_id = req.session.get('emp_id')
        emp_data = AddEmployee.objects.get(id=e_id)
        all_query = Query.objects.filter(Email=emp_data.Email, Status=True)
        return render(req, 'empdeshbord.html', {'data':emp_data,'donequery':True , 'all_query':all_query})
    else:
        return redirect('Login')
    

    
        
    
     


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
    return redirect('Login')

def add_dep(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        return render(req,'admindeshboard.html',{'data':a_data , 'add_dep':True})
    else:
        return redirect('Login')
    
    
def save_dep(req):
    if 'a_data' in req.session:
        if req.method == 'POST':
           
            dn=req.POST.get('dep_name')
            dd=req.POST.get('dep_desc')
            dh=req.POST.get('dep_head')
            dept=Department.objects.filter(Dep_name=dn)
            if dept:
               messages.warning(req,'department already exist')
               a_data= req.session.get('a_data')
               return render(req,'admindeshboard.html',{'data':a_data , 'add_dep':True})
            else:
                Department.objects.create(Dep_name=dn,Dep_desc=dd,Dep_head=dh)
                messages.success(req,'Department created')
                a_data= req.session.get('a_data')
                return render(req,'admindeshboard.html',{'data':a_data , 'add_dep':True})
    else:
        return redirect('Login')
    
def show_dep(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        departments = Department.objects.all()
        return render(req,'admindeshboard.html',{'data':a_data , 'show_dep':True, 'departments':departments})
    else:
        return redirect('Login')
    

def aad_emp(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        departments = Department.objects.all()
        return render(req,'admindeshboard.html',{'data':a_data , 'aad_emp':True, 'departments':departments})
    else:
        return redirect('Login')
def save_emp(req):
    if 'a_data' in req.session:
        if req.method == 'POST':
            en=req.POST.get('name')
            ec=req.POST.get('contact')
            ee=req.POST.get('email')
            ed=req.POST.get('department')
            eco=req.POST.get('code')
            ei=req.FILES.get('image')
            send_mail(
            "Django Email forwold",
            f'this is informations regarding your company credentials Name:{en}, \nEmail:{ee}, \nContact:{ec},\nDepartment:{ed},\nCode{eco},\nImage{ei}',
            "lakkisahus04@gmail.com",
            [ee],
            fail_silently=False,
        )
            dept=AddEmployee.objects.filter(Email=ee)
            if dept:
               messages.warning(req,'Emploayee already exist')
               a_data= req.session.get('a_data')
               departments = AddEmployee.objects.all()
               return render(req,'admindeshboard.html',{'data':a_data , 'aad_emp':True, 'departments':departments})
            else:
                AddEmployee.objects.create(Name=en,Email=ee,Contact=ec,Images=ei,Code=eco,Departments=ed)
                messages.success(req,'Employee created')
                departments = AddEmployee.objects.all()
                a_data= req.session.get('a_data')
                return render(req,'admindeshboard.html',{'data':a_data , 'aad_emp':True})
    else:
        return redirect('Login')
    
def show_emp(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        departments = AddEmployee.objects.all()
        return render(req,'admindeshboard.html',{'data':a_data , 'show_emp':True, 'departments':departments})
    else:
        return redirect('Login')
    
    

def emp_all_query(req):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        empallquery = Query.objects.all()
        return render(req,'admindeshboard.html',{'data':a_data , 'emp_all_query':True, 'all_query':empallquery})
    else:
        return redirect('Login')
    
def reply(req , pk):
    if 'a_data' in req.session:
        a_data = req.session.get('a_data')
        q_data=Query.objects.get(id=pk)
        emp_all_query=Query.objects.all()
        return render(req, 'admindeshboard.html', {'data':a_data , 'q_data':q_data , 'emp_all_query':emp_all_query} )