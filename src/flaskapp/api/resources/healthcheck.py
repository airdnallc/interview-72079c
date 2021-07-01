"""Healthcheck endpoint resource."""
from flask_restful import Resource
import os


class HealthcheckResource(Resource):
    """Healthcheck resource."""

    def get(self):
        return f'sample-kube-app {os.uname().nodename} is healthy' # the text can be anything you like, but this helps
    # identify individual containers behind api gateways and traffic routers like load balancers. Needs to return 200
