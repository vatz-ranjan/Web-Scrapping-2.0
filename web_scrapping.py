from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from queries import create_table_query, insert_query, features_mobiles, folder_name, sqlite_file_name, json_file_name
from json_database import JSONDataBase
from smartphone_class import SmartPhone
from sql_database import SQLDataBase


def web_scraping():
    sql = SQLDataBase(folder_name=folder_name, file_name=sqlite_file_name)
    sql.setup()
    sql.create_table(query=create_table_query)
    json = JSONDataBase(folder_name=folder_name, file_name=json_file_name)
    json.setup()
    more_data = True
    page_no = 1
    while more_data:
        base_url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page='
        url = base_url + str(page_no)
        page_no = page_no + 1
        req = urllib.request.urlopen(url).read().decode()
        soup = BeautifulSoup(req, features='lxml')

        entries = soup.findAll('a', href=True, attrs={'class': '_1fQZEK'})

        if len(entries) > 0:
            for entry in entries:
                smart_phone = SmartPhone()

                model_name = entry.find('div', attrs={'class': '_4rR01T'}).text.upper()
                smart_phone.set_model_name(model_name)

                brand_name = model_name.split(" ")[0]
                smart_phone.set_brand_name(brand_name
                                           )
                color = model_name[model_name.find("(") + len("("):model_name.find(",")]
                if len(color) < 2:
                    color = "?"
                smart_phone.set_color(color)

                try:
                    offer_price = int(entry.find('div', attrs={'class': '_30jeq3 _1_WHN1'}).text[1:].replace(',', ''))
                except:
                    offer_price = "?"
                smart_phone.set_offer_price(offer_price)

                try:
                    discount = int(entry.find('div', attrs={'class': '_3Ay6Sb'}).string[:-5])
                except:
                    discount = 0
                smart_phone.set_discount(discount)

                if discount == 0:
                    original_price = offer_price
                else:
                    try:
                        original_price = int(entry.find('div', attrs={'class': '_3I9_wc _27UcVY'}).text.strip()[1:].replace(',', ''))
                    except:
                        original_price = "?"
                smart_phone.set_original_price(original_price)

                features = entry.find('ul', attrs={'class': '_1xgFaf'})
                features_list = []

                for feature in features:
                    features_list.append(feature.text.split("|"))

                try:
                    if 'RAM' in features_list[0][0].upper():
                        ram = features_list[0][0][:features_list[0][0].upper().find("RAM")]
                    else:
                        ram = "?"
                except: ram = "?"
                smart_phone.set_ram(ram)

                try:
                    if 'ROM' in features_list[0][1].upper():
                        rom = features_list[0][1][:features_list[0][1].upper().find("ROM")]
                    else:
                        rom = "?"
                except:
                    rom = "?"
                smart_phone.set_rom(rom)

                try:
                    if 'DISPLAY' in features_list[1][0].upper():
                        resolution = features_list[1][0].upper().strip()
                    else:
                        resolution = "?"
                except:
                    resolution = "?"
                smart_phone.set_resolution(resolution)

                try:
                    if 'MP' in features_list[2][0].upper():
                        primary_cam = features_list[2][0].upper().replace('REAR', '').replace('CAMERA', '').strip()
                    else:
                        primary_cam = "?"
                except:
                    primary_cam = "?"
                smart_phone.set_primary_camera(primary_cam)

                try:
                    if 'FRONT' in features_list[2][1].upper():
                        secondary_cam = features_list[2][1].upper().replace('FRONT', '').replace('CAMERA', '').strip() # .replace('FRONT', '').replace('CAMERA', '')
                    else:
                        secondary_cam = "?"
                except:
                    secondary_cam = "?"
                smart_phone.set_secondary_camera(secondary_cam)

                try:
                    if 'BATTERY' in features_list[3][0].upper():
                        battery_cap = features_list[3][0][:features_list[3][0].find('mAh')].upper().strip()
                        battery_type = features_list[3][0][features_list[3][0].find('mAh')+len('mAh'):].upper().strip()
                    else:
                        battery_cap = "?"
                        battery_type = "?"
                except:
                    battery_cap = "?"
                    battery_type = "?"
                smart_phone.set_battery_type(battery_type)
                smart_phone.set_battery_capacity(battery_cap)

                try:
                    if 'PROCESSOR' in features_list[4][0].upper():
                        processor = features_list[4][0].upper().strip()
                    else:
                        processor = "?"
                except:
                    processor = "?"
                smart_phone.set_processor(processor)

                values = (smart_phone.get_brand_name(),
                          smart_phone.get_model_name(),
                          smart_phone.get_color(),
                          smart_phone.get_original_price(),
                          smart_phone.get_discount(),
                          smart_phone.get_offer_price(),
                          smart_phone.get_ram(),
                          smart_phone.get_rom(),
                          smart_phone.get_resolution(),
                          smart_phone.get_primary_camera(),
                          smart_phone.get_secondary_camera(),
                          smart_phone.get_battery_capacity(),
                          smart_phone.get_battery_type(),
                          smart_phone.get_processor()
                          )
                sql.insert_values(insert_query, values)
                json.insert_values(features_mobiles, values)

        else:
            more_data = False
        # break

    sql.commit()
    sql.close()


if __name__ == '__main__':
    web_scraping()