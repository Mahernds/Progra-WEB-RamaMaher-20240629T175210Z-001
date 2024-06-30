from django.shortcuts import render
from .models import Usuario,Genero
# Create your views here.

def index(request):
    usuarios= Usuario.objects.all()
    context={"usuarios": usuarios}
    return render(request, 'alumnos/index.html', context)

def crud(request):
    usuarios=Usuario.objects.all()
    context={'usuarios':usuarios}
    return render (request, 'alumnos/usuarios_list.html',context)



def alumnosAdd(request):
    if request.method is not "POST":
        generos=Genero.objects.all()
        context={"generos":generos}
        return render(request, 'myApp/alumnos_add.html', context)
    
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        
        
        objGenero=Genero.objects.get(id_genero = genero)
        obj=Usuario.objects.create(  rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    )
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request, 'usuarios/usuarios_add.html', context)


def usuarios_del(request,pk):
    context={}
    try:
       usuarios=Usuario.objects.get(rut=pk)

       usuarios.delete()
       mensajes="Bien, Datos eliminados..."
       usuarios=Usuario.objects.all()
       context = {'usuarios':usuarios, 'mensajes': mensajes}
       return render(request, 'usuarios/usuarios_list.html',context)
    except:
        mensajes="Error, rut no existe..."
        usuarios = Usuario.object.all()
        context = {'usuarios': usuarios, 'mensajes':mensajes}
        return render(request, 'usuarios/usuarios_list.html', context)


def usuarios_findEdit(request,pk):
    if pk !="":
        usuario=Usuario.object.get(rut=pk)
        generos=Genero.objects.all()

        print(type(usuario.id_genero.genero))

        context={'usuario':usuario,'generos':generos}
        if usuario:
            return render(request, 'usuarios/usuarios_edit.html',context)
        else:
            context={'mensaje':"Error, rut no existe... "}
            return render(request,'usuarios/usuarios_list.html',context)
        

def usuariosUpdate(request):
    if request.method=="POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)

        usuario = Usuario()
        usuario.rut=rut
        usuario.nombre=nombre
        usuario.apellido_paterno=aPaterno
        usuario.apellido_materno=aMaterno
        usuario.fecha_nacimiento=fechaNac
        usuario.email=email 
        usuario.direccion=direccion
        usuario=activo=1
        usuario.save()

        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados...", 'generos':generos, 'usuario':usuario}
        return render (request, 'usuario/usuarios_findEdit.html', context)
    
    else:
        usuarios=Usuario.objects.all()
        context={'usuarios' :usuarios}
        return render(request, 'usuarios/usuarios_list.html',contex)

