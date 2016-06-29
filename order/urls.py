from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^order$',views.order),
    url(r'^redirect$',views.redirect),
]
