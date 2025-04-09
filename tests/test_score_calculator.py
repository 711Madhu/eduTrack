from score_calculator import calculate_average

def test_calculate_average():
    assert calculate_average([70, 80, 90]) == 80
    assert calculate_average([]) == 0
