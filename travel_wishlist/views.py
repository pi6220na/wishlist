from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, EditPlaceForm


# Create your views here.
def place_list(request):

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')


    places = Place.objects.filter(visited=False)
    new_place_form = NewPlaceForm
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'new_place_form':new_place_form })

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited':visited})

def place_is_visited(request):

    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')

def place_to_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)

    if request.method == "POST":
        form = EditPlaceForm(request.POST, instance=place)
        if form.is_valid():
            print('about to save form')
            placed = form.save(commit=False)
            placed.name = place.name
            placed.visited = place.visited
            placed.review_text = place.review_text
            placed.visited_date = place.visited_date
            placed.save()
            return redirect('edit_detail', pk=place.pk)

        #form = EditPlaceForm(instance=Place)
    #places = Place.objects.filter(visited=False)
    edit_place_form = EditPlaceForm(request.POST, instance=place)

    return render(request, 'travel_wishlist/editlist.html', {'place': place, 'edit_place_form': edit_place_form})


