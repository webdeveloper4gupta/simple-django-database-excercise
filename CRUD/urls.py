from django.urls import path
from . import views
# from django.urls import url
# from django.conf.urls import url
from django.urls import include, re_path

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name="create"), 
    path('retrieve',views.retrieve,name="retrieve"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    re_path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
]