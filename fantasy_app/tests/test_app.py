#from app import create_app
import pytest
'''
@pytest.fixture
def app():
    app = create_app("testing")
    return app.test_client()

def test_environment_is_test(app_config):
    assert app_config.FLASK_ENV == "testing"


def test_environment_is_not_dev(app_config):
    assert app_config.FLASK_ENV != "development"


def test_environment_is_not_prod(app_config):
    assert app_config.FLASK_ENV != "production"
'''