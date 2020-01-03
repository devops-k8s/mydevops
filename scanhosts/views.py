from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,HttpResponse
from models import *
import json

def user_info(request):
    ip_addr = request.META['REMOTE_ADDR']
    user_ua = request.META['HTTP_USER_AGENT']

    user_obj = UserIPInfo.object.filter(ip =  ip_addr)
    if not user_obj:
        res = UserIPInfo.object.create(ip = ip_addr)
        ip_add_id = res.id
    else:
        ip_add_id = user_obj[0].id
    BrowseInfo.objects.create(useragent = user_ua,userip_id = ip_add_id)

    result = {"STATUS":"success",
              "INFO":"User info",
              "IP":ip_addr,
              "UA":user_ua}
