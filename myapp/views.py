from django.shortcuts import render
from .models import Chirp
from django.http import HttpResponse
import json
import requests

# Create your views here.


def index(request):
	latest_chirp_list = Chirp.objects.all()
	if request.method == 'POST':
		if request.POST.get('chirp_text'):
			new_chirp=Chirp()
			new_chirp.text= request.POST.get('chirp_text')
			new_chirp.save()
			url = 'https://bellbird.joinhandshake-internal.com/push'
			myjson = {'id': 7}
			x = requests.post(url, json = myjson) #don't know how to test if this is working
			print(x.text)
			return render(request, "./myapp/templates/chirps.html", {'chirp_list' : latest_chirp_list}) 
		else:
			for key, value in request.POST.items():
				print('Key: %s' % (key) ) 
				print('Value %s' % (value) )
			chirp_key = request.POST.get('id')
			update_chirp = Chirp.objects.get(id=chirp_key)
			update_chirp.votes += 1
			update_chirp.save()
			print (update_chirp.votes)
			return render(request, "./myapp/templates/chirps.html", {'chirp_list' : latest_chirp_list}) 

	else:
		return render(request, "./myapp/templates/chirps.html", {'chirp_list' : latest_chirp_list})
   
		

