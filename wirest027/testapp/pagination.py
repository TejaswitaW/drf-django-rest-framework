from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'mypage'
    page_size_query_param = 'num'
    max_page_size = 15

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 20 

class CustomCursorPagePagiantion(CursorPagination):
    ordering = '-esal'
    page_size = 5