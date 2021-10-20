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
    url(r'^$',admin_view.index,name='index'),
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
    url(r'^getfactor/',user_view.getfactor,name='getfactor'),
    url(r'^addAgefactor/',admin_view.addAgefactor,name='addAgefactor'),
    url(r'^agefactorAction/',admin_view.agefactorAction,name='agefactorAction'),
    url(r'^customizeagefactor/',user_view.customizeagefactor,name='customizeagefactor'),
    url(r'^agecustAction/',user_view.agecustAction,name='agecustAction'),
    url(r'^addseason/',admin_view.addseason,name='addseason'),
    url(r'^seasonAction/',admin_view.seasonAction,name='seasonAction'),
    url(r'^adminhome/',admin_view.adminhome,name='adminhome'),
    url(r'^addseasonfactor/',admin_view.addseasonfactor,name='addseasonfactor'),
    url(r'^seasonfactorAction/',admin_view.seasonfactorAction,name='seasonfactorAction'),
    url(r'^addseasoncountryfactorr/',admin_view.addseasoncountryfactor,name='addseasoncountryfactor'),
    url(r'^getfact/',admin_view.getfact,name='getfact'),
    url(r'^countryaction/',admin_view.countryAction,name='countryAction'),
    url(r'^customizeseasoncountryfactor/',user_view.customizeseasoncountryfactor,name='customizeseasoncountryfactor'),
    url(r'^seasonfactAction/',user_view.seasonfactAction,name='seasonfactAction'),
    url(r'^addcontact/',user_view.addcontact,name='addcontact'),
    url(r'^contactAction/',user_view.contactAction,name='contactAction'),
    url(r'^checkusername/',user_view.checkusername,name='checkusername'),
    url(r'^addtoblacklist/',user_view.addtoblacklist,name='addtoblacklist'),
    url(r'^blacklistAction/',user_view.blacklistAction,name='blacklistAction'),
    url(r'^viewcontact/',user_view.viewcontact,name='viewcontact'),
    url(r'^viewblacklist/',user_view.viewblacklist,name='viewblacklist'),
    url(r'^block/(?P<pid>\d+)/$',user_view.block,name='block'),
    url(r'^unblock/(?P<pid>\d+)/$',user_view.unblock,name='unblock'),
    url(r'^trashAction/',user_view.trashAction,name='trashAction'),
    url(r'^viewtrash/',user_view.viewtrash,name='viewtrash'),
    url(r'^deletetrash/(?P<pid>\d+)/$',user_view.deletetrash,name='deletetrash'),
    url(r'^logout/',user_view.logout,name='logout'),
    url(r'^forgotpassword/',user_view.forgotpassword,name='forgotpassword'),
    url(r'^resetpassword/',user_view.resetpassword,name='resetpassword'),
    url(r'^checkAction/',user_view.checkAction,name='checkAction'),
    url(r'^reset/',user_view.reset,name='reset'),
    url(r'^viewspam/',user_view.viewspam,name='viewspam'),
    
    
]

