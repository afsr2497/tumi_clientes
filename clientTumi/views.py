from django.shortcuts import render
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from clientTumi.models import ejemploArchivo
from PIL import Image
from .models import inspeccionInformacion
from django.urls import reverse
import requests

# Create your views here.

def index(request):
    if request.method == 'POST':
        infoUsuario = request.POST.get('usuarioInfo')
        infoContra = request.POST.get('contraInfo')
        usrInfo = authenticate(request,username=infoUsuario,password=infoContra)
        if usrInfo is not None:
            login(request,usrInfo)
            return HttpResponseRedirect('dashboard')
        else:
            return HttpResponseRedirect(reverse('clientTumi:index'))
    return render(request,'clientTumi/login.html')

def dashboard(request):
    return render(request,'clientTumi/dashboard.html',{
        'inspecciones_usuario':inspeccionInformacion.objects.all()
    })

def subirArchivos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombreArchivo')
        archivo = request.FILES['archivo']
        print(nombre)
        print(type(archivo))
        ejemploArchivo(nombre=nombre,archivoImg=archivo).save()
    return render(request,'clientTumi/uploadFiles.html')

def descargarArchivos(request):
    return render(request,'clientTumi/downloadFile.html')

def descargarImagen(request,ind):
    print(ind)
    datos_usr = ejemploArchivo.objects.get(id=ind)
    img_usr = Image.open(datos_usr.archivoImg)
    response = HttpResponse()
    response['Content-Type'] = 'image/jpeg'
    response['Content-Disposition'] = 'attachment; filename=usuario.jpeg'
    img_usr.save(response,'jpeg')
    return response

def consultarRequest(request):
    servicioLidar = requests.get('http://127.0.0.1:8080/clientTumi/procesarRequest')
    print(servicioLidar.json())
    return HttpResponseRedirect(reverse('clientTumi:dashboard'))