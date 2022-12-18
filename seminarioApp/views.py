from django.shortcuts import render,redirect
from .serializers import InscritoSerializer
from .models import Inscrito
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from seminarioApp.models import Inscrito
from seminarioApp.forms import FormReserva 
from django.http import JsonResponse

##########
#API REST#
##########
def verinscritosapi(request):
    inscritos = Inscrito.objects.all()
    data = {'inscritos': list(inscritos.values('nombre', 'telefono', 'fecha', 'institucion', 'hora', 'estado', 'observacion'))}
    return JsonResponse(data)

######
#CRUD#
######
def index (request):
    return render(request, 'index.html')

def reservas (request):
    reservas = Inscrito.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarreserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregar.html', data)

def editarreserva(request, id):  
    reserva = Inscrito.objects.get(id=id)
    form = FormReserva(instance=reserva)
    if request.method == "POST":  
        form = FormReserva(request.POST, instance=reserva)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/reservas')  
            except Exception as e: 
                pass    
    return render(request,'agregar.html',{'form':form}) 

def eliminarreserva(request, id):
    reserva = Inscrito.objects.get(id = id)
    try:
        reserva.delete()
    except:
        pass
    return redirect('/reservas')

#################
#CLASS BASE VIEW#
#################

class ListaInscrito(APIView):
    def get(self, request):
        inscrito = Inscrito.objects.all()
        serial = InscritoSerializer(inscrito, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritoSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleInscrito(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(id=pk)
        except Inscrito.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscrito = self.get_object(pk)
        serial = InscritoSerializer(inscrito)
        return Response(serial.data)

    def put(self, request, pk):
        inscrito = self.get_object(pk)
        serial = InscritoSerializer(inscrito, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscrito = self.get_object(pk)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



####################
#FUNCTION BASE VIEW#
####################

@api_view(['GET', 'POST'])
def listar_inscritos(request):
    if request.method == 'GET':
        persona = Inscrito.objects.all()
        serial = InscritoSerializer(persona, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InscritoSerializer(data = request.data)
        if serial.is_valid() :
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def inscrito_detalle(request, pk):
    try:
        inscrito = Inscrito.objects.get(pk=pk)
    except Inscrito.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InscritoSerializer(inscrito)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InscritoSerializer(inscrito, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)