from rest_framework.pagination import PageNumberPagination


class MangoReadPagination(PageNumberPagination):
    page_size = 12


class CommentReadPagination(PageNumberPagination):
    page_size = 3
