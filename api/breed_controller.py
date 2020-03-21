import sys
sys.path.append('../')
from flask import Blueprint, jsonify, make_response, request
from shared.model import Breed, Origin, Temperament, BreedTemperament, db_close, db_connect
from shared.log import Log
from playhouse.shortcuts import model_to_dict

_logging = Log('breed_controller').logger()

breed_controller = Blueprint('breed_controller', __name__)


@breed_controller.route('/', methods=['GET'])
def breeds():
    _args = request.args
    _logging.debug(_args.items())
    if not _args:
        return get_all_breeds()

    elif 'temperament' in _args:
        return get_breed_by_temperament(_args['temperament'])

    elif 'origin' in _args:
        return get_breed_by_origin(_args['origin'])

    elif 'name' in _args:
        return get_breed_by_name(_args['name'])

    else:
        _logging.info('Query string not found')
        return not_found()

@breed_controller.route('/<string:breed_id>', methods=['GET'])
def breed_by_id(breed_id):
    return get_breed_by_id(breed_id)

def get_all_breeds():
    try:
        db_connect()
        _logging.info('Getting All Breeds')
        _breeds = Breed.select(Breed.name, Breed.breed_id)
        if len(_breeds) == 0:
            db_close()
            return not_found()

        else:
            _response =  make_response(jsonify({'breeds':[model_to_dict(breed, only=[Breed.breed_id, Breed.name]) for breed in _breeds]}), 200)
            _logging.debug(_response)
            db_close()
            return _response

    except Exception as err:
        _logging.error('Error while querying database, details: {} '.format(err))
        db_close()
        raise


def get_breed_by_id(_breed_id:str):
    try:
        db_connect()
        _logging.info('Getting breed info by id')
        _breed = Breed.get_or_none(Breed.breed_id == _breed_id)
        _logging.debug(_breed)
        if _breed is None:
            _logging.info('Breed id not found')
            db_close()
            return not_found()

        else:
            _response =  make_response(jsonify(model_to_dict(_breed, backrefs=True)), 200)
            _logging.debug(_response)
            db_close()
            return _response

    except Exception as err:
        _logging.error('Error while querying database, details: {} '.format(err))
        db_close()
        raise

def get_breed_by_name(_breed_name:str):
    try:
        db_connect()
        _logging.info('Getting breed info by name')
        _breed = Breed.get_or_none(Breed.name == _breed_name)
        _logging.debug(_breed)
        if _breed is None:
            _logging.info('Breed id not found')
            db_close()
            return not_found()

        else:
            _response =  make_response(jsonify(model_to_dict(_breed, backrefs=True)), 200)
            _logging.debug(_response)
            db_close()
            return _response

    except Exception as err:
        _logging.error('Error while querying database, details: {} '.format(err))
        db_close()
        raise

def get_breed_by_temperament(_temperament:str):
    try:
        db_connect()
        _logging.info('Getting breed by temperament')
        _breeds = Breed.select(Breed.breed_id, Breed.name).join(BreedTemperament).join(Temperament).where(Temperament.name == _temperament)
        _logging.debug(_breeds)
        if len(_breeds) == 0:
            _logging.info('Temperament not found')
            db_close()
            return not_found()

        else:
            _response =  make_response(jsonify({'breeds':[model_to_dict(breed, only=[Breed.breed_id, Breed.name]) for breed in _breeds]}), 200)
            _logging.debug(_response)
            db_close()
            return _response

    except Exception as err:
        _logging.error('Error while querying database, details: {} '.format(err))
        db_close()
        raise

def get_breed_by_origin(_origin:str):
    try:
        db_connect()
        _logging.info('Getting breed by origin')
        _breeds = Breed.select().join(Origin).where(Origin.name == _origin)
        _logging.debug(_breeds)
        if len(_breeds) == 0:
            db_close()
            _logging.info('Origin not found')
            return not_found()

        else:
            _response =  make_response(jsonify({'breeds':[model_to_dict(breed, backrefs=True) for breed in _breeds]}), 200)
            _logging.debug(_response)
            db_close()
            return _response

    except Exception as err:
        _logging.error('Error while querying database, details: {} '.format(err))
        db_close()
        raise

def not_found():
    _logging.info('Not found')
    return make_response(jsonify({'message': 'not found'}), 404)

