from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics

from .serializers import LessonSerializer
from .models import lesson
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework.decorators import action


class LessonView(viewsets.ModelViewSet):
    #queryset = lesson.objects.filter(user='sram')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        class_id = self.request.query_params.get('class_id', None)
        lesson_id = self.request.query_params.get('lesson_id', None)
        self.queryset = lesson.objects.filter(user=username,lesson_id=lesson_id,class_id=class_id)
        return self.queryset

    # @action(detail=True, methods=['patch'])
    # def update_record(self, request, *args, **kwargs):
    #
    #     instance = self.queryset
    #     serializer = self.serializer_class(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return self.response(serializer.data)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer