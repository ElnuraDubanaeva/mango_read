from rest_framework.pagination import PageNumberPagination


class MangoReadPagination(PageNumberPagination):
    page_size = 12
