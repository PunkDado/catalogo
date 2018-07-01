from django.contrib import admin
from .models import Produtos
# Register your models here.


#class ProdutosAdmin(admin.ModelAdmin):
#    list_display = ('nome', 'descricao', 'preco', 'texto_mkt')

admin.site.register(Produtos)
