from rest_framework import viewsets

from api.models import Book
from api.serializers import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
