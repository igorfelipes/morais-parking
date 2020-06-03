from djongo import models

class Veiculo(models.Model):

   
    placa = models.CharField(max_length=7, null=False, unique=True)
    proprietario = models.CharField(max_length=50, null=False, unique=True)
    matricula = models.BigIntegerField(unique=True)
    curso = models.CharField(max_length=50, null=False)
    area_especial = models.BooleanField() 

    def __str__(self):
        return self.proprietario

class Entrada(models.Model):
    SETOR_TYPE_CHOICES = (
        (1, 'setor A Funcionarios'),
        (2, 'setor B Geral'),
        (3, 'setor C Geral'),
        (4, 'setor D Geral'),
    )

    setor_type = models.PositiveSmallIntegerField('Setores',choices=SETOR_TYPE_CHOICES)
    placa = models.CharField(max_length=7, null=False, unique=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

class Evento(models.Model):
    SETOR_TYPE_CHOICES = (
        (1, 'Setor A Funcionarios'),
        (2, 'Setor B Geral'),
        (3, 'Setor C Geral'),
        (4, 'Setor D Geral'),
    )
    evento = models.CharField(max_length=50, null=False, unique=True)
    data = models.DateTimeField()
    setor_type = models.PositiveSmallIntegerField('Setor',choices=SETOR_TYPE_CHOICES) 
    descrição = models.TextField()

class Ocorrencia(models.Model):
    SETOR_TYPE_CHOICES = (
        (1, 'Setor A Funcionarios'),
        (2, 'Setor B Geral'),
        (3, 'Setor C Geral'),
        (4, 'Setor D Geral'),
    )
    OCCURRENCE_TYPE_CHOICES = (
        (1, 'Assalto / Furto'),
        (2, 'Batida / Sinistro'),
        (3, 'Estacionamento Indevido'),
        (4, 'Inundação'),
        (5, 'Dano ao Veiculo'),
    )
    
    placa = models.CharField(max_length=7, null=False, unique=True)
    setor_type = models.PositiveSmallIntegerField('Setor',choices=SETOR_TYPE_CHOICES, null=True) 
    occurrence_type = models.PositiveSmallIntegerField('Motivo da Ocorrencia', choices=OCCURRENCE_TYPE_CHOICES)
    obs = models.TextField('Obersavões')
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

class Vagas(models.Model):
    SETOR_TYPE_CHOICES = (
        (1, 'Setor A Funcionarios'),
        (2, 'Setor B Geral'),
        (3, 'Setor C Geral'),
        (4, 'Setor D Geral'),
    )
    
    vagas_normais = models.IntegerField(null=False)
    vagas_especiais = models.IntegerField(null=False)
    setor_type = models.PositiveSmallIntegerField('Setor',choices=SETOR_TYPE_CHOICES)