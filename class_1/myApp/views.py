from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer
from .models import user_register

@api_view(['GET', 'POST'])
def user_register_view(request):
    if request.method == 'GET':
        users = user_register.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        print(serializer.data)  # Print serializer data for debugging
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

