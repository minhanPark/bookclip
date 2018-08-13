from django import forms
from betterforms.multiform import MultiModelForm
from .models import Book, Words

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'book_name',)
        labels = {
            'author': "저자",
            'book_name': "책 이름"
        }
        widgets = {
            'book_name': forms.TextInput(attrs={'placeholder': '둘 중 하나만 입력할 시 여기에 입력해주세요.'}),
        }

class WordForm(forms.ModelForm):

    class Meta:
        model = Words
        fields = ('word',)
        labels = {
            'word':"글귀"
        }

class BookWordMultiForm(MultiModelForm):
    form_classes = {
        'book':BookForm,
        'word':WordForm
    }