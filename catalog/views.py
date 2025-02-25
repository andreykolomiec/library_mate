from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import AuthorCreationForm, BookForm, BookSearchForm
from .models import Book, Author, LiteraryFormat


# додамо в нашу ф-цію змінну-лічильник(для підрахунку кількості входжень на нашу сторінку num_visits)
@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()  # кількість книжок
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_literary_formats': num_literary_formats,
        'num_visits': num_visits + 1,
    }
    return render(request, "catalog/index.html", context=context)


# @login_required - підходить до FBV (Function Base Views), але не підходить до Class Base Views
# Для Class Base Views використовуються міксіни (Mixin) В нашему випадку викор. LoginRequiredMixin
# Таким чином ми Ми можемо обмежити доступ неавтентифікованим користувачам,
# застосувавши декоратор login_required до твоєї функції-представлення або
# LoginRequiredMixin — спосіб обмежити доступ у класових представленнях.
# Доступ до цих представлень отримають лише автентифіковані користувачі.

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    queryset = Author.objects.prefetch_related('books')
    paginate_by = 2


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorCreationForm


class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


# Іноді потрібно реалізувати можливість пошуку за певним параметром.
# Для цього потрібно ввести текст для пошуку та створити форму.
# на сторінку Book List нашого сайту,#}
# створимо Search(пошук) книги, додамо кастомні методи до класу BookListView:
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 2

# Також можна додати опцію, щоб введений текст зберігався.
    # Для цього потрібно змінити кастомний метод:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        title = self.request.GET.get('title', "")
        context["title"] = title
        context["search_form"] = BookSearchForm(
            initial={'title': title}
        )
        return context

# реалізація пошуку: Необхідно зробити так: якщо ми передаємо пошукове слово, то queryset фільтрується
    # за цим словом; якщо ні — повертаються всі пости:

    # def get_queryset(self):
    #     title = self.request.GET.get("title")
    #     if title:
    #         return self.queryset.filter(title__icontains=title)
    #     return self.queryset

# Також ти можеш реалізувати такий пошук за допомогою форми:
    def get_queryset(self):
        queryset = Book.objects.select_related("format")
        form = BookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data['title'])
        return queryset





class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class LiteraryFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_confirm_delete.html"
    success_url = reverse_lazy("catalog:literary-format-list")


def test_session_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "<h1>Test Session</h1>"
        f"<h4>Session data: {request.session['book']}</h4>"

    )