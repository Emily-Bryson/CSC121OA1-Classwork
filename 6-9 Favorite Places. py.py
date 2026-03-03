favorite_places = {
    "maggie":"knoxville, gatlinburg",
    "katie":"all of route 66",
    "emily":"ocean isle, gatlinburg, pigeon forge"
}
for name, places in favorite_places.items():
    print (f"{name.title()}'s favorite places are:")
    for place in places.split(','):
        print(place.title())