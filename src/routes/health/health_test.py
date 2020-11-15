''' write unit tests for this api here '''
import pytest
from unittest.mock import Mock
from health import HealthApi

def test_health_route_OK():
    api = HealthApi(None)
    api.is_database_connected = Mock(return_value=True)
    response = api.health()
    assert response == "health route - service is alive, report some nice stats"

def test_health_route_broken_db_connection():
    api = HealthApi(None)
    api.is_database_connected = Mock(return_value=False)
    response = api.health()
    assert response == "service is down"