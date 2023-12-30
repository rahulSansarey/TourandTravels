from django.urls import path
from . import views

urlpatterns=[
    path('dummy',views.dummy,),
    path('index',views.index,),
    path('create',views.create_view),
    path('list',views.list_view),
    path('login',views.login,),
    path('contacts',views.contacts_create_view,),
    path('payment',views.payment,),
    
    path('<id>',views.detail_view,),
    path('<id>/update',views.update_view,),
    path('<id>/delete',views.delete_view,),

    
    ]
