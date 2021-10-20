"""spam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Admin import views as admin_view
from User import views as user_view
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',admin_view.index),
    url(r'^login/',admin_view.login,name='login'),
    url(r'^loginAction/',admin_view.loginAction,name='loginAction'),
    url(r'^home/',user_view.home,name='home'),
    url(r'^addHobby/',admin_view.addHobby,name='addHobby'),
    url(r'^hobbyAction/',admin_view.hobbyAction,name='hobbyAction'),
    url(r'^register/',user_view.register,name='register'),
    url(r'^getstate/',user_view.getstate,name='getstate'),
    url(r'^registerAction/',user_view.registerAction,name='registerAction'),
    url(r'^sendmessage/',user_view.sendmessage,name='sendmessage'),
    url(r'^messageAction/',user_view.messageAction,name='messageAction'),
    url(r'^viewmessage/',user_view.viewmessage,name='viewmessage'),
    url(r'^outbox/',user_view.outbox,name='outbox'),
    url(r'^deletemessage/(?P<pid>\d+)/(?P<r>\d+)/$',user_view.deletemessage,name='deletemessage'),
    url(r'^forward/(?P<pid>\d+)/$',user_view.forward,name='forward'),
    url(r'^forwardAction/',user_view.forwardAction,name='forwardAction'),
    url(r'^reply/(?P<pid>\d+)/$',user_view.reply,name='reply'),
    url(r'^update/',user_view.update,name='update'),
    url(r'^updateAction/',user_view.updateAction,name='updateAction'),
    url(r'^addHobbyfactor/',admin_view.addHobbyfactor,name='addHobbyfactor'),
    url(r'^factorAction/',admin_view.factorAction,name='factorAction'),
    url(r'^customize/',user_view.customize,name='customize'),
    url(r'^customizeAction/',user_view.customizeAction,name='customizeAction'),
    
    

    
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
