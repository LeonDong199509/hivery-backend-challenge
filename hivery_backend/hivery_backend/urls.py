"""hivery_backend URL Configuration

"""
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from paranuara_challenge.views import CompanyList, CompanyDetail,CommonFriendView
from paranuara_challenge.views import PersonList, FruitVegView
from django.conf.urls import url,include
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='PARANUARA AP')
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'docs/', schema_view),
    url(r'^api/companies/$', CompanyList.as_view(),name='companies'),
    url(r'^api/companies/(?P<index>[0-9]+)/$',CompanyDetail.as_view(),name='company'),
    url(r'^api/companies/(?P<index>[0-9]+)/employees/$', PersonList.as_view(),name='employees'),
    url(r'^api/common-friends/$', CommonFriendView.as_view(),name = 'common_friends'),
    url(r'^api/people/(?P<index>[0-9]+)/favorite-food/$', FruitVegView.as_view(),name='favorite-food'),
]
