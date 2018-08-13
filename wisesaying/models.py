from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=40, blank=True)
    book_name = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

class Words(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    word = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    def author_is(self):
        return self.book.author

    def book_is(self):
        return self.book.book_name
