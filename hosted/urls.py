from django.urls import path
from. import views

app_name = 'hosted'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]