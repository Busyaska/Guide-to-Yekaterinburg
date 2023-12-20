import math
import requests
from Alice_routs import Messages
from Alice_user import User


class CoordinatesProcessor:
    @staticmethod
    def find_distance(sight_latitude: float, sight_longitude: float, user_latitude: float,
                      user_longitude: float) -> float:
        earth_radius = 6371
        sight_latitude_radians = math.radians(sight_latitude)
        sight_longitude_radians = math.radians(sight_longitude)
        user_latitude_radians = math.radians(user_latitude)
        user_longitude_radians = math.radians(user_longitude)
        delta_latitude = user_latitude_radians - sight_latitude_radians
        delta_longitude = user_longitude_radians - sight_longitude_radians
        angular_distance = math.sin(delta_latitude / 2) ** 2 + math.cos(sight_longitude_radians) * math.cos(
            user_latitude_radians) * math.sin(delta_longitude / 2) ** 2
        angular_distance_radians = 2 * math.atan2(math.sqrt(angular_distance), math.sqrt(1 - angular_distance))
        distance = earth_radius * angular_distance_radians
        return distance

    @staticmethod
    def process_coordinates(line: str, sights: list[str, float, float]) -> str:
        user_latitude = User.get_user_latitude()
        user_longitude = User.get_user_longitude()
        if line == 'blue_line':
            first_sight_index = 0
            last_sight_index = -1
            for i in [first_sight_index, last_sight_index]:
                sight_name = sights[i][0]
                sight_latitude = sights[i][1]
                sight_longitude = sights[i][2]
                distance = CoordinatesProcessor.find_distance(sight_latitude, sight_longitude, user_latitude,
                                                              user_longitude)
                sights[i] = [sight_name, distance]
        else:
            for i in range(len(sights)):
                sight_name = sights[i][0]
                sight_latitude = sights[i][1]
                sight_longitude = sights[i][2]
                distance = CoordinatesProcessor.find_distance(sight_latitude, sight_longitude, user_latitude,
                                                              user_longitude)
                sights[i] = [sight_name, distance]
        the_nearest_sight = min(sights, key=lambda x: x[1])[0]
        the_nearest_sight_number = the_nearest_sight.split('_')[-1]
        return the_nearest_sight_number

    @staticmethod
    def find_the_nearest_sight_number(line: str):
        file_content = RequestProcessor.get_coordinates_file(line)
        sights = []
        for sight in file_content:
            sight = sight.strip()
            sight_name, coordinates = sight.split(' : ')
            latitude, longitude = coordinates.split()
            sights.append([sight_name, float(latitude), float(longitude)])
        the_nearest_sight_number = CoordinatesProcessor.process_coordinates(line, sights)
        Response.set_the_nearest_sight_number(the_nearest_sight_number)


class RequestProcessor:
    @staticmethod
    def get_coordinates(address: str) -> str:
        api_key = "bd5a0ad6-7f0f-4edc-9b28-6f471ba5e87f"
        base_url = "https://geocode-maps.yandex.ru/1.x/"
        full_address = f"Россия, Екатеринбург, {address}"
        params = {
            'apikey': api_key,
            'geocode': full_address,
            'format': 'json',
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        if 'response' in data and 'GeoObjectCollection' in data['response']:
            features = data['response']['GeoObjectCollection']['featureMember']
            if features:
                coordinates = features[0]['GeoObject']['Point']['pos']
                longitude, latitude = coordinates.split()
                User.set_user_longitude(float(longitude))
                User.set_user_latitude(float(latitude))
                return "Success"
            else:
                return "Address_Error"
        else:
            return "Geocode_Error"

    @staticmethod
    def get_coordinates_file(line: str) -> list:
        url = f"https://storage.yandexcloud.net/alice-skill/sights_coordinates/{line}_coordinates.txt"
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = "utf-8"
            return response.text.splitlines()
        else:
            return None

    @staticmethod
    def get_sight_file(line: str, current_sight_number: str) -> list:
        url = f'https://storage.yandexcloud.net/alice-skill/{line}/sight_{current_sight_number}.txt'
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = "utf-8"
            return response.text.splitlines()
        else:
            return None


class Response:
    __got_user_location = False
    __the_nearest_sight_number = None
    __commands = {
        'change_route': Messages.get_routs(),
        "Address_Error": Messages.get_geocode_error(),
        "Geocode_Error": Messages.get_address_error(),
        'exit': Messages.get_farewell()
    }

    @staticmethod
    def set_got_user_location(value: bool):
        Response.__got_user_location = value

    @staticmethod
    def set_is_making_route(value: bool):
        Response.__is_making_route = value

    @staticmethod
    def set_the_nearest_sight_number(value: str):
        Response.__the_nearest_sight_number = value

    @staticmethod
    def get_the_nearest_sight_number() -> str:
        return Response.__the_nearest_sight_number

    @staticmethod
    def make_rout(rout_info: dict) -> dict:
        line = rout_info['line']
        total_sights_number = int(rout_info['total_sights_number'])
        user_latitude = User.get_user_latitude()
        user_longitude = User.get_user_longitude()
        the_nearest_sight_number = int(Response.get_the_nearest_sight_number())
        sights = {}
        rout_url = f'https://yandex.ru/maps?rtext={user_latitude}%2C{user_longitude}~'
        file_content = RequestProcessor.get_coordinates_file(line)
        for line in file_content:
            sight_name, coordinates = line.split(' : ')
            latitude, longitude = coordinates.split()
            sights[sight_name] = [latitude, longitude]
        for i in range(total_sights_number):
            sight_number = ((the_nearest_sight_number + i) % total_sights_number)
            sight_name = f'sight_{sight_number}'
            latitude, longitude = sights[sight_name]
            rout_url += f'{latitude}%2C{longitude}~'
        rout_url = rout_url[:-1] + '&rtt=pd'
        message = Messages.make_rout_url_message(rout_url)
        return message

    @staticmethod
    def start_excursion(rout_info: dict) -> dict:
        command = rout_info['command']
        line = rout_info['line']
        next_sight_number = rout_info['next_sight_number']
        visited_sights_number = rout_info['visited_sights_number']
        total_sights_number = rout_info['total_sights_number']
        new_excursion = rout_info['new_excursion']
        if new_excursion == 'true':
            CoordinatesProcessor.find_the_nearest_sight_number(line)
        the_nearest_sight_number = Response.get_the_nearest_sight_number()
        if line == 'blue_line' and the_nearest_sight_number == '11':
            line = 'blue_line_reverse'
        current_sight_number = str((int(next_sight_number) + int(the_nearest_sight_number)) % int(total_sights_number))
        data = RequestProcessor.get_sight_file(line, current_sight_number)
        if data:
            image_id, title, description, button_text = data
            message = Messages.make_current_sight_message(title, image_id, description,
                                                          button_text, command, line, next_sight_number,
                                                          visited_sights_number, total_sights_number)
        else:
            message = Messages.get_regular_error()
        return message

    @staticmethod
    def make_other_sight_message(rout_info):
        line = rout_info['line']
        CoordinatesProcessor.find_the_nearest_sight_number(line)
        the_nearest_sight_number = Response.get_the_nearest_sight_number()
        sight_name = f'sight_{the_nearest_sight_number}'
        file_content = RequestProcessor.get_coordinates_file(line)
        data = RequestProcessor.get_sight_file(line, the_nearest_sight_number)
        if file_content and data:
            for file_line in file_content:
                if sight_name in file_line:
                    sight, coordinates = file_line.split(' : ')
                    sight_latitude, sight_longitude = coordinates.split()
                    break
            image_id, title, description = data
            user_latitude = User.get_user_latitude()
            user_longitude = User.get_user_longitude()
            message = Messages.make_the_nearest_sight_number_message(image_id, title, description,
                                                                     user_latitude, user_longitude, sight_latitude,
                                                                     sight_longitude)
        else:
            message = Messages.get_regular_error()
        return message

    @staticmethod
    def process_command(data):
        command = data['request']['payload']['command']
        if command == 'start_excursion':
            rout_info = data['request']['payload']
            message = Response.start_excursion(rout_info)
        elif command == 'ask_address':
            Response.set_got_user_location(True)
            message = Messages.get_ask_address()
        elif command == 'make_rout':
            rout_info = data['request']['payload']
            message = Response.make_rout(rout_info)
        elif command == 'find_the_nearest_sight':
            rout_info = data['request']['payload']
            message = Response.make_other_sight_message(rout_info)
        else:
            message = Response.__commands[command]
        return message

    @staticmethod
    def process_message(data: dict) -> dict:
        message = Messages.get_regular_message()
        if Response.__got_user_location:
            address = data["request"]["original_utterance"]
            result = RequestProcessor.get_coordinates(address)
            if result == 'Success':
                message = Messages.get_routs()
                Response.set_got_user_location(False)
            else:
                message = Response.__commands[result]
        if data["session"]["new"] == True:
            message = Messages.get_welcome_message()
        elif 'payload' in data['request']:
            message = Response.process_command(data)
        elif data['request']['nlu']['intents']:
            if data['request']['nlu']['intents'].get('CUSTOM_CONFIRM', {}):
                Response.set_got_user_location(True)
                message = Messages.get_ask_address()
            elif data['request']['nlu']['intents'].get('CUSTOM_REJECT', {}):
                message = Messages.get_farewell()
            elif data['request']['nlu']['intents'].get('SKILLS', {}) or data['request']['nlu']['intents'].get('HELP',{}):
                message = Messages.get_help_message()
        response = {
            'version': data["version"],
            'session': data["session"],
            'response': message
        }
        return response


def process_request(event: dict, context: dict) -> dict:
    data = event
    response = Response.process_message(data)
    return response