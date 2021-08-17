
from django.contrib import admin
from django.urls import path
from .views import adminloginview,userorders,deliveryboy,adminorders,declineorder,acceptorder,adminhomepageview,authenticateadmin,placeorder,userauthenticate,userlogout,customerwelcomeview,userloginview,logoutadmin,addpizza,signupuser,deletepizza,homepageview

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('admin/',adminloginview, name='adminloginpage'),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepageview,name='adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('addpizza/',addpizza),
    path('deletepizza/<int:pizzapk>/',deletepizza),
    path('',homepageview, name='homepage'),
    path('signupuser/',signupuser),
    path('loginuser/',userloginview, name='userloginpage'),
    path('customer/welcome/',customerwelcomeview, name='customerpage'),
    path('customer/authenticate/',userauthenticate),
    path('userlogout/',userlogout),
    path('placeorder/',placeorder),
    path('userorders/',userorders),
    path('adminorders/',adminorders),
    path('acceptorder/<int:orderpk>/',acceptorder),
    path('declineorder/<int:orderpk>/',declineorder),
    path('deliveryboy/',deliveryboy),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_URL}),
]
#  urlpatterns = urlpatterns+static(settings.M)