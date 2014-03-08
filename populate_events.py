__author__ = 'Adam'
import os


def add_event(sport, players, info, address):
    event = Event.objects.get_or_create(sport=sport, players=players, info=info, address=address)[0]
    return event


def populate():
    info_a = 'We will be here for another 2 hours. Need more people'
    info_b = 'We are on the second field.'

    lake_johnson = 'Lake Johnson Park, Raleigh, NC'
    pullen_park = 'Pullen Park, Raleigh, NC'
    williams_park = '1525 Lynn Road, Raleigh, NC'

    add_event(sport='Football', players=6, info=info_a, address=lake_johnson)
    add_event(sport='Football', players=10, info=info_b, address=pullen_park)
    add_event(sport='Soccer', players=14, info=info_a, address=williams_park)
    add_event(sport='Soccer', players=4, info=info_a, address=lake_johnson)
    add_event(sport='Ultimate Frisbee', players=20, info=info_b, address=pullen_park)
    add_event(sport='Ultimate Frisbee', players=1, info=info_a, address=williams_park)

    # Print out all events
    for event in Event.objects.all():
        print("Sport: {0}, Players: {1}, Info: {2}, Address: {3}".format(
            event.sport,
            str(event.players),
            event.info,
            event.address
        ))

# Start execution here!
if __name__ == '__main__':
    print("Starting NSA population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neighborhood_sports_app.settings')
    from NSA.models import Event
    populate()