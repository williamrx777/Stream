from django.db import models

# Create your models here.

class Stream(models.Model):

    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=1000,null=False)


    class Meta:
        db_table ='stream'
        verbose_name='stream'
        verbose_name_plural = 'streams'

    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.nome,
                                       self.url)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.nome,
                                       self.url)

    pass
