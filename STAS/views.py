from django.shortcuts import render_to_response
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib import auth 
from STAS import models
import numpy as np
import shutil
import time
import cv2
import os
import subprocess as sb

from django.views.generic.base import View
from STAS.models import FORM_IMAGE
from .forms import *

def about(request): 
    return render(request, 'work.html')

def hotel_image_view(request): 
    if request.method == 'POST': 
        form = HotelForm(request.POST , request.FILES) 
        if form.is_valid(): 
            form.save() 
            return redirect('images')
    else: 
        form = HotelForm() 
    return render(request, 'index.html', {'form' : form}) 

  
def success(request): 

    return redirect('success')


def showImg(request): 
    img_detection = FORM_IMAGE.objects.latest('id')
    img_path = img_detection.Pathological_Section.url
    path = '/data/home/mio/makeYOLOv3'
    sb.call('python ' + path +'/one_pic.py -i '+ os.getcwd() + img_path , shell=True)
    if request.method == 'GET': 
        Hotels = FORM_IMAGE.objects.latest('id')
        return render(request, 'work.html', {'Hotels' : Hotels})

