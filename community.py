from admin_division import AdminDivision

class Community(AdminDivision):
    objects = []

    def __init__(self, name, id, typ, pow_id):
        AdminDivision.__init__(self, name, id, typ)
        self.pow_id = pow_id
        Community.objects.append(self)
