from admin_division import AdminDivision

class Voivodeship(AdminDivision):
    objects = []

    def __init__(self, name, id):
        AdminDivision.__init__(self, name, id, typ='wojewódźtwo')
        self.counties = []
        Voivodeship.objects.append(self)