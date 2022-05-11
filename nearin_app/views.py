from contextlib import redirect_stderr
from doctest import master
import profile
from random import randint
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.conf import settings
from django.core.mail import send_mail


    
default_data ={
    'app_name' : 'nearin_app',
    'no_header_pages' : ['admin_index','shop_list','about_us','contact_us','change_shop_password','change_password','index','register_page','profile_page','user_profile2','otp_page','index2','login','register','login_user','user_register']
}
#create views for ADMIN
# def shops_profile():
#     default_data['shops_profile'] = Shop_profile.objects.all()

def admin_index(request):
    default_data['current_page'] = 'admin_index'
    return render(request, 'near_admin/index.html',default_data)

def shop_list(request):
    default_data['current_page'] = 'shop_list'
    products()
    return render(request, 'near_admin/shop_list.html',default_data)

# Create your views here.
def index2(request):
    default_data['current_page'] = 'index2'
    return render(request, 'user/login_shop.html',default_data)


def dashboard_page(request):
    default_data['current_page'] = 'dashboard_page'
    return render(request, 'user/dashboard_page.html',default_data)

def profile_page(request):
    default_data['current_page'] = 'profile_page'
    
    shop_data(request) #call the profile data method to collect profile data
    city()
    state()
    return render(request, 'user/profile_page.html',default_data)

def register_page(request):
    default_data['current_page'] = 'register_page'
    return render(request, 'user/register_page.html',default_data)


def otp_page(request):
    default_data['current_page'] = 'otp_page'
    return render(request, 'user/otp_page.html',default_data)


# registration for shops
def shop_profile(request):
    print(request.POST)
    
    request.session['reg_data'] = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }

    create_otp(request)

    return redirect(otp_page)


    # shop_login = Shop_login.objects.create(
    #     Email = request.POST['email'],
    #     Password = request.POST['password'],
    # )
    # profile  = Shop_profile.objects.create(
    #     Shop_login = shop_login,
    # )
    
    # return redirect(index)

# shop profile data
def shop_data(request):
    shop_login = Shop_login.objects.get(Email = request.session['email'])
    shop_profile = Shop_profile.objects.get(Shop_login = shop_login)

    default_data['shop_data'] = shop_profile

# profile image
def shop_image_upload(request):
    shop_login = Shop_login.objects.get(Email = request.session['email'])
    shop_profile = Shop_profile.objects.get(Shop_login = shop_login)
    
    shop_profile.ShopImage = request.FILES['shop_image']
    
    shop_profile.save()
    return redirect(profile_page)

# shop profile update
def shop_update(request):
    shop_login = Shop_login.objects.get(Email = request.session['email'])
    shop_profile = Shop_profile.objects.get(Shop_login = shop_login)

    shop_profile.ShopName = request.POST['shop_name']
    shop_profile.City = request.POST['city']
    shop_profile.State = request.POST['state']
    shop_profile.Contact = request.POST['contact']
    shop_profile.Pincode = request.POST['pincode']
    shop_profile.Address = request.POST['address']
    shop_profile.Delivery = request.POST['delivery']

    shop_profile.save()

    return redirect(profile_page)

def login_shop(request):
    
    print(request.POST)
    try:
        shop_login = Shop_login.objects.get(Email = request.POST['email'])
        if shop_login.Password == request.POST['password']:
            request.session['email'] = shop_login.Email
            return redirect(profile_page)
        else:
            print('incorrect password')
    except Shop_login.DoesNotExist as err:
        print(err)
        return redirect(index)

    # return redirect(profile_page)

def create_otp(request):
    email_to_list = [request.session['reg_data']['email'],]
    subject = "OTP varification By Near.in."
    otp = randint(1000,9999)

    print('OTP is: ', otp)

    request.session['otp'] = otp

    message = f"Your One Time Password for verification is: {otp}"

    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, email_to_list)


# verification
def verify_otp(request):
    otp = int(request.POST['otp'])

    if otp == request.session['otp']:
        shop_login = Shop_login.objects.create(
            Email = request.session['reg_data']['email'],
            Password = request.session['reg_data']['password'],
            IsActive = True,
        )
        
        Shop_profile.objects.create(
            Shop_login = shop_login,
        )

        del request.session['otp']
        del request.session['reg_data']

        print('otp verify success!')

        return redirect(index2)
    else:
        print('invalid otp')

    return redirect(register_page)

# change_shop_password of shop
def change_shop_password(request):
    default_data['current_page'] = 'change_shop_password'
    return render(request, 'user/change_shop_password.html',default_data)

# shop_new_password of shop
def shop_new_password(request):
    shop_login = Shop_login.objects.get(Email = request.session['email'])
    # profile = Profile.objects.get(Master = master)
    shop_login.Password = request.POST['new_pass']
    shop_login.save()
    return redirect(profile_page)

# shop logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']

    return redirect(index2)


# VIEWS FOR CUSTOMER

def index(request):
    default_data['current_page'] = 'index'
    products()
    return render(request, 'index.html',default_data)

# def index(request):
#     default_data['current_page'] = 'index'
#     return render(request, 'index.html',default_data)

def login_user(request):
    default_data['current_page'] = 'login_user'
    return render(request, 'login_user.html',default_data)

def user_register(request):
    default_data['current_page'] = 'user_register'
    return render(request, 'register.html',default_data)

def user_profile(request):
    print(request.POST)
    
    request.session['user_data'] = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }

    create_user_otp(request)

    return redirect(otp)

def otp(request):
    default_data['current_page'] = 'otp_page'
    return render(request, 'otp.html',default_data)


def create_user_otp(request):
    email_to_list = [request.session['user_data']['email'],]
    subject = "OTP varification By Near.in."
    otp = randint(1000,9999)

    print('OTP is: ', otp)

    request.session['otp'] = otp

    message = f"Your One Time Password for verification is: {otp}"

    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, email_to_list)

# verification
def cust_otp(request):
    otp = int(request.POST['otp'])

    if otp == request.session['otp']:
        master = Master.objects.create(
            Email = request.session['user_data']['email'],
            Password = request.session['user_data']['password'],
            IsActive = True,
        )
        
        Profile.objects.create(
            Master = master,
        )

        del request.session['otp']
        del request.session['user_data']

        print('otp verify success!')

        return redirect(login_user)
    else:
        print('invalid otp')

    return redirect(user_register)

def user_login(request):
    
    print(request.POST)
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            return redirect(user_profile2)
        else:
            print('incorrect password')
    except Master.DoesNotExist as err:
        print(err)
        return redirect(login_user)

# def user_profile2(request):
#     default_data['current_page'] = 'user_profile2'
    
#     user_data(request) #call the profile data method to collect profile data
#     city()
#     return render(request, 'profile.html',default_data)

# user profile data
def user_data(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    default_data['user_data'] = profile

# def state_data(request):
#     state = State.objects.get(State = state)
#     default_data['state_data'] = state

# profile image upload
def profile_upload(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    # if 'profile_image' in request.FILES:
    profile.ProfileImage = request.FILES['profile_image']

    profile.save()
    return redirect(user_profile2)

# User PRofile Update

def user_profile_update(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    profile.FullName = request.POST['name']
    profile.City = request.POST['city']
    profile.State = request.POST['state']
    profile.Contact = request.POST['contact']
    profile.Pincode = request.POST['pincode']
    profile.Address = request.POST['address']
    profile.Gender = request.POST['gender']
    profile.DOB = request.POST['dob']

    profile.save()

    return redirect(user_profile2)

# change_password of user
def change_password(request):
    default_data['current_page'] = 'change_password'
    return render(request, 'change_password.html',default_data)
# logout of customer
def logout_user(request):
    if 'email' in request.session:
        del request.session['email']

    return redirect(index)

# new password by user
def new_password(request):
    master = Master.objects.get(Email = request.session['email'])
    # profile = Profile.objects.get(Master = master)
    master.Password = request.POST['new_password']
    master.save()
    return redirect(user_profile2)

# about_us for index page
def about_us(request):
    default_data['current_page'] = 'about_us'
    return render(request, 'about_us.html',default_data)

# Contact us for index page
def contact_us(request):
    default_data['current_page'] = 'contact_us'
    return render(request, 'contact_us.html',default_data)


# State

def state(request):
    default_data['current_page'] = 'user_profile2'
    
    state_data(request) #call the profile data method to collect profile data
    return render(request, 'profile.html',default_data)

# user profile data
def state_data(request):
    # master = Master.objects.get(Email = request.session['email'])
    state = State.objects.get()

    default_data['state_data'] = state

# select data to index page

def user_profile2(request):
    default_data['current_page'] = 'user_profile2'
    
    user_data(request) #call the profile data method to collect profile data
    city()
    state()
    return render(request, 'profile.html',default_data)

# select data of CITY


def city():
    default_data['city_items'] = City.objects.all()

def state():
    default_data['state_items'] = State.objects.all()

def products():
    default_data['product'] = Shop_profile.objects.all()

