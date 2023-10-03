import sys

import pandas as pd
sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\Airbnb\venv\Lib\site-packages')
import pymongo
from pymongo.server_api import ServerApi

def extract():
    client = pymongo.MongoClient(
                "mongodb+srv://cluster0.45tmhd1.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority",
                tls=True, tlsCertificateKeyFile='C:\\Users\\Vinoth\\Downloads\\X509-cert-5084476662482489136.pem',
                server_api=ServerApi('1'))

    db = client["sample_airbnb"]
    col_name=db.list_collection_names()
    col=db[col_name[0]]
    data=col.find()
    Airbnbdata=[]
    for i in data:
        data=dict(id=i['_id'],
        listing_url=i['listing_url'],
        name=i['name'],
        description=i['description'],
        summary=i['summary'],
        space=i['space'],
        neighborhood_overview=i['neighborhood_overview'],
        notes=i['notes'],
        transit=i['transit'],
        access=i['access'],
        interaction=i['interaction'],
        house_rules=i['house_rules'],
        property_type=i['property_type'],
        room_type=i['room_type'],
        bed_type=i['bed_type'],
        minimum_nights=i['minimum_nights'],
        maximum_nights=i['maximum_nights'],
        cancellation_policy=i['cancellation_policy'],
        accommodates=i['accommodates'],
        bedrooms=i.get('bedrooms'),
        beds=i.get('beds'),
        availability_365=i['availability']['availability_365'],
        number_of_reviews=i['number_of_reviews'],
        cleaning_fee=i.get('cleaning_fee'),
        extra_people=i['extra_people'],
        guests_included=i['guests_included'],
        host_id=i['host']['host_id'],
        host_name=i['host']['host_name'],
        host_location=i['host']['host_location'],
        neighbourhood=i['host']['host_neighbourhood'],
        country=i['address']['country'],
        country_code=i['address']['country_code'],
        location_type=i['address']['location']['type'],
        longitude=i['address']['location']['coordinates'][0],
        lattitude=i['address']['location']['coordinates'][1],
        is_location_exact=i['address']['location']['is_location_exact'],
        price=i['price'],
        amenities=','.join(i['amenities']),
        rating=i['review_scores'].get('review_scores_rating'))
        Airbnbdata.append(data)

    df=pd.DataFrame(Airbnbdata)
    df.fillna(method="ffill", inplace=True)
    df.description.replace(to_replace='', value='Not Available',inplace=True)
    df.summary.replace(to_replace='', value='No Summary Present',inplace=True)
    df.space.replace(to_replace='', value='No space details Provided',inplace=True)
    df.neighborhood_overview.replace(to_replace='', value='No neighborhood_overview details',inplace=True)
    df.notes.replace(to_replace='', value='No notes',inplace=True)
    df.transit.replace(to_replace='', value='No transit given',inplace=True)
    df.access.replace(to_replace='', value='No access details',inplace=True)
    df.interaction.replace(to_replace='', value='No interaction details',inplace=True)
    df.house_rules.replace(to_replace='', value='No house_rules available',inplace=True)
    df.host_location.replace(to_replace='', value='No host_location details',inplace=True)
    df.neighbourhood.replace(to_replace='', value='No neighbourhood available',inplace=True)
    df.amenities.replace(to_replace='', value='No amenities details',inplace=True)

    df.price=df.price.astype(str).astype(float)
    df.cleaning_fee=df.cleaning_fee[~df.cleaning_fee.isna()].astype(str).astype(float)
    df.extra_people=df.extra_people.astype(str).astype(float)
    df.guests_included=df.guests_included.astype(str).astype(float)
    df.rating=df.rating.astype('Int64')

    df.drop(labels=list(df[df.name.duplicated(keep=False)].index), inplace=True)
    df.to_csv(r'Airbnb.csv')
    return df
