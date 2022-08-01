"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path

from inicio import views
from registros import views as views_registros
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros,name="Principal"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('contaco/',views_registros.contacto,name="Contacto"),
    path('eliminarComentario/<int:id>',views_registros.eliminarComentarioContacto,name="Eliminar"),
    path('comentarios/',views_registros.comentarios,name="Comentarios"),

    #CRUD ALUMNOS
    path('eliminarAlumno/<matricula>',views_registros.eliminarAlumno,name="Eliminacion"),
    path("edital/<matricula>/",views_registros.editaral, name="Editaral"),
    path("editaralum/<matricula>/",views_registros.editaralum, name="Editaralu"),
    #CONSULTAS
    path("consultas1",views_registros.consultar1, name="Consultas"),
    path("consultas2",views_registros.consultar2, name="Consultas2"),
    path("consultas3",views_registros.consultar3, name="Consultas3"),
    path("consultas4",views_registros.consultar4, name="Consultas4"),
    path("consultas5",views_registros.consultar5, name="Consultas5"),
    path("consultas6",views_registros.consultar6, name="Consultas6"),
    path("consultas7",views_registros.consultar7, name="Consultas7"),
    
    path("subir",views_registros.archivos, name="Subir"),
    path("seguridad",views_registros.seguridad, name="Seguridad"),

    path('formulario/',views.formulario, name="Formulario"),
    path('ejemplo/',views.ejemplo, name="Ejemplo"),
    path('editarComentario/<int:id>/',views_registros.consultar,name="Consulta"),
    path("edit/<int:id>/",views_registros.editar, name="Editar")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)