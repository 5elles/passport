"""id URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('detail/<slug:slug>', views.PersonDetailView.as_view(), name='person_url'),
    path('document/<slug:slug>', views.DocumentDetailView.as_view(), name='document_url'),
    path('residence/<slug:slug>', views.ResidenceDetailView.as_view(), name='residence_url'),
    path('search', views.SearchPersons.as_view(), name='search_person'),
    path('search/results/', views.SearchResults.as_view(), name='search_results'),
]
