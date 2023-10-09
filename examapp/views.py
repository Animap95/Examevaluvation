from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from examapp.models import UserProfile
from django.contrib.auth import login



# Create your views here.


def home(request):

    return render(request, 'home.html')


def custom_login(request):

     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.actype == 'admin':
                login(request, user)
                return redirect('examapp:adminprofile')
            elif user.actype  == 'centers':
                login(request, user)
                return redirect('examapp:centerprofile')
            elif user.actype == 'examiner':
                login(request, user)
                return redirect('examapp:examinerprofile')
        else:
              messages.info(request, "Invalid Username or Password")
              return redirect('examapp:custom_login')
     return render(request,'custom_login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        centername = request.POST['centername']
        actype = request.POST['actype']
        email = request.POST['email']
        branch = request.POST['branch']
        username = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password == cpass:
            if UserProfile.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect("examapp:register")
            elif UserProfile.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('examapp:register')
            else:

                    user= UserProfile.objects.create_user(name=name, centername=centername,actype=actype,
                                                email=email,branch=branch,username=username, password=password)
                    user.save();
                    print("user created")
                    return redirect('examapp:custom_login')
        else:
            messages.info(request, "Passwords not match")
            return redirect('examapp:register')
    return render(request,'register.html')


def centreprofile(request):
    return render(request,'centerprofile.html')


def adminprofile(request):
    return render(request,'Adminprofile.html')

def examinerprofile(request):
    return render(request,'examinerprofile.html')
# @login_required(login_url='/login')
# def form(request):
#     try:
#         user = User.objects.get(id=request.user.id)
#         us = Customer.objects.filter(user=user)
#         if us:
#             messages.info(request, "Form already submitted")
#             return redirect('examapp:profile')
#     except:
#         pass
#
#     if request.method == 'POST':
#         user = User.objects.get(id=request.user.id)
#         print(user)
#         name = request.POST['name']
#         dob = request.POST['dob']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         address = request.POST['address']
#         district = District.objects.get(id=request.POST['district'])
#         branch = Branch.objects.get(id=request.POST['branch'])
#         actype = request.POST['actype']
#         material = request.POST.getlist('material')
#         print(name)
#         print(material)
#         customer = Customer.objects.create(user=user, name=name, dob=dob, age=age, gender=gender, phone=phone,
#                                            email=email,
#                                            address=address, district=district, branch=branch, actype=actype,
#                                            material=material)
#         customer.save()
#         messages.info(request, "Form submitted successfully")
#         return redirect('examapp:profile')
#     return render(request, 'main.html')


# class AjaxHandlerView(View):
#     def get(self, request):
#         dist_id = request.GET.get('district')
#         branch = []
#         if dist_id:
#             print(dist_id)
#             district = District.objects.get(id=dist_id)
#             branch = Branch.objects.filter(district=district)
#         return render(request, 'branch_select.html', {'branch': branch})
#
#
# @login_required(login_url='/login') #profile view only works if loginned otherwise send to login url
# def profile(request):
#     return render(request, 'profile.html')
#

# class ProfileView(LoginRequiredMixin,TemplateView):  # same as above but class view
#     template_name = 'profile.html'
#     # extra_context = {'branch':branch}
#     login_url = '/login'
