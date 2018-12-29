""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(uuid):
        """ Query a user by last and first name """
        return User.query.filter_by(
            uuid=uuid
        ).one()

    def update(self, last_name, first_name, uuid, age):
        """ Update a user's age """
        user = self.get(uuid)
        user.first_name = first_name
        user.last_name = last_name
        user.age = age

        return user.save()

    @staticmethod
    def create(last_name, first_name, uuid, age):
        """ Create a new user """
        user = User(last_name=last_name, first_name=first_name, uuid=uuid, age=age)

        return user.save()
