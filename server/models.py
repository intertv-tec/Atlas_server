from django.db import models

class Automation(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    last_ping = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=100,blank=True)

    def __str__(self):
        if self.is_active:
            return f'{self.name} 🟢'  # Retorna o nome seguido de um emoji verde se ativo
        else:
            return f'{self.name} 🔴'  # Retorna o nome seguido de um emoji vermelho se inativo
