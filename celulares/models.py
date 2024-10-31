from django.db import models

class NumeroTelefone(models.Model):
    numero = models.CharField(max_length=15, unique=True, help_text="Número de telefone cadastrado")
    
    def __str__(self):
        return self.numero

class Aparelho(models.Model):
    funcionario = models.CharField(max_length=100, help_text="Nome do funcionário com o aparelho")
    imei = models.CharField(max_length=15, unique=True, help_text="Número IMEI do aparelho")
    imei_e_sim = models.CharField(max_length=15, unique=True, help_text="Número IMEI(eSIM) do aparelho", null=True)
    numero_cadastrado = models.OneToOneField(NumeroTelefone, on_delete=models.CASCADE, help_text="Número de telefone cadastrado no aparelho")
    nome_dispositivo = models.CharField(max_length=100, help_text="Nome ou modelo do dispositivo")
    data_registro = models.DateTimeField(auto_now_add=True, help_text="Data de registro")

    def __str__(self):
        return f'{self.nome_dispositivo} - {self.imei}'
