from django.urls import path
from . import views

app_name= 'main'
urlpatterns = [
    path('text',views.textsum),
    path('doc',views.docsum),
    path('',views.main),
]
