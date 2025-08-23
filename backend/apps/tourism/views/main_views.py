#apps/tourism/views/main_views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.tourism.models import Spot
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.tourism.models import (
    TouristSpot, Category, Location, Review, Gallery, OperatingHour
)
from apps.tourism.serializers import (
    TouristSpotSerializer, CategorySerializer, LocationSerializer,
    ReviewSerializer, GallerySerializer, OperatingHourSerializer,
    TouristSpotDetailSerializer
)
from apps.tourism.filters import TouristSpotFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly


## --- Tourist Spot Views ---
class TouristSpotListCreateView(generics.ListCreateAPIView):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TouristSpotFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']


class TouristSpotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer


class TouristSpotFullDetailView(generics.RetrieveAPIView):
    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotDetailSerializer


# --- Category Views ---
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# --- Location Views ---
class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


# --- Review Views ---
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# --- Gallery Views ---
class GalleryListCreateView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


# --- Operating Hour Views ---
class OperatingHourListCreateView(generics.ListCreateAPIView):
    queryset = OperatingHour.objects.all()
    serializer_class = OperatingHourSerializer


class OperatingHourDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OperatingHour.objects.all()
    serializer_class = OperatingHourSerializer


def public_home(request):
    featured_spots = TouristSpot.objects.filter(is_featured=True)
    return render(request, 'home/index.html', {
        'featured_spots': featured_spots
    })

def tourist_dashboard(request):
    spots = TouristSpot.objects.all()
    return render(request,
                  'dashboards/tourist_dashboard.html', {'spots': spots})

def explore_spots(request):
    search_query = request.GET.get('search', '')
    if search_query:
        spots = TouristSpot.objects.filter(name__icontains=search_query) | TouristSpot.objects.filter(location__name__icontains=search_query)
    else:
        spots = TouristSpot.objects.all()
    return render(request, 'tourism/explore_spots.html', {'spots': spots, 'search_query': search_query})

def saved_spots(request):

    return render(request, 'tourism/saved_spots.html')

@login_required
def review_spots(request):
    # Placeholder logic (you can replace with actual review handling)
    return render(request, "tourism/review_spots.html", {})

from django.shortcuts import render, get_object_or_404

@login_required
def spot_detail_view(request, pk):
    spot = get_object_or_404(TouristSpot, pk=pk)
    return render(request, 'tourism/spot_detail.html', {'spot': spot})

@login_required
def reported_spots(request):
    return render(request, "tourism/reported_spots.html")

def reported_spots(request):
    query = request.GET.get('query', '')  # Get the search query from the URL
    if query:
        # Filter spots by name (case-insensitive search)
        spots = Spot.objects.filter(name__icontains=query)  # This filters by name field
    else:
        # If no query, return all spots
        spots = Spot.objects.all()

    return render(request, 'tourism/reported_spots.html', {'spots': spots, 'query': query})
