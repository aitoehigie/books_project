from django.urls import path, include
from .views import BookList

app_name = 'book_api'

urlpatterns = [
    path('books', BookList.as_view(), name='books'),
]
