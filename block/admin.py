from django.contrib import admin
from .models import Block


@admin.register(Block)
class ActionAdmin(admin.ModelAdmin):
    list_filter = ('created',)
