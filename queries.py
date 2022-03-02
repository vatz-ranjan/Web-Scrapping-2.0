folder_name = "Mobiles-Flipkart"

sqlite_file_name = "Mobiles_SQL.sqlite"

json_file_name = "Mobiles_JSON.json"

features_mobiles = ["Brand_Name", "Model_Name", "Color", "Original_Price", "Discount",
                    "Offer_Price", "RAM", "ROM", "Resolution", "Primary_Camera",
                    "Secondary_Camera", "Battery_Capacity", "Battery_Type", "Processor"]

create_table_query = '''
        CREATE TABLE IF NOT EXISTS MOBILES 
        (
        {} TEXT NOT NULL, {} TEXT NOT NULL, {} TEXT, {} INTEGER,
        {} INTEGER, {} INTEGER, {} TEXT, {} TEXT, {} TEXT,
        {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT
        )
        '''.format(features_mobiles[0], features_mobiles[1], features_mobiles[2], features_mobiles[3], features_mobiles[4],
                   features_mobiles[5], features_mobiles[6], features_mobiles[7], features_mobiles[8], features_mobiles[9],
                   features_mobiles[10], features_mobiles[11], features_mobiles[12], features_mobiles[13])

insert_query = '''
        INSERT INTO MOBILES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''.format(features_mobiles[0], features_mobiles[1], features_mobiles[2], features_mobiles[3], features_mobiles[4],
                   features_mobiles[5], features_mobiles[6], features_mobiles[7], features_mobiles[8], features_mobiles[9],
                   features_mobiles[10], features_mobiles[11], features_mobiles[12], features_mobiles[13])