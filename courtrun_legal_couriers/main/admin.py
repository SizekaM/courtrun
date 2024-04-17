from django.contrib import admin
from .models import *

#admin.site.register(Order)


@admin.register(SummonOrder)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields=('name', 'order_id', 'email', 'contact')

@admin.register(ServeOrder)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields=('name', 'order_id', 'email', 'contact')


@admin.register(NoticeOrder)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields=('name', 'order_id', 'email', 'contact')


@admin.register(FileOrder)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields=('name', 'order_id', 'email', 'contact') 

@admin.register(CorrespondenceOrder)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields=('name', 'order_id', 'email', 'contact') 


@admin.register(CollectionDropoffOrder)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields=('name', 'order_id', 'email', 'contact') 

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )