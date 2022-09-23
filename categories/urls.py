from django.urls import path
from categories import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
]
