class SmartPhone:

    def __init__(self):
        self.__brand_name: str = None
        self.__model_name = None
        self.__color = None
        self.__original_price = None
        self.__discount = None
        self.__offer_price = None
        self.__ram = None
        self.__rom = None
        self.__resolution = None
        self.__primary_camera = None
        self.__secondary_camera = None
        self.__battery_capacity = None
        self.__battery_type = None
        self.__processor = None

    def set_brand_name(self, brand_name):
        self.__brand_name = brand_name

    def set_model_name(self, model_name):
        self.__model_name = model_name

    def set_color(self, color):
        self.__color = color

    def set_original_price(self, original_price):
        self.__original_price = original_price

    def set_discount(self, discount):
        self.__discount = discount

    def set_offer_price(self, offer_price):
        self.__offer_price = offer_price

    def set_ram(self, ram):
        self.__ram = ram

    def set_rom(self, rom):
        self.__rom = rom

    def set_resolution(self, resolution):
        self.__resolution = resolution

    def set_primary_camera(self, primary_camera):
        self.__primary_camera = primary_camera

    def set_secondary_camera(self, secondary_camera):
        self.__secondary_camera = secondary_camera

    def set_battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity

    def set_battery_type(self, battery_type):
        self.__battery_type = battery_type

    def set_processor(self, processor):
        self.__processor = processor

    def get_brand_name(self):
        return self.__brand_name

    def get_model_name(self):
        return self.__model_name

    def get_color(self):
        return self.__color

    def get_original_price(self):
        return self.__original_price

    def get_discount(self):
        return self.__discount

    def get_offer_price(self):
        return self.__offer_price

    def get_ram(self):
        return self.__ram

    def get_rom(self):
        return self.__rom

    def get_resolution(self):
        return self.__resolution

    def get_primary_camera(self):
        return self.__primary_camera

    def get_secondary_camera(self):
        return self.__secondary_camera

    def get_battery_capacity(self):
        return self.__battery_capacity

    def get_battery_type(self):
        return self.__battery_type

    def get_processor(self):
        return self.__processor

