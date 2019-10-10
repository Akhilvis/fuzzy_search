from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.fuzzy_search, name='fuzzy-search'),
    # path('autocomplete/', include(app_urls)),
]
