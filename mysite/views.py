from django.shortcuts import render
from msilib.schema import Error
from django.shortcuts import render

from .models import Usuario
from django.shortcuts import render

def inicio(request):
    return render(request,"index.html")

def ingresaru(request):
    return render(request, 'ingresarU.html')

def registrou(request):
    
    msj = None
    user = request.POST['username']
    nameu= request.POST['nombre']
    passu = request.POST['password']
    emailu = request.POST['email']
    perfil = request.POST['perfil']

    try:
        Usuario.objects.create(username=user,nombre=nameu,password=passu, email = emailu, perfil = perfil)
        msj = 'se ha ingresado la persona'
    except Exception as err:
        msj = f'ha ocurrido un problema en la operación_, {err}'
    
    
    return render(request,"respuesta.html",{'msj':msj})


def listarU(request):

    usu = Usuario.objects.all()
    return render(request,"listarU.html",{"usuarios":usu})

def actualizarU(request):
    return render(request,"actualizarU.html", {"formita": "hidden"})

def editarU(request):
    usu = None
    msj = ""
    visibilidad =""
    try:
        usu = Usuario.objects.get(perfil = request.GET["perfil"])
        visibilidad = "visible"
        return render(request, "actualizarU.html", {"formita":visibilidad, "usu":usu})
    except:
        usu = None
    
    if usu == None:
        perfil = None
        try:
            perfil = request.POST["perfil"]
        except:
            perfil = None

        if perfil != None:
            usu = Usuario.objects.get(perfil = perfil)
            nombreu = request.POST["nombre"]
            user = request.POST["username"]
            passu = request.POST["password"]
            emailu = request.POST["email"]
           

            usu.nombre = nombreu
            usu.password = passu
            usu.email = emailu
            usu.username= user
         

            try:
                usu.save()
                msj = "Se ha actualizado "
            except:
                msj = "Se ha ocurrido un error al actualizar "

            visibilidad = "hidden"
            return render(request, "actualizarU.html", {"msj":msj, "formita":visibilidad})
        
        else:
            msj = "No se ha encontrado "
            visibilidad = "hidden"
            return render(request, "actualizarU.html", {"msj":msj, "formita":visibilidad})
    else:
        msj = "No se encontró la persona solicitada"
        visibilidad = "hidden"
        return render(request, "actualizarU.html", {"msj":msj, "formita":visibilidad})



def eliminarU(request):
 return render(request,"eliminarU.html")       

    
def eliminaU(request):
    msj = None
    try:
        perfilu = request.POST['perfil']
        usu = Usuario.objects.get( perfil= perfilu)        
        usu.delete()
        msj = "Eliminado"
        return render(request, "eliminarU.html",{"msj":msj})
    except Exception as ex:
        if str(ex.args).find('does not exist') > 0:
            msj = 'usuario no existe'
        else:
            msj = 'Ha ocurrido un problema'
        
        return render(request,"eliminarU.html", {"msj":msj})    
