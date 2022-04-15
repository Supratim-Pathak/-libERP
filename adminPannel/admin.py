from pyexpat import model
from django.contrib import admin
from wcwidth import list_versions
from adminPannel.models import books_info
from adminPannel.models import stu_info
# Register your models here.

@admin.register(books_info)
class bookInfo(admin.ModelAdmin):
    list_display = ('book_id', 'book_name', 'author', 'isbn_no')

@admin.register(stu_info)
class stuinfoAdmin(admin.ModelAdmin):
    list_display = ('stu_name','stu_roll')


