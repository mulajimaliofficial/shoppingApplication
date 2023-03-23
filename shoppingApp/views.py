from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from shoppingApp.models import *
from shoppingApp.serializers import *
from shopping.pagination import *


class MyProductView(APIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            instance = self.get_object(pk)
            serializer = self.serializer_class(instance)

        else:

            instance = Product.objects.all()
            serializer = self.serializer_class(instance, many=True,context={"request":request})
            page = self.paginate_queryset(instance)
            if page is not None:
                serializer = self.serializer_class(page, many=True,context={"request":request})
                return self.get_paginated_response(serializer.data)
        return Response({"message": "Records getting successfully.", "data": serializer.data}, status=status.HTTP_200_OK)

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def post(self, request):
        print("Rquest: ",request.data)
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Records updated successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "something went worng", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Records updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "something went worng", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response({"message": "Records deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

