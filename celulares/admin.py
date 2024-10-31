from django.contrib import admin
from .models import Aparelho, NumeroTelefone
from django.db import models 

@admin.register(Aparelho)
class AparelhoAdmin(admin.ModelAdmin):
    list_display = ('nome_dispositivo', 'imei', 'imei_e_sim', 'funcionario', 'numero_cadastrado', 'data_registro')
    search_fields = ('nome_dispositivo', 'imei', 'funcionario')
    list_filter = ('funcionario', 'data_registro')

    # Sobrescreve o método para filtrar números já utilizados, mas mantém o atual na edição
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "numero_cadastrado":
            # Quando estiver editando, incluir o número atualmente associado
            obj_id = request.resolver_match.kwargs.get('object_id')
            if obj_id:
                aparelho = Aparelho.objects.get(pk=obj_id)
                kwargs["queryset"] = NumeroTelefone.objects.filter(
                    models.Q(aparelho__isnull=True) | models.Q(pk=aparelho.numero_cadastrado.pk)
                )
            else:
                kwargs["queryset"] = NumeroTelefone.objects.filter(aparelho__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(NumeroTelefone)
class NumeroTelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    search_fields = ('numero',)
