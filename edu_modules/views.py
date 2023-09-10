from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from edu_modules.models import EduModule
from edu_modules.paginators import EduModulePaginator
from edu_modules.serializers import EduModuleSerializer


class EduModuleCreateAPIView(generics.CreateAPIView):
    serializer_class = EduModuleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_module = serializer.save()
        new_module.owner = self.request.user
        new_module.save()


class EduModuleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = EduModuleSerializer
    queryset = EduModule.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return EduModule.objects.none()
        else:
            user = self.request.user
            return EduModule.objects.filter(owner=user)


class EduModuleDestroyAPIView(generics.DestroyAPIView):
    queryset = EduModule.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return EduModule.objects.none()
        else:
            user = self.request.user
            return EduModule.objects.filter(owner=user)


class EduModuleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EduModuleSerializer
    queryset = EduModule.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return EduModule.objects.none()
        else:
            user = self.request.user
            return EduModule.objects.filter(owner=user)


class EduModuleListAPIView(generics.ListAPIView):
    serializer_class = EduModuleSerializer
    queryset = EduModule.objects.all()
    pagination_class = EduModulePaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return EduModule.objects.none()
        else:
            user = self.request.user
            return EduModule.objects.filter(owner=user)
