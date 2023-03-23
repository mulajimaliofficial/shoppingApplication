from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math
from rest_framework import status
## you can override page_size, max_page_size from url query params \
## to make it more dynamic
class CustomPagination(PageNumberPagination):
    page_size = 1 # default page size
    max_page_size = 1000 # default max page size
    page_size_query_param = 'page_size' # if you want to dynamic items per page from request you must have to add it 
      
    def get_paginated_response(self, data):
        # if you want to show page size in resposne just add these 2 lines
        if self.request.query_params.get('page_size'):
            self.page_size = int(self.request.query_params.get('page_size'))
            
        # you can count total page from request by total and page_size
        total_page = math.ceil(self.page.paginator.count / self.page_size)
        
        # here is your response
        return Response({
            'message':"Records getting successfully",
            'count': self.page.paginator.count,
            'total': total_page,
            'page_size': self.page_size,
            'current': self.page.number,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'results': data
        }, status=status.HTTP_200_OK)