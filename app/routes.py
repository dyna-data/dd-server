from flask import Blueprint, abort, jsonify
from app.shared import import_model


api = Blueprint("api", __name__, url_prefix='/api')

@api.route('/<model>', methods=['GET'])
def get_all(model):
    mdl_cls = import_model(model)
    if mdl_cls is None:
        abort(404)
    
    dataset = mdl_cls.query.all()
    if dataset is None:
        return None
    else:
        return jsonify([m.to_dict() for m in dataset])


@api.route('/<model>/<id>', methods=['GET'])
def get_id(model, id):
    mdl_cls = import_model(model)
    if mdl_cls is None:
        abort(404)
    
    dataset = mdl_cls.query.get(id)
    if dataset is None:
        return None
    else:        
        return jsonify(dataset.to_dict())