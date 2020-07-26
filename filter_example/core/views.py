from django.shortcuts import render

from django_filters import rest_framework as filters
from rest_framework import generics

from .models import Especialidade, Medico
from .serializers import MedicoSerializer


class MedicoFilterSet(filters.FilterSet):
    especialidade = filters.ModelMultipleChoiceFilter(
        field_name='especialidade', queryset=Especialidade.objects.all()
        # conjoined=True, this parameter make the filter be like an AND operator
    )

    class Meta:
        model = Medico
        fields = ('especialidade',)


class ListMedicos(generics.ListAPIView):
    search_fields = ['nome']
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MedicoFilterSet
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()
