class User:
    __user_longitude = None
    __user_latitude = None

    @staticmethod
    def get_user_longitude() -> float:
        return User.__user_longitude

    @staticmethod
    def get_user_latitude() -> float:
        return User.__user_latitude

    @staticmethod
    def set_user_longitude(value: float):
        User.__user_longitude = value

    @staticmethod
    def set_user_latitude(value: float):
        User.__user_latitude = value