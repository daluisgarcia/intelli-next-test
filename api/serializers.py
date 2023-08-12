from rest_framework import serializers

from api.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        read_only_fields = ('isbn', 'year_of_publication', 'publisher', 'image_url_s', 'image_url_m', 'image_url_l')
        fields = ('isbn', 'title', 'author', 'year_of_publication', 'publisher', 'image_url_s', 'image_url_m', 'image_url_l')
