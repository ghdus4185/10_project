from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/review_create', views.review_create, name="review_create"),
    path('<int:review_id>/review_delete/<int:movie_id>/', views.review_delete, name="review_delete"),
    path('<int:id>/like/', views.like, name='like')
]
