from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from home.models import *

def index(request):
    return render_to_response('index.html')

def fakulte(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('fakulteekle.html', c)

def bolum(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('bolumekle.html', c)

def ogrenci(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('ogrenciekle.html', c)

def sorgu(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('ogrencisorgula.html', c)

def ekle(request):
	if(request.POST.get('value') == 'fakulte'):
		Fakulte(name=request.POST.get('fakad')).save()
	elif(request.POST.get('value') == 'bolum'):
		bolumObje = Bolum(name=request.POST.get('bad'))
		Fakulte.objects.get(id=request.POST.get('fakid')).bolum_set.add(bolumObje)
	elif(request.POST.get('value') == 'ogrenci'):
		ogrenciObje = Ogrenci(name=request.POST.get('ad'), surname=request.POST.get('soyad'))
		Bolum.objects.get(id=request.POST.get('bid')).ogrenci_set.add(ogrenciObje)

	return render_to_response('index.html')

def sorgula(request):
	e = Ogrenci.objects.get(id = request.POST.get('soid'))
	return render_to_response('sorgucevap.html')
