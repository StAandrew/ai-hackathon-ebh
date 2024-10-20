import googlemaps
from datetime import datetime, time
from operator import itemgetter
import pprint
import json

#Get top 5 nearby cafes function
def get_nearby_cafe(flat_address: str = "2 Spencer Way, London, UK") -> str:
    """This tool allows to get nearby cafes from the address that you pass in.
    
    The tool takes an address string as an input and returns the list of top 5 cafes as an output.
    """
    gmaps = googlemaps.Client(key='AIzaSyC635qRah1SfJs4rdtX6iJeg08RshxhUk0')
    
    address_coords = gmaps.geocode(flat_address)

    #print(address_coords[0]["geometry"]["location"])
    # Request cafes in 500m radius
    cafe_results = gmaps.places_nearby(
        location=address_coords[0]["geometry"]["location"],
        radius=500,
        type="cafe"
    )

    cafe_list=[]
    # Get the names and the ratings of the cafes
    for i in range(len(cafe_results["results"])):
        cafe_list.append(dict(Name = cafe_results["results"][i]["name"],Rating = cafe_results["results"][i].get("rating",0)))
        #print(cafe_results["results"][i]["name"],", ",cafe_results["results"][i].get("rating",0))

    # Sort the cafes by rating
    cafe_sorted_list = sorted(cafe_list, key = itemgetter("Rating"), reverse=True)

    rslt = "The top 5 cafes nearby based on Google Maps reviews are:"
    # Take the top 5 cafes
    for i in range(5):
        rslt = rslt + "\n"+cafe_sorted_list[i]["Name"] + " with rating " + str(cafe_sorted_list[i]["Rating"])

    return rslt