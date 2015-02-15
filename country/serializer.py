# __author__ = 'isanka'
from rest_framework import serializers
from authentication.serializers import AccountSerializer
from country.models import Country


class CountrySerializer(serializers.ModelSerializer):
    created_by = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Country

        fields = ('id', 'name', 'created_by', 'dial_code', 'region', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(CountrySerializer, self).get_validation_exclusions()

        return exclusions + ['author']


