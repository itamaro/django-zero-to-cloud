from django.contrib import admin

from .models import Pizza, Topping

class ToppingInline(admin.TabularInline):
    model = Topping

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    inlines = [ToppingInline]

admin.site.register(Topping)
