from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Travel
from django.http.response import Http404
from typing import List


class UserTraveInfo(APIView):

    def get_travel(self, user_id: int):
        try:
            return Travel.objects.filter(user_id=user_id)
        except Travel.DoesNotExist:
            raise Http404

    def build_response(self, travels: List[Travel]):
        data = []
        for travel in travels:
            travel = {
                'id': travel.pk,
                'name': travel.name,
                'status': travel.status,
                'travel_category': travel.category.name
            }
            data.append(travel)
        return data

    def get(self, request, user_id: int):
        travels = self.get_travel(user_id)
        response = self.build_response(travels)
        return Response(response, status=status.HTTP_200_OK)


class UserTravelforCategory(APIView):

    def __get_user_travel_category(self, user_id: int, category_id: int):
        try:
            return Travel.objects.filter(user_id=user_id, category_id=category_id)
        except Travel.DoesNotExist:
            raise Http404

    def build_response(self, travels: List[Travel]):
        data = []
        for travel in travels:
            travel = {
                'id': travel.pk,
                'user_id': travel.user_id,
                'name': travel.name,
                'status': travel.status,
                'travel_category': travel.category.name
            }
            data.append(travel)
        return data

    def get(self, request, user_id, category_id):
        travels = self.__get_user_travel_category(user_id, category_id)
        response = self.build_response(travels)
        return Response(response, status=status.HTTP_200_OK)
