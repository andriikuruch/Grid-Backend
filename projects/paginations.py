from rest_framework.pagination import PageNumberPagination


class RangedPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'count'
    max_page_size = 100
