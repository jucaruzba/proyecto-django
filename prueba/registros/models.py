from operator import mod
from statistics import mode
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField


class Alumnos(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12, verbose_name="Matricula") #Texto corto
    nombre = models.TextField() #Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen=models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        ordering=["-created"] #Este elemento indica que se ordernara del más recienre al ,mas viejo

    def __str__(self):
        return self.nombre #Indica que se mostrare el nombre en la tabla 

class Comentario(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    alumno=models.ForeignKey(Alumnos,
        on_delete=models.CASCADE, verbose_name="Alumno")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    coment=RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"
        ordering=["-created"]

    def __str__(self):
        return self.coment


class ComentarioContacto(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    usuario=models.TextField(verbose_name="Usuario")
    mensaje=models.TextField(verbose_name="Comentario")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name="Comentario Contacto"
        verbose_name_plural="Comentarios Contactos"
        ordering=["-created"]

    def __str__(self):
        return self.mensaje

class Archivos(models.Model): #Define la estructura de nuestra tabla
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    titulo= models.CharField(max_length=12, verbose_name="Titulo") #Texto corto
    descripcion=models.CharField(max_length=12, verbose_name="Descripcion")
    archivo=models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Archivo"
        verbose_name_plural="Archivos"
        ordering=["-created"]

    def __str__(self):
        return self.archivo

