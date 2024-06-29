class Payloads:
    @staticmethod
    def user_create():
        return {
            "id": 123456,
            "username": "tolunay12345",
            "firstName": "john",
            "lastName": "doe",
            "email": "johndoe@mail.com",
            "password": "1234",
            "phone": "90123456789",
            "userStatus": 1
        }

    @staticmethod
    def user_update():
        return {
            "id": 123456,
            "username": "tolunay12345",
            "firstName": "john",
            "lastName": "doe",
            "email": "johndoe@mail.com",
            "password": "1234",
            "phone": "42123456789",
            "userStatus": 1
        }

    @staticmethod
    def user_array():
        return [
            {
                "id": 12341234,
                "username": "tolunay123array",
                "firstName": "jane",
                "lastName": "doe",
                "email": "janedoe@mail.com",
                "password": "1234",
                "phone": "90987654321",
                "userStatus": 2
            }
        ]

    @staticmethod
    def user_login():
        return {
            "username": "tolunay12345",
            "password": "1234"
        }

    @staticmethod
    def user_delete():
        return {
            "id": 123456,
            "username": "tolunay1234del",
            "firstName": "john",
            "lastName": "doe",
            "email": "johndoe@mail.com",
            "password": "1234",
            "phone": "90123456789",
            "userStatus": 1
        }
