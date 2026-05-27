import pytest

from filter import filter_above_threshold

@pytest.fixture
def sample_data():
    return {'numbers':[1.0, 5.0,10.0,15.0],'threshold':10.0}

def test_empty_list(sample_data):
    assert filter_above_threshold(sample_data.get('numbers'),sample_data.get('threshold'))

@pytest.mark.parametrize("numbers,threshold",[
    ([1,2,3,4,5],2),
    ([1.0,2.0,3.0,4.0,5.0],2.0),
    ([11.0,11.2],11.1)
])
def test_positive_1(numbers,threshold):
    assert filter_above_threshold(numbers,threshold)


@pytest.mark.parametrize("numbers,threshold", [
    (['бибки'], 10)
])
def test_wrong_value(numbers,threshold):
    with pytest.raises((ValueError)):
        # print('ValueError, TypeError')
        filter_above_threshold(numbers,threshold)

@pytest.mark.parametrize("numbers,threshold", [
    ([1,2,3], '10')
])
def test_wrong_type(numbers,threshold):
    with pytest.raises((TypeError)):
        # print('ValueError, TypeError')
        filter_above_threshold(numbers,threshold)