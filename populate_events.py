__author__ = 'Adam'
import os


def add_event(sport, players, address, latitude, longitude):
    event = Event.objects.get_or_create(sport=sport, players=players,
                                        #info=info,
                                        address=address,
                                        latitude=latitude, longitude=longitude)[0]
    return event


def populate():
    #info_a = 'We will be here for another 2 hours. Need more people'
    #info_b = 'We are on the second field.'

    lake_johnson = 'Lake Johnson Park, Raleigh, NC'
    pullen_park = 'Pullen Park, Raleigh, NC'
    williams_park = '1525 Lynn Road, Raleigh, NC'
    the_oval = "On the Oval Culinary Creations, Raleigh, NC 27606"
    kentwood_park = "Kentwood Park, 4531 Kaplan Dr, Raleigh, NC 27606"
    carmichael_gym = "Carmichael Gymnasium, Raleigh, NC"

    lake_johnson_lat = '35.763521'
    lake_johnson_long = '-78.7138224'
    pullen_park_lat = '35.7808484'
    pullen_park_long = '-78.6643668'
    williams_park_lat = '35.869753'
    williams_park_long = '-78.665720'
    the_oval_lat = '35.74183'
    the_oval_long = '-78.713608'
    kentwood_park_lat = '35.74183'
    kentwood_park_long = '-78.713608'
    carmichael_gym_lat = '35.74183'
    carmichael_gym_long = '-78.713608'

    add_event(sport='Football', players=6, address=lake_johnson,
              latitude=lake_johnson_lat, longitude=lake_johnson_long)
    add_event(sport='Football', players=10, address=pullen_park,
              latitude=pullen_park_lat, longitude=pullen_park_long)
    add_event(sport='Soccer', players=14, address=williams_park,
              latitude=williams_park_lat, longitude=williams_park_long)
    add_event(sport='Baseball', players=4, address=the_oval,
              latitude=the_oval_lat, longitude=the_oval_long)
    add_event(sport='Tennis', players=20, address=kentwood_park,
              latitude=kentwood_park_lat, longitude=kentwood_park_long)
    add_event(sport='Basketball', players=1, address=carmichael_gym,
              latitude=carmichael_gym_lat, longitude=carmichael_gym_long)

    # Print out all events
    for event in Event.objects.all():
        print("Sport: {0}, Players: {1}, Address: {2}, Latitude: {3}, Longitude: {4}".format(
            event.sport,
            str(event.players),
            #event.info,
            event.address,
            str(event.latitude),
            str(event.longitude)
        ))

# Start execution here!
if __name__ == '__main__':
    print("Starting NSA population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neighborhood_sports_app.settings')
    from NSA.models import Event
    populate()
