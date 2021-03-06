from django.urls import path, include
from rest_framework.routers import DefaultRouter
from phonebooks_api import views


router = DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.PhonebookViewSet)
router.register('phonebooks', views.UsersPhonebookViewSet)

urlpatterns=[
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UsersLoginApiView.as_view()),
    path('',include(router.urls))

]
