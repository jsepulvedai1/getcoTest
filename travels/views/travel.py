from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CategoryTypes, Travel
from django.http.response import Http404
from typing import List


class travelsList(APIView):

    def get_travel(self):
        try:
            return Travel.objects.all()
        except Travel.DoesNotExist:
            raise Http404

    def build_response(self, travels: List[Travel]):
        travels_dict = {}
        for travel in travels:
            info = {
                'name': travel.name,
                'status': travel.status,
                'category': travel.category.name
            }

            if travel.status in travels_dict:
                travels_dict[CategoryTypes(travel.status).name].append(info)
            else:
                travels_dict[CategoryTypes(travel.status).name] = [info]
        return travels_dict

    def get(self, request):

        travels = self.get_travel()
        response = self.build_response(travels)
        return Response(response, status=status.HTTP_200_OK)
