import googlemaps
from datetime import datetime, time
import pprint
import json

gmaps = googlemaps.Client(key='AIzaSyC635qRah1SfJs4rdtX6iJeg08RshxhUk0')

#Get time to work function
def get_time_to_work(home_address = "2 Spencer Way, London, UK", work_address = "30 Fenchurch Street, London, UK"):
    """This tool allows to get journey times to work from your home address. 
    
    The tool takes in two inputs: 'home_adress' (string) and 'work_address' (string) and returns a response as a string.
    """

    # Get 9 am timestamp
    work_start = datetime.combine(datetime.now().date(), time(9, 0))
    # Request directions via public transit
    directions_result = gmaps.directions(
        home_address,
        work_address,
        mode="transit",
        arrival_time=work_start
    )

    # Get travel duration from the directions
    for leg in directions_result[0]['legs']:
        duration=leg['duration']['text']

    rslt = "Time to get to work by public transport: " + duration

    return rslt