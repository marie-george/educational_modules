from edu_modules.apps import EduModulesConfig
from django.urls import path

from edu_modules.views import EduModuleCreateAPIView, EduModuleUpdateAPIView, EduModuleDestroyAPIView, EduModuleRetrieveAPIView, EduModuleListAPIView

app_name = EduModulesConfig.name

urlpatterns = [
    path('create/', EduModuleCreateAPIView.as_view(), name='module_create'),
    path('update/<int:pk>/', EduModuleUpdateAPIView.as_view(), name='module_update'),
    path('delete/<int:pk>/', EduModuleDestroyAPIView.as_view(), name='module_delete'),
    path('<int:pk>/', EduModuleRetrieveAPIView.as_view(), name='module_detail'),
    path('', EduModuleListAPIView.as_view(), name='modules_list')
]
