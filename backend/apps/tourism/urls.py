#apps/tourism/urls.py
from django.urls import path

from apps.tourism.views.main_views import (
    TouristSpotListCreateView, TouristSpotDetailView,
    CategoryListCreateView, CategoryDetailView,
    LocationListCreateView, LocationDetailView,
    ReviewListCreateView, ReviewDetailView,
    GalleryListCreateView, GalleryDetailView,
    OperatingHourListCreateView, OperatingHourDetailView,
    TouristSpotFullDetailView, public_home,
)
from apps.tourism.views import main_views
from apps.tourism.views.main_views import review_spots
from apps.tourism.views.api_views import TouristSpotListAPIView, list_tourist_spots

app_name = "tourism"

urlpatterns = [

    path('tourist-spots/', TouristSpotListAPIView.as_view()),
    path('spots/', TouristSpotListCreateView.as_view(), name='spot-list-create'),
    path('spots/<int:pk>/', TouristSpotDetailView.as_view(), name='spot-detail'),
    path('spots/<int:pk>/full/', TouristSpotFullDetailView.as_view(), name='spot-full-detail'),

    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    path('galleries/', GalleryListCreateView.as_view(), name='gallery-list-create'),
    path('galleries/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),

    path('hours/', OperatingHourListCreateView.as_view(), name='operatinghour-list-create'),
    path('hours/<int:pk>/', OperatingHourDetailView.as_view(), name='operatinghour-detail'),
    path('', public_home, name='public-home'),

    path('spots/<int:pk>/view/', main_views.spot_detail_view, name='spot-detail-view'),

    path('explore/', main_views.explore_spots, name='explore_spots'),
    path('saved/', main_views.saved_spots, name='saved_spots'),
    path('review/', review_spots, name='review_spots'),
    path('reports/', main_views.reported_spots, name='reported_spots'),

    #path('review/', main_views.review_submissions, name='review_submissions'),  # if needed
]
