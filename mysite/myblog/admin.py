from django.contrib import admin
from .models import Irasas, Komentaras


# Register your models here.

class KomentarasInLine(admin.TabularInline):
    model = Komentaras
    extra = 0


class IrasasAdmin(admin.ModelAdmin):
    list_display = ('autorius', 'pavadinimas', 'data')
    inlines = [KomentarasInLine]


class KomentarasAdmin(admin.ModelAdmin):
    list_display = ('irasas', 'autorius', 'data')
    list_editable = ('autorius',)


admin.site.register(Irasas, IrasasAdmin)
admin.site.register(Komentaras, KomentarasAdmin)
