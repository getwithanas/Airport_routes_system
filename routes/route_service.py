from routes.models import AirportRoute

def get_nth_node(direction, n): # Get the nth node in the specified direction.
    if direction == "left":
        return AirportRoute.objects.order_by('position')[n-1]  # Get nth node from the left (ascending order)
    else:
        return AirportRoute.objects.order_by('-position')[n-1] # Get nth node from the right (descending order)


def get_longest_route(): # Get the route with the longest duration.
    return AirportRoute.objects.order_by('-duration').first() 


def get_shortest_between_two(airport1, airport2): # Get the shortest route between two airports.
    return AirportRoute.objects.filter(
        airport_code__in=[airport1, airport2]
    ).order_by('duration').first()
