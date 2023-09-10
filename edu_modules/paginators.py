from rest_framework.pagination import PageNumberPagination


class EduModulePaginator(PageNumberPagination):
    page_size = 5
