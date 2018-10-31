from django.shortcuts import render, redirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from mysite.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
#from blog.forms import Registro

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html')  


def registro (request):
    return render(request, 'blog/Registro.html')    


#def persona_view(request):
   # if request.method == 'POST':
    #    form = Registro(request.POST)            
     #   if form.is_valid():
      #      form.save()
       # return redirect('blog:index')    
   # else: 
    #    form = Registro()
   # return render(request,'blog/Registro.html',{'form':form})    