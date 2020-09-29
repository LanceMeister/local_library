from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
# Define the admin class

# Register the admin class with the associated model


class BookInline(admin.TabularInline):
    model = Book

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.book_set.count()
        return extra


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')

    inlines = [BookInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.bookinstance_set.count()
        return extra
# Register the Admin classes for Book using the decorator


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre',)
    inlines = [BooksInstanceInline]
# Register the Admin classes for BookInstance using the decorator


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ( 'book', 'imprint', 'status','borrower','due_back','id')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower' )
        }),
    )


admin.site.register(Genre)

admin.site.register(Language)
