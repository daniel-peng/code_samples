import os
import pandas as pd

COLUMNS = ['id', 'mileage', 'customer_id', 'dealership_id', 'interior_condition', 'powertrain', 'vehicle_type',
           'structural_damage', 'exterior_condition', 'windshield', 'tires_status', 'tires_needs_new', 'tires_brand',
           'wheels_alloy', 'wheels_size', 'wheels_condition', 'year', 'style', 'trans', 'engine', 'drivetrain',
           'division', 'base_price', 'tires', 'seats', 'paint', 'color', 'interior_color', 'seconds_in_disposition',
           'transports_count', 'bought_price', 'costs', 'profit']


def load():
    print(os.path.join(os.path.dirname(__file__), 'dataset.csv'))
    return pd.read_csv(os.path.join(os.path.dirname(__file__), 'dataset.csv'), sep=',', low_memory=False)
