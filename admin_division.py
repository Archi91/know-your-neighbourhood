
class AdminDivision:
    objects = []

    def __init__(self, name, id, typ):
        self.name = name
        self.typ = typ
        self.id = id
        AdminDivision.objects.append(self)

    def get_to_print(self):
        return self.name, self.typ

