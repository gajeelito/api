import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Login
import json


from django.http import Http404

# Create your views here.

class LoginView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs, ):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, correo="",contrasenia="" ):
        
        if (correo):
            login= list(Login.objects.filter(correo=correo).values())
            loginb= list(Login.objects.filter(contrasenia=contrasenia).values())
            
            
            if len(login)> 0 and len(loginb)>0:
                loginu = login[0]
                password = loginb[0]
               
                
                
                datos={ 'loginu' : loginu,  }
            else:
                datos={'message' : "usuario o contraseña incorrecta" , }
            return JsonResponse(datos)
        else:
            login=list(Login.objects.values())
            if len(login)>0:
                datos={'message' : "Correcto" , 'login' : login}
            else:
                datos={'message' : "Usuario no encontrado..." , }
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        
        
        
        #print(jd)
        Login.objects.create(correo=jd['email'],nombre=jd['nombre'],contrasenia=jd['pass'])

        datos={'message' : "Usuario registrado;)"}
        return JsonResponse(datos)



    
        


        

    def put(self, request,id):
        jd = json.loads(request.body)
        login= list(Login.objects.filter(id=id).values())
        if len(login) > 0:
            login=Login.objects.get(id=id)
            login.correo=jd['email']
            login.nombre=jd['nombre']
            login.contrasenia=jd['pass']
            login.save()
            datos={'message' : "Datos actualizados!!"}
        else:
            datos={'message' : "Usuario no encontrado..." , }
        return JsonResponse(datos)


    def delete(self, request,id):
        login= list(Login.objects.filter(id=id).values())
        if len(login) > 0:
            Login.objects.filter(id=id).delete()
            datos={'message' : "Usuario Eliminado!!"}
        else:
            datos={'message' : "Usuario no encontrado..." , }
        return JsonResponse(datos)

