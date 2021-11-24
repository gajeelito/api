from django.urls import path

from .views import LoginView

urlpatterns=[
    path('login/',LoginView.as_view(),name='login_list'),
    path('login/<int:id>',LoginView.as_view(),name='login_list'),
    path('login/<str:correo>/<str:contrasenia>',LoginView.as_view(),name='login_list'),
    
]