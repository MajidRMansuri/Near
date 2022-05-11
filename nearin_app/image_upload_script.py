# profile image upload
from django.urls import path
from django.db import models
from .models import *
from django.conf import settings
import os
from .views import *

def upload_image(request):
    shop_login = Shop_login.objects.get(Email = request.session['email'])
    shop_profile = Shop_profile.objects.get(Shop_login = shop_login)

    image = request.FILES['shop_image']
    
    image_name = image.name
    image_path = os.path.join(settings.MEDIA_ROOT, 'images/shops')
    images = os.listdir(image_path)

    image_extension = image_name.split('.')[-1]

    new_image_name = f"{shop_profile.id}_{shop_login.Email.split('@')[0]}.{image_extension}"
    image.name = new_image_name

    
    print('image name:', image_name)
    print('new name:', new_image_name)
    print('image path:', images)

    if new_image_name in images:
        os.remove(os.path.join(image_path, new_image_name))

    shop_profile.Avatar = image

    shop_profile.save()

    return redirect(profile_page)
    