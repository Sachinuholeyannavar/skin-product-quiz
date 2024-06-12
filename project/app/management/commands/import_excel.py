import pandas as pd
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Import data from Excel file into Django database'

    def handle(self, *args, **kwargs):
        excel_file_path = r'C:\Users\jagdeeshgouda\Desktop\prj\project\app\Skin Care Questionaire Tags.xlsx'

        # Get the Product model dynamically
        Product = apps.get_model('app', 'Product')

        # Read Excel file and inspect the first few rows
        try:
            df = pd.read_excel(excel_file_path, na_values=[''], keep_default_na=False, header=1)
            print("First few rows of the DataFrame:")
            print(df.head())
            print("Columns in the DataFrame:")
            print(df.columns.tolist())

            # Strip leading/trailing whitespace from column names
            df.columns = df.columns.str.strip()

            # Rename columns to match the expected field names in the Product model
            df.rename(columns={
                'AnteAGE Eye': 'Product Name',
                'Skin Care': 'Skin Care/Hair Care',
                'Anteage': 'Brand',
                'Unnamed: 4': 'Teens',
                'Unnamed: 5': "20's",
                'X': "30's",
                'X.1': "40's",
                'X.2': "50's",
                'X.3': "60's",
                'X.4': 'Skin Type Normal',
                'X.5': 'Oily',
                'X.6': 'Dry',
                'X.7': 'Sensitive',
                'X.8': 'Combination',
                'Unnamed: 15': 'Skin Concerns: Acne',
                'X.9': 'Aging',
                'X.10': 'Dull Skin',
                'X.11': 'Elasticity',
                'X.12': 'Hydration',
                'X.13': 'Pigmentation',
                'Unnamed: 21': 'Pores',
                'Unnamed: 22': 'Redness',
                'Unnamed: 23': 'Scarring',
                'X.14': 'Sensitive Skin',
                'Unnamed: 25': 'Sun Protection',
                'X.15': 'Texture',
                'X.16': 'UnEven Skin Tone',
                'Unnamed: 28': 'Products: Body care',
                'X.17': 'Eye Cream',
                'Unnamed: 30': 'Cleanser',
                'Unnamed: 31': 'Exfoiliant',
                'Unnamed: 32': 'Microneedling',
                'X.18': 'Moisturizer',
                'Unnamed: 34': 'Peels',
                'Unnamed: 35': 'Serums',
                'Unnamed: 36': 'Sun Screen',
                'Unnamed: 37': 'Spot Treatment',
                'Unnamed: 38': 'Toner',
                'Unnamed: 39': 'Do  you use sunscreen Daily Yes',
                'Unnamed: 40': 'No',
                'Unnamed: 41': 'Skin React to sun Exposure',
                'Unnamed: 42': 'Hair Loss: Yes',
                'Unnamed: 43': 'No'
            }, inplace=True)

            # Debugging: print the columns again to verify renaming
            print("Renamed columns in the DataFrame:")
            print(df.columns.tolist())
        except Exception as e:
            self.stderr.write(f'Failed to read Excel file: {e}')
            return

        # Function to convert value to boolean
        def value_to_boolean(value):
            if pd.isnull(value):
                return None
            else:
                value = str(value).strip().lower()
                if value in ['yes', 'y']:
                    return True
                elif value in ['no', 'n']:
                    return False
                elif value == 'x':
                    return True
            return None

        # Process data and save to database
        try:
            for index, row in df.iterrows():
                # Create Product object with data
                Product.objects.create(
                    product_name=row['Product Name'].strip() if not pd.isnull(row['Product Name']) else '',
                    skin_care_hair_care=row['Skin Care/Hair Care'].strip() if not pd.isnull(row['Skin Care/Hair Care']) else '',
                    brand=row['Brand'].strip() if not pd.isnull(row['Brand']) else '',
                    teens=value_to_boolean(row['Teens']),
                    twenties=value_to_boolean(row["20's"]),
                    thirties=value_to_boolean(row["30's"]),
                    forties=value_to_boolean(row["40's"]),
                    fifties=value_to_boolean(row["50's"]),
                    sixties=value_to_boolean(row["60's"]),
                    skin_type_normal=value_to_boolean(row['Skin Type Normal']),
                    oily=value_to_boolean(row['Oily']),
                    dry=value_to_boolean(row['Dry']),
                    sensitive=value_to_boolean(row['Sensitive']),
                    combination=value_to_boolean(row['Combination']),
                    skin_concerns_acne=value_to_boolean(row['Skin Concerns: Acne']),
                    aging=value_to_boolean(row['Aging']),
                    dull_skin=value_to_boolean(row['Dull Skin']),
                    elasticity=value_to_boolean(row['Elasticity']),
                    hydration=value_to_boolean(row['Hydration']),
                    pigmentation=value_to_boolean(row['Pigmentation']),
                    pores=value_to_boolean(row['Pores']),
                    redness=value_to_boolean(row['Redness']),
                    scarring=value_to_boolean(row['Scarring']),
                    sensitive_skin=value_to_boolean(row['Sensitive Skin']),
                    sun_protection=value_to_boolean(row['Sun Protection']),
                    texture=value_to_boolean(row['Texture']),
                    uneven_skin_tone=value_to_boolean(row['UnEven Skin Tone']),
                    body_care=value_to_boolean(row['Products: Body care']),
                    eye_cream=value_to_boolean(row['Eye Cream']),
                    cleanser=value_to_boolean(row['Cleanser']),
                    exfoliant=value_to_boolean(row['Exfoiliant']),
                    microneedling=value_to_boolean(row['Microneedling']),
                    moisturizer=value_to_boolean(row['Moisturizer']),
                    peels=value_to_boolean(row['Peels']),
                    serums=value_to_boolean(row['Serums']),
                    sun_screen=value_to_boolean(row['Sun Screen']),
                    spot_treatment=value_to_boolean(row['Spot Treatment']),
                    toner=value_to_boolean(row['Toner']),
                    use_sunscreen_daily=value_to_boolean(row['Do  you use sunscreen Daily Yes']),
                    react_to_sun_exposure=value_to_boolean(row['Skin React to sun Exposure']),
                    hair_loss=value_to_boolean(row['Hair Loss: Yes']),
                )
        except Exception as e:
            self.stderr.write(f'Failed to import data: {e}')
            return

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))