"""AllQuotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loginpage, name="login Page"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('addauthor/', views.addauthor, name="addauthor"),
    path('author_delete/<str:pk>', views.author_delete, name="author_delete"),
    path('author_update/<str:pk>', views.author_update, name="author_update"),
    path('addfileauth/', views.addfileauth, name="addfileauth"),
    path('addquotes/', views.addquotes, name="addquotes"),
    path('delete_quotes/<str:pk>', views.delete_quotes, name="delete_quotes"),
    path('quotes_update/<str:pk>', views.quotes_update, name="quotes_update"),
    path('addfilequote/', views.addfilequote, name="addfilequote"),
    path('specialmsg/', views.specialmsg, name="specialmsg"),
    path('spclmsg_delete/<str:pk>', views.spclmsg_delete, name="spclmsg_delete"),
    path('spclmsg_update/<str:pk>', views.spclmsg_update, name="spclmsg_update"),
    path('addcatagories/', views.addcatagories, name="addcatagories"),
    path('catagory_delete/<str:pk>', views.catagory_delete, name="catagory_delete"),
    path('catagory_update/<str:pk>', views.catagory_update, name="catagory_update"),
    path('logout/', views.logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
