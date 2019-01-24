from django.contrib import admin
from .models import Post

admin.site.register(Post)
admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Blog da Lu'