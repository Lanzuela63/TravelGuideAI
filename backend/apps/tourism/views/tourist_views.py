from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def explore_spots(request):
    return render(request, 'tourism/explore_spots.html')

@login_required
def saved_spots(request):
    return render(request, 'tourism/saved_spots.html')


