from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from shoppingApp.models import *
from shoppingApp.serializers import *
from shopping.pagination import *
from rest_framework import permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token




class CreateAccount(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        reg_serializer = RegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response({"message": "Signup successfully"}, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        params = request.data
        if params["email"] is None or params["password"] is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=params["email"], password=params["password"])
        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "message": "Login Successfully."}, status=status.HTTP_200_OK)



class MyProductView(APIView):
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            instance = self.get_object(pk)
            serializer = self.serializer_class(instance,context={"request":request})

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
        return Response({"message": "Records deleted successfully."}, status=status.HTTP_200_OK)



class ListUsers(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegistrationSerializer

    def get(self, request):
        instance = MyUser.objects.all()
        serializers = self.serializer_class(instance, many=True)
        return Response({"message": "Getting all records.", "data": serializers.data}, status=status.HTTP_200_OK)


class UpdateProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegistrationSerializer

    def put(self, request):
        params = request.data
        print(request.user)
        instance = MyUser.objects.get(email=request.user)
        serializers = self.serializer_class(instance, params, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Profile Updated", "data": serializers.data}, status=status.HTTP_200_OK)
        return Response({"message": "Profile not updated"}, status=status.HTTP_200_OK)  