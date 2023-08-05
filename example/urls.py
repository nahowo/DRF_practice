from django.urls import path, include
from .views import HelloAPI, bookAPI, booksAPI, BookAPI, BooksAPI
from .views import BookAPIMixins, BooksAPIMixins
from rest_framework import routers
from .views import BookViewSet

urlpatterns = [
    path('hello/', HelloAPI.as_view()),
    path('fbv/books/',booksAPI),
    path('fbv/book/<int:bid>/',bookAPI),
    path('cbv/books/',BooksAPI.as_view()),
    path('cbv/book/<int:bid>/',BookAPI.as_view()),
    path('mixin/books/',BooksAPIMixins.as_view()),
    path('mixin/book/<int:bid>/',BookAPIMixins.as_view()),
]

router = routers.SimpleRouter()
router.register('books', BookViewSet)
urlpatterns = router.urls