from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponse,
    HttpRequest,
    HttpResponseRedirect,
    HttpResponseNotFound,
)
from django.urls import reverse_lazy
from .models import Author, Book, Genre, BookInstance
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import AuthorsForm


# @login_required
def index(request: HttpRequest) -> HttpResponse:
    # Генерация количеств некоторых главнвх обьектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'На складе')
    num_instances_available = BookInstance.objects.filter(status=1).count()
    # Авторы книг
    num_authors = Author.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    # Отрисовка HTML-шаблона 'index.html'с данными
    # внутри переменной context
    return render(
        request,
        "index.html",
        context={
            "num_books": num_books,
            "num_instances": num_instances,
            "num_instances_available": num_instances_available,
            "num_authors": num_authors,
            "num_visits": num_visits + 1,
        },

    )


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 8


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 4


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    # queryset = Author.objects.all()
    paginate_by = 4

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Универсальный класс представления списка книг,
    находящихся в заказе у текущего пользователя.
"""
    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status="2").order_by("due_back")

# @login_required
# def authors_add(request: HttpRequest) -> HttpResponse:
#     author = Author.objects.all()
#     authorsform = AuthorsForm()
#     context = {
#         "form": authorsform,
#         "author": author
#     }
#     return render(request, "authors_add.html", context=context)


# # def create(request: HttpRequest) -> HttpResponse:
# #     if request.method == "POST":
# #         author = Author()
# #         author.first_name = request.POST.get("first_name")
# #         author.last_name = request.POST.get("last_name")
# #         author.date_of_birth = request.POST.get("date_of_birth")
# #         author.date_of_death = request.POST.get("date_of_death")
# #         author.save()
# #         return HttpResponseRedirect("catalog/authors_add")
    
# def delete(request: HttpRequest, id: int) -> HttpResponse:
#     try:  
#         author = Author.objects.get(id=id)
#         author.delete()
#         return HttpResponseRedirect("/authors_add/")
#     except Author.DoesNotExist:
#         return HttpResponseNotFound("<h2>Автор не найден</h2>")
    
# def edit1(request: HttpRequest, id: int) -> HttpResponse:
#     author = Author.objects.get(id=id)
#     if request.method == "POST":
#         author.first_name = request.POST.get("first_name")
#         author.last_name = request.POST.get("last_name")
#         author.date_of_birth = request.POST.get("date_of_birth")
#         author.date_of_death = request.POST.get("date_of_death")
#         author.save()
#         return HttpResponseRedirect("/authors_add/")
#     return render(request, "edit1.html", {"author": AuthorsForm})
        
class BookCreate(CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("catalog:book-list")  
    

class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy("catalog:book-list")  
    
    
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("catalog:book-list")
 

class AuthorCreateView(CreateView):
    model =Author
    fields = "__all__"
    success_url = reverse_lazy("catalog:author-list")       
    
    
class AuthorUpdateView(UpdateView):
    model =Author
    fields = "__all__"
    success_url = reverse_lazy("catalog:author-list")   
    
    
class AuthorDeleteView(DeleteView):
    model =Author
    success_url = reverse_lazy("catalog:author-list") 
     