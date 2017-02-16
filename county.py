from admin_division import AdminDivision

class County(AdminDivision):
    objects = []

    def __init__(self, name, id, typ):
        AdminDivision.__init__(self, name, id, typ)
        self.communities = []
        County.objects.append(self)