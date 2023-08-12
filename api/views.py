from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Book
from api.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    This view provides a list
    """
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        if 'title' in request.query_params:
            self.queryset = self.queryset.filter(title__icontains=request.query_params['title'])

        if 'author' in request.query_params:
            self.queryset = self.queryset.filter(author__icontains=request.query_params['author'])

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('Create new books is not allowed')

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        for keys in request.data:
            if keys not in ['title', 'author']:
                return HttpResponseBadRequest('Bad Request, only title and/or author can be changed')

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
