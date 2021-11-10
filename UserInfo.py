class UserInfo:
    def __init__(self) -> None:
        self.firstName = None
        self.lastName = None
        self.gender = None
        self.birthday = None
        self.certification_type = None
        self.id_number = None
        self.password = None
        self.email = None
        self.phoneNumber = None

    def setInfo(self, firstName, lastName, gender, birthday, certification_type, id_number, password, email, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.birthday = birthday
        self.certification_type = certification_type
        self.id_number = id_number
        self.password = password
        self.email = email
        self.phoneNumber = phoneNumber
