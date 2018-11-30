from django.shortcuts import render, redirect
from django.template import RequestContext
from django.shortcuts import render_to_response
#from mysite.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
#from blog.forms import Registro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.contrib.auth import logout
from .models import Post
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html')  


def registro (request):
    return render(request, 'blog/Registro.html')    

def rescatados (request):
    return render(request,'blog/registrorescatados.html')

def login1 (request):
    return render(request,'blog/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request,'blog/post_list.html')    

#def index(request):
 #   context = {
  #      'posts': Post.objects.order_by('-date')
    #    if request.user.is_authenticated else []
    #}

    #return render(request, 'blog/post_list.html', context)


#def persona_view(request):
   # if request.method == 'POST':
    #    form = Registro(request.POST)            
     #   if form.is_valid():
      #      form.save()
       # return redirect('blog:index')    
   # else: 
    #    form = Registro()
   # return render(request,'blog/Registro.html',{'form':form})    

class RegistrarUsuario(CreateView):
    model = User
    template_name = "blog/Registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('registro')