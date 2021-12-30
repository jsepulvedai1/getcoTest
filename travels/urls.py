from django.urls import path
from travels.views import user_travel, travel, register
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path(
        'user_travels/<int:user_id>/',
        user_travel.UserTraveInfo.as_view(),
        name='user_travels'
    ),
    path(
        'list_travels',
        travel.travelsList.as_view(),
        name='list_travels'
    ),
    path(
        'register',
        register.RegisterUser.as_view(),
        name='register'
    ),
    path(
        'auth/login',
        obtain_jwt_token,
        name='obtain_jwt_token'
    ),
    path(
        'user_travels/<int:user_id>/categories<int:category_id>',
        user_travel.UserTravelforCategory.as_view(),
        name='verify_jwt_token'
    )
]
