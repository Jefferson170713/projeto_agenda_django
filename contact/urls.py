from django.urls import path # type: ignore

from contact import views

app_name = 'contact'

urlpatterns = [
    path('bootstrap/<int:contact_id>/', views.contact_bootstrap, name='contact_bootstrap'),
    path('bootstrap/', views.index_bootstrap, name='index_bootstrap'),
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
]
