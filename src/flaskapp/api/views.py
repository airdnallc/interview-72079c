"""API views """
from flask import Blueprint
from flask_restful import Api
from .resources.healthcheck import HealthcheckResource
from .resources.sample_index import SampleIndexResource
from .resources.sample_database import SampleDatabaseResource

# in addition to these imports, you'll need to follow this pattern in the
# __init__.py at flaskapp/api/resources/__init__.py


# main_blueprint = Blueprint('api', __name__, url_prefix='/api/v1') # url_prefix is not necessary, but is useful
main_blueprint = Blueprint('api', __name__)
api = Api(main_blueprint)


api.add_resource(HealthcheckResource, '/healthcheck', '/healthz') # you can have multiple paths for a resource. Uncommon

api.add_resource(SampleIndexResource, '/')

api.add_resource(SampleDatabaseResource, '/count')

# api.add_resource(
#     SomeOtherResource, '/path/morepath/<int:property_id>' # how to add a variable
# )

