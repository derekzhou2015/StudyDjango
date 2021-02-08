from django.contrib import admin
from .models import Book, Publisher
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price',
                    'dis_publisher', 'dis_authors', 'pub_date')
    search_fields = ('title', 'price', 'pub_date')

    def dis_publisher(self, obj):
        return obj.publisher.name

    def dis_authors(self, obj):
        return [item.first_name for item in obj.authors.all()]

    dis_publisher.short_description = 'Publisher'
    dis_authors.short_description = 'Authors'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'email')
    search_fields = ('name', 'city', 'email')


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
