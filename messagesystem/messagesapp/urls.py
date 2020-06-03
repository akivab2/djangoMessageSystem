from django.urls import path, include
from . import views


urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('messages/', views.message_list),
    path('messages/<int:pk>/', views.message_detail),
    path('messages/unread/', views.unread_message_list),
    path('messages/user/<int:pk>/', views.specific_user_message_list),
    path('messages/user/unread/<int:pk>/', views.unread_specific_message_list)
]
