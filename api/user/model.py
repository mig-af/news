from api.init import db



class User(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    name = db.Column("name", db.String(100))
    


    def get_name(self):
        return self.name
    def __str__(self):
        return self.name


