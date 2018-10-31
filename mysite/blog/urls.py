from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView 

urlpatterns = [
url(r'^$', views.post_list,name="index"),
#url(r'^registro/', TemplateView.as_view(template_name="blog/Registro.html"),name='registro' ),
#url(r'^index/', TemplateView.as_view(template_name="blog/post_list.html"),name='index' ),

url(r'^registro/',views.registro,name="registro"),

]
