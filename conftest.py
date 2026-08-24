import pytest
from lib.Utility import sprk_session


@pytest.fixture
def spark():
    return sprk_session("Loc")