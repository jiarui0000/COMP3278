class UserInfo:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.gender = ""
        self.birthday = ""
        self.certification_type = ""
        self.id_number = ""
        self.password = ""
        self.email = ""
        self.phoneNumber = ""

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
