from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('Author/', views.Authors, name="Author"),
    path('Authors/<str:data>', views.Authorss, name="Authors"),
    path('wishes/', views.wishes, name="wishes"),
    path('Catagories/', views.Catagories, name="Catagories"),
    path('Special_days/', views.Special_days, name="days"),
    path('Quotes/<str:name>', views.Quotes, name="Quotes"),
    path('Catagory/<str:type>', views.Catagory, name="Catagory"),
    path('Days/<str:day>', views.Days, name="Days"),
    path('BirthDay/<str:type>', views.BirthDay, name="BirthDay")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
