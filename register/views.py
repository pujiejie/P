from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .serializers import UsersModelSerializer
from .models import Users


class LoginView(ListModelMixin, GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer

    # def get(self, request):
    #     query_set = Users.objects.all()
    #     serializer = UsersModelSerializer(query_set, many=True)
    #     print(serializer.data)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = UsersModelSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         result = serializer.create(request)
    #         return Response(result, status=200)
