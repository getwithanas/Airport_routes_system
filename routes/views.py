from django.shortcuts import render, redirect
from .forms import AirportRouteForm, NthNodeSearchForm
from .route_service import (
    get_nth_node, get_longest_route, get_shortest_between_two
)

def add_route(request): # View to add a new airport route.
    form = AirportRouteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('add-route')

    return render(request, 'routes/add_route.html', {'form': form})


def nth_node_view(request):  # View to get the nth node in a direction.
    node = None
    form = NthNodeSearchForm(request.GET or None)

    if form.is_valid():
        direction = form.cleaned_data['direction']
        n = form.cleaned_data['n']
        node = get_nth_node(direction, n) # Fetch the nth node using the service function

    return render(request, 'routes/nth_node.html', {
        'form': form,
        'node': node
    })


def longest_route_view(request): # View to get the longest route.
    longest = get_longest_route()
    return render(request, 'routes/longest_route.html', {'longest': longest})


def shortest_route_view(request):  # View to get the shortest route between two airports.
    airport1 = request.GET.get('a1')
    airport2 = request.GET.get('a2')
    shortest = None

    if airport1 and airport2:
        shortest = get_shortest_between_two(airport1, airport2)

    return render(request, 'routes/shortest_route.html', {
        'shortest': shortest
    })
