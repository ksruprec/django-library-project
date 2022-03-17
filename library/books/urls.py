from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book_list'), #homepage
    path('<int:book_id>', views.book_view, name='book_view'), #read book details
    path('new', views.book_create, name='book_new'), #create new book object
    path('edit/<int:book_id>', views.book_update, name='book_edit'), #update book
    path('delete/<int:book_id>', views.book_delete, name='book_delete'), #delete book
]