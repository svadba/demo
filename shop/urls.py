from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^city/(?P<slug>[-\w]+)/$', views.ProductCityList.as_view(), name='city'),
    # url(r'^category/(?P<slug>[-\w]+)/$', views.ProductCityList.as_view()),
    # url(r'^$', views.ProductCityList.as_view()),
    # url(r'^$', views.ProductList, name='ProductList'),
    # url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),

]




# url(r'^$', views.ProductCityList.as_view()),
# url(r'^city/(?P<city_slug>[-\w]+)/$', views.ProductCityList.as_view()),
# url(r'^(?P<slug>[-\w]+)/$', views.ProductCityList.as_view(), name='citylist'),
# url(r'^(?P<slug>[-\w]+)/$', views.ProductCityList.as_view(), name='categorylist'),
# url(r'^city1/(?P<slug>[-\w]+)/$', views.CityListView.as_view(), name='City'),
# url(r'^city1/(?P<slug>[-\w]+)/$', views.CityListView.as_view(), name='Category'),
# url(r'^city1/page(?P<page>\d+)/$', views.CityListView.as_view()),
