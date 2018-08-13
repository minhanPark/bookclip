from django.contrib import admin
from .models import Book, Words

admin.site.register(Book)
# admin.site.register(Words)
@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ('word', 'book_is', 'author_is')
    fieldsets = (
        ('책', {
            'fields': ('book',)
        }),
        ('문장',{
            'fields':('word',)
        })
    )
