import pytest

from settings.pulse_api_client import PulseRestAPI


@pytest.fixture(scope='module')
def app():
    return PulseRestAPI(resourse='books')