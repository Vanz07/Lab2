import lab2

def test_find_min_max():
    result = lab2.find_min_max([10, 20, 30, 40, 50])
    assert result == "min value is 10 and max value 50"

def test_calc_average():
    result = lab2.calc_average_temp([10, 20, 30, 40, 50])
    assert result == "average is 30.0"

def test_calc_median_temperature():
    result = lab2.calc_median_temperature([10, 20, 30, 40, 50])
    assert result == 30

def test_calc_median_temperature_even():
    result = lab2.calc_median_temperature([10, 20, 30, 40])
    assert result == 25.0