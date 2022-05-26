import pytest


@pytest.fixture(params=["one", "uno"])
def fixture1(request):
    return request.param


@pytest.fixture(params=["two", "duo"])
def fixture2(request):
    return request.param


@pytest.fixture(name="fixture1")
@pytest.fixture(name="fixture2")
def test_foobar():
    assert isinstance(fixture1, str)
    assert isinstance(fixture2, str)
