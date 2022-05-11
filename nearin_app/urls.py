from django.urls import path
from .views import *



urlpatterns = [
    path('', index),
    path('admin_index/', admin_index, name='admin_index'),
    path('shop_list/', shop_list, name='shop_list'),
    path('dashboard_page/', dashboard_page, name='dashboard_page'),
    path('profile_page/', profile_page, name='profile_page'),
    path('shop_profile/', shop_profile, name='shop_profile'),
    path('register_page/', register_page, name='register_page'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('otp_page/', otp_page, name='otp_page'),
    path('shop_image_upload/', shop_image_upload, name='shop_image_upload'),
    path('shop_update/', shop_update, name='shop_update'),
    path('logout/', logout, name='logout'),
    path('login_shop/', login_shop, name='login_shop'),
    path('index2/', index2, name='index2'),
    path('index/', index, name='index'),
    path('login_user/', login_user, name='login_user'),
    path('user_register/', user_register, name='user_register'),
    path('user_profile/', user_profile, name='user_profile'),
    path('otp/', otp, name='otp'),
    path('about_us/', about_us, name='about_us'),
    path('contact_us/', contact_us, name='contact_us'),
    path('shop_new_password/', shop_new_password, name='shop_new_password'),
    path('change_shop_password/', change_shop_password, name='change_shop_password'),
    path('cust_otp/', cust_otp, name='cust_otp'),
    path('create_user_otp/', create_user_otp, name='create_user_otp'),
    path('user_login/', user_login, name='user_login'),
    path('user_profile2/', user_profile2, name='user_profile2'),
    path('profile_upload/', profile_upload, name='profile_upload'),
    path('change_password/', change_password, name='change_password'),
    path('logout_user/', logout_user, name='logout_user'),
    path('new_password/', new_password, name='new_password'),
    path('user_profile_update/', user_profile_update, name='user_profile_update'),

    
    # path('login/', login, name='login'),
    # path('register/', register, name='register'),
    # path('otp/', otp, name='otp'),
    # path('registration/', registration, name='registration'), 
    # path('user_login/', user_login, name='user_login'), 
    # path('profile/', profile, name='profile'), 
    # path('verify_otp2/', verify_otp2, name='verify_otp2'),
    # path('shop_login/', shop_login, name='shop_login'),
]