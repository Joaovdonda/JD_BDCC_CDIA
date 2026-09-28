from django.db import models


class Talhao(models.Model):
    STATUS_CHOICES = [
        ('APROVADO', 'Aprovado'),
        ('REVISAO', 'Revisão'),
        ('BLOQUEADO', 'Bloqueado'),
    ]

    identificador = models.CharField(max_length=50, unique=True)
    produtor = models.CharField(max_length=200)
    fazenda = models.CharField(max_length=200)
    geojson = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='REVISAO')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.identificador} - {self.fazenda}'


class Lote(models.Model):
    STATUS_CHOICES = [
        ('APROVADO', 'Aprovado'),
        ('SUSPEITO', 'Suspeito'),
        ('BLOQUEADO', 'Bloqueado'),
    ]

    talhao = models.ForeignKey(Talhao, on_delete=models.CASCADE, related_name='lotes')
    codigo = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='SUSPEITO')
    motivo = models.TextField(blank=True)
    data_recepcao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codigo
