class User:
    def __init__(self, id, gender, height, weight):
        self.id = id
        self.gender = gender
        self.height = height
        self.weight = weight

    def bmi_calc(self):
        return self.weight / (self.height * self.height)

    def file_record(self):
        return f"{self.id}|{self.gender}|{self.height}|{self.weight}\n"
