from django.contrib import admin
from TestModel.models import Account, AccountDetails

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


class AccountDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tel', 'addr', 'gender', 'birthday')


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountDetails, AccountDetailsAdmin)
