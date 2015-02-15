from django.shortcuts import render
from rest_framework import viewsets, permissions
#from rest_framework.response import Response


from country.models import Country
from country.permissions import IsCountryOwner
from country.serializer import CountrySerializer


class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsCountryOwner())

    def perform_create(self, serializer):
        instance = serializer.save(created_by=self.request.user)

        return super(CountryViewset, self)
        perform_create(serializer)