from django.urls import path
from .views import TypeList, TypeDetail

urlpatterns = [
    path('', TypeList.as_view(), name="type"),
    path('type/<int:pk>/', TypeDetail.as_view(), name = "type-detail"),
]
