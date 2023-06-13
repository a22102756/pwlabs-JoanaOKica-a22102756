from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
class Author(models.Model):
    firstName = models.CharField(max_length=250, null=False)
    lastName = models.CharField(max_length=250, null=False)
    dateOfBirth = models.DateField(null=False)

    def __str__(self):
        return  self.firstName

class Post(models.Model):
    title = models.CharField(max_length=250, null=False)
    content = models.CharField(max_length=850, null=False)
    createTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.title

class Coment(models.Model):
    comment = models.CharField(max_length=850, null=False)
    createTime = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE, related_name='coments')

    def __str__(self):
        return  self.comment

