from django.urls import include, re_path as url
from snippetsApp import views

urlpatterns=[
    
    url(r'^reference/(?P<Tag>[\w-]+)/$',views.post_item),   # POST request
    url(r'^reference/(?P<Tag>[\w-]+)/(?P<Company>[\w-]+)/$',views.inventory_item)         # GET request
]