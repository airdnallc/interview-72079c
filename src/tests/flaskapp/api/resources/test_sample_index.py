import pytest
from flaskapp.api.resources.sample_index import cluster_hello


def test_cluster_hello():
    assert cluster_hello() == "Hello from the unknown cluster"
