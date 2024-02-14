from django.urls import path, re_path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("books/create/", views.BookCreate.as_view(), name="book-create"),
    path("books/update/<int:pk>/", views.BookUpdate.as_view(), name="book-update"),
    path("books/delete/<int:pk>/", views.BookDelete.as_view(), name="book-delete"),
    path("authors/", views.AuthorListView.as_view(), name="author-list"),
    # path("authors_add/", views.authors_add, name="authors_add"),
    # path("create/", views.create, name="create"),
    # path("edit1/<int:id>", views.edit1, name="edit1"),
    # path("delete/<int:id>", views.delete, name="delete"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path("authors/create/", views.AuthorCreateView.as_view(), name="author-create"),
    path("authors/update/<int:pk>/", views.AuthorUpdateView.as_view(), name="author-update"),
    path("authors/delete/<int:pk>/", views.AuthorDeleteView.as_view(), name="author-delete"),
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
]


app_name = "catalog"
