import geopy
import csv
from geopy.geocoders import Nominatim
from time import sleep

# TEST WITH GEOCODING
nom = Nominatim(user_agent="Parmeg")
n = nom.geocode("via Enrico Ferri, 18/2, Reggio nell'Emilia")
print(n)
print(type(n.address))
print(type(n.latitude), type(n.longitude))
print(type(n))
# print(n.raw)
# print(n.raw['lat'])

def remove_duplicates(csv_file_name):
    with open(str(csv_file_name)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        no_duplicates = []
        for row in csv_reader:
            if row[0] in no_duplicates:
                pass
            else:
                no_duplicates.append(row)
        with open() as csv_file_clean:
            csv_writer = csv.write(csv_file_clean)
            for row in no_duplicates:
                csv_writer.writerow()

# GEOCODER
def geocoder(csv_file):
    with open(csv_file) as input_file:
        csv_reader = csv.reader(input_file, delimiter=";")
        nom = Nominatim(user_agent="Water on Mars")
        geocoded_rows = []
        not_geocoded_rows = []
        for row in csv_reader:
            address_to_be_geocoded = row[1] + ", " + row[0] + "," + row[2]
            n = nom.geocode(address_to_be_geocoded)
            if n is not None:
                print(n.latitude, n.longitude)
                geocoded_rows.append({
                    'address': n.address,
                    'lat': n.latitude,
                    'lon': n.longitude
                    })
                sleep(1.2)
            else:
                not_geocoded_rows.append({'address': address_to_be_geocoded})
                sleep(1.2)
        fields = ['address', 'lat', 'lon']
        with open("geocoded.csv", "w", encoding='utf-8', newline="") as output_file:
            csv_writer = csv.DictWriter(output_file, delimiter=';', fieldnames=fields)
            csv_writer.writeheader()

            for element in geocoded_rows:
                csv_writer.writerow(element)

        with open("not_geocoded.csv", "w", encoding='utf-8', newline="") as output_file:
            csv_writer = csv.DictWriter(output_file, delimiter='*', fieldnames=fields)
            csv_writer.writeheader()

            for element in not_geocoded_rows:
                csv_writer.writerow(element)


