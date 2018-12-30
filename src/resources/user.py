"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument
from flask.json import jsonify

from repositories import UserRepository
from util import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from('../swagger/user/GET.yml')
    def get(uuid):
        """ Return an user key information based on his name """
        user = UserRepository.get(uuid=uuid)
        return jsonify({'user': user.json})

    @staticmethod
    @parse_params(
        Argument(
            'age',
            location='json',
            required=False,
            help='The age of the user.'
        ),
        Argument(
            'first_name',
            location='json',
            required=False,
            help='The first name of the user.'
        ),
        Argument(
            'last_name',
            location='json',
            required=False,
            help='The last name of the user.'
        ),

    )
    @swag_from('../swagger/user/POST.yml')
    def post(last_name, first_name, uuid, age):
        """ Create an user based on the sent information """
        user = UserRepository.create(
            last_name=last_name,
            first_name=first_name,
            uuid=uuid,
            age=age
        )
        return jsonify({'user': user.json})

    @staticmethod
    @parse_params(
        Argument(
            'age',
            location='json',
            required=False,
            help='The age of the user.'
        ),
        Argument(
            'first_name',
            location='json',
            required=False,
            help='The first name of the user.'
        ),
        Argument(
            'last_name',
            location='json',
            required=False,
            help='The last name of the user.'
        ),

    )
    @swag_from('../swagger/user/PUT.yml')
    def put(last_name, first_name, uuid, age):
        """ Update an user based on the sent information """
        repository = UserRepository()
        user = repository.update(
            last_name=last_name,
            first_name=first_name,
            uuid=uuid,
            age=age
        )
        return jsonify({'user': user.json})
