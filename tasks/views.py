from rest_framework import generics
from tasks.models import Task
from .serializers import UserSerializer,TaskSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny


# register view
class Registerview(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# task creation view
class TaskListCreatView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(User=self.request.user)       