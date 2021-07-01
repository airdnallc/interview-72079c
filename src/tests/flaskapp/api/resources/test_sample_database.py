import pytest
from flaskapp.api.resources.sample_database import db_count


@pytest.mark.skip("doesn't work without application context, since db access is handled by flask")
def test_count():
    assert db_count() is not None