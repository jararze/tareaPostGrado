from django.contrib import admin
from .models import Causa, Donacion, Usuario, Categoria, Comentario


admin.site.register(Causa)
admin.site.register(Donacion)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Comentario)


# @admin.register(Categoria)
# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = ['nombre', 'descripcion']
#     search_fields = ['nombre']
#
# @admin.register(Causa)
# class CausaAdmin(admin.ModelAdmin):
#     list_display = ['titulo', 'monto_objetivo', 'activa', 'categoria']
#     list_filter = ['activa', 'categoria']
#     search_fields = ['titulo', 'descripcion']