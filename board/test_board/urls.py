from django.contrib import admin
from django.urls import path
from test_board.views import post_list

urlpatterns = [
    path('', post_list),
]