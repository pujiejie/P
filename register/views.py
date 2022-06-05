from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsersModelSerializer
from .models import Users


class LoginView(APIView, CreateModelMixin):

    def get(self, request):
        query_set = Users.objects.all()
        serializer = UsersModelSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            result = serializer.create()
            return Response(result, status=200)

