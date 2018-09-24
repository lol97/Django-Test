from django.shortcuts import render

def index(request):
	context = {
		'judul' : 'Index',
	}
	
	return render(request,'index.html',context)