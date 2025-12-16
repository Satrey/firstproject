from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('user/<str:name>/', views.user, name='user'),
#     path('books/', views.books, name='books'),
#     path('book/<int:id>/', views.book, name='book'),
#     path('addbook/', views.addbook, name='addbook'),
#     path('getbook/<str:author>', views.getbook, name='getbook'),
# ]


urlpatterns = [
    path('<name>', views.IndexView.as_view(), name='index'),
    path('newbook/', views.BookCreateView.as_view(), name='newbook'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update'),
<<<<<<< HEAD
    path('delete/<author>', views.BookDeleteView.as_view(), name='delete'),
    
=======
    path('delete/<str:author>', views.BookDeleteView.as_view(), name='delete'),
    path('show/<int:pk>', views.BookDetailView.as_view(), name='show'),
    path('list/', views.BookListView.as_view(), name='list'),
    # path('about/', views.about, name='about'),
    # path('user/<str:name>/', views.user, name='user'),
    # path('books/', views.books, name='books'),
    # path('book/<int:id>/', views.book, name='book'),
    # path('addbook/', views.addbook, name='addbook'),
    # path('getbook/<str:author>', views.getbook, name='getbook'),
>>>>>>> e6668f6 (str238 DRF app created.)
]