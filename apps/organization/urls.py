from django.conf.urls import url, include
from django.urls import path, re_path

from .views import OrgView, AddUserAskView, OrgHomeView

app_name = 'org'

urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),

]
