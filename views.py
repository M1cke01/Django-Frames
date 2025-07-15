from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.viewsets import ViewSet
from forms_test.models import Product
from .serializers import ProductSerializer

from .serializers import TestSerializer

class TestAPIView(APIView):
    """API View de Prueba"""
    serializer_class = TestSerializer

    def get(self, request, format=None):
        """Regresa una lista de caracteristias de un APIView"""
        apiview_info = [
            "Usa métodos HTTP como funciones (get, post, patch, put, delete)",
            "Es similar a un Django View tradicional",
            "Te da el mayor control de la lógica de la app",
            "Es mapeado manualmente a los urls"
        ]

        return Response({"message":"Hola", "apiview_info": apiview_info})
    
    def post(self, request):
        """Crea un mensaje con el nombre ingresado"""
        serilizer = self.serializer_class(data=request.data)

        if serilizer.is_valid():
            name = serilizer.validated_data.get("name")
            message = f"Hola {name}!"
            return Response({"message": message})
        else:
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Manejar la actualización de un objeto"""
        return Response({"method":"PUT"})
    
    def patch(self, request, pk=None):
        """Manejar la actualización parcial de un objeto"""
        return Response({"method":"PATCH"})
    
    def delete(self, request, pk=None):
        """Manejar la eliminación de un objeto"""
        return Response({"method":"DELETE"})
    
class TestViewset(ViewSet):
    """Test API Viewset"""
    
    serializer_class = TestSerializer

    def list(self, request):
        """Regresa un listado de caracteristicas de los Viewsets"""
        viewset_info = [
            "Usa acciones (list, create, retrive, update, partial_update, destroy)",
            "Se mapea automaticamente a los urls usando routers",
            "Provee más funcionalidad con menos codigo"
        ]
        return Response({"message":"Hola", "viewset_info":viewset_info})
    
    def create(self, request):
        """Crea un mensaje de saludo"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hola {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """Maneja la consulta de un objeto por su ID"""
        return Response({"method":"GET"})
    
    def update(self, request, pk=None):
        """Maneja la actualizacion de un objeto por su ID"""
        return Response({"method":"PUT"})
    
    def partial_update(self, request, pk=None):
        """Maneja la actualizacion parcial de un objeto por su ID"""
        return Response({"method":"PACTH"})
    
    def destroy(self, request, pk=None):
        """Maneja la eliminación de un objeto por su ID"""
        return Response({"method":"DELETE"})
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)