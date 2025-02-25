from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import LiteraryFormat, Book, Author


@admin.register(Book)                          # Вважається більш компактним та читабільним, ніж admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "format", ]  # Це список назв полів моделі, які будуть відображатися у списку
                                                   # записів в адміністративному інтерфейсі.
    list_filter = ["format", ]                   # Це список полів, які використовуються для фільтрації записів
                                                 # у боковій панелі адміністративного інтерфейсу.
    search_fields = ["title", ]                  # Це список полів, за якими здійснюється пошук у
                                                 # адміністративному інтерфейсі.


@admin.register(Author)                       # Реєструє модель Author у Django адміністративному інтерфейсі з
                                              # використанням кастомного класу AuthorAdmin.
class AuthorAdmin(UserAdmin):                 # Вказує, що AuthorAdmin успадковує всі функціональні можливості UserAdmin
                                              # (який використовується для моделі користувачів User у Django) Це означає,
                                              # що всі базові налаштування (наприклад, форми створення, редагування,
                                              # перегляд списків тощо) вже задані, і ми можемо додатково розширити їх.

    list_display = UserAdmin.list_display + ("pseudonym",)    # UserAdmin.list_display містить стандартний набір полів
                                              # (наприклад, username, email, is_staff тощо). + ("pseudonym",) додає нове
                                              # поле pseudonym (псевдонім), яке буде відображатися в таблиці поруч із іншими полями.

    fieldsets = UserAdmin.fieldsets + (("Additional Info", {"fields": ("pseudonym",)}),)   # fieldsets визначає
                                              # структуру форми редагування в адмінці. Поля групуються в секції для кращої організації.
                                              # UserAdmin.fieldsets включає всі стандартні секції для моделі користувача, наприклад:
                                              # Personal info (особиста інформація), Permissions (права доступу), Important dates (важливі дати)
                                              # + (("Additional Info", {"fields": ("pseudonym",)}),) додає нову секцію
                                              # під назвою "Additional Info", яка містить поле pseudonym.

    add_fieldsets = UserAdmin.add_fieldsets + (("Additional Info", {"fields": ("first_name", "last_name", "pseudonym",)}),)
                                              # add_fieldsets визначає структуру форми створення нового запису в Django admin.
                                              # UserAdmin.add_fieldsets включає стандартні секції, такі як:
                                              # Username (ім'я користувача)
                                              # Password (пароль)
                                              # + (("Additional Info", {"fields": ("first_name", "last_name", "pseudonym",)}),)
                                              # додає нову секцію "Additional Info" для форми створення,
                                              # яка дозволяє вводити ім’я (first_name), прізвище (last_name) та псевдонім (pseudonym).


# Як це працює в Django admin:

# Список записів (list_display):
# У таблиці списку авторів відображатимуться стандартні поля користувача плюс нове поле pseudonym.

# Редагування запису (fieldsets):
# У формі редагування буде додана нова секція "Additional Info" із полем для псевдоніма.

# Створення запису (add_fieldsets):
# При створенні нового автора можна буде ввести ім’я, прізвище та псевдонім у спеціальній секції "Additional Info".

admin.site.register(LiteraryFormat)          # Реєструє модель LiteraryFormat в адміністративному інтерфейсі.
                                             # Використовуються стандартні налаштування, тобто відображення та
                                             # функціонал у адміністративній панелі будуть за замовчуванням.

#admin.site.register(Book, BookAdmin)         # Реєструє модель Book з використанням класу BookAdmin, який визначає
                                             # спеціальні налаштування для цієї моделі.
                                             # Завдяки цьому відображення записів у адміністративному інтерфейсі для
                                             # моделі Book включатиме колонки, фільтри, і пошукові поля, налаштовані у BookAdmin.

#admin.site.register(Author, UserAdmin)       # Реєструє модель Author з використанням класу UserAdmin. Використовується
                                             # стандартний UserAdmin, що забезпечує функціонал для керування користувачами
                                             # (або подібними моделями), наприклад, фільтрація за групами, додавання прав доступу, і т. ін.


