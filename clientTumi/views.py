from django.shortcuts import render
from django.http import FileResponse, HttpResponse

from clientTumi.models import ejemploArchivo
from PIL import Image

# Create your views here.

def index(request):
    return HttpResponse('Hola Tumi')

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