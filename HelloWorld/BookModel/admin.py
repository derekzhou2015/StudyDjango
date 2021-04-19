from django.contrib import admin
from .models import Book, Publisher, Author, AuthorDetail
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',
                    'dis_publisher', 'dis_authors', 'pub_date')
    search_fields = ('title', 'price', 'pub_date',
                     'authors__name', 'publisher__name')

    def dis_publisher(self, obj):
        return obj.publisher.name

    def dis_authors(self, obj):
        return [item.name for item in obj.authors.all()]

    dis_publisher.short_description = 'Publisher'
    dis_authors.short_description = 'Authors'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'email')
    search_fields = ('name', 'city', 'email')


class AuthorDetailInline(admin.StackedInline):
    model = AuthorDetail
    can_delete = False


class AuthorAdmin(admin.ModelAdmin):

    def gender(self, obj): return obj.detail.get_gender_display()
    def tel(self, obj): return obj.detail.tel
    inlines = [AuthorDetailInline]
    list_display = ('name', 'age', 'gender', 'tel')
    search_fields = ('name', 'detail__tel')


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
