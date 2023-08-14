from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('eventdetails', views.eventinfo, name='eventdetails' ),
    path('', views.eventhome, name="home"),
    # path('getmail/', views.getmail, name='getmail'),
    path('thanks/', views.thankyou, name='thanks'),
    path('sendemail/', views.sendemail, name='sendemail'), 
    path('emailbutton', views.emailbutton, name='emailbutton')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
