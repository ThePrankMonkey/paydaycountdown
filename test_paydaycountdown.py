from datetime import date
from paydaycountdown import HolidayEZ
from paydaycountdown import HolidayHard
from paydaycountdown import get_real_pay_dates

# Test Holiday classes
july_4th = HolidayEZ("July 4th", 7, 4, 2018)
def test_july_4th_date():
    assert(july_4th.date == date(2018,7,4))

def test_july_4th_name():
    assert(july_4th.name == "July 4th")

veterens_day = HolidayEZ("Veterans Day", 11, 11, 2018)
veterens_day_observed = HolidayEZ("Veterans Day", 11, 11, 2018, observed=True)
def test_veterens_day_date():
    assert(veterens_day.date == date(2018,11,11))

def test_veterens_day_name():
    assert(veterens_day.name == "Veterans Day")

def test_veterens_day_observed_date():
    assert(veterens_day_observed.date == date(2018,11,12))

def test_veterens_day_observed_name():
    assert(veterens_day_observed.name == "Veterans Day (Observed)")

thanksgiving_day = HolidayHard("Thanksgiving Day", 11, 4, 3, 2018)
def test_thanksgiving_day_date():
    assert(thanksgiving_day.date == date(2018,11,22))

def test_thanksgiving_day_name():
    assert(thanksgiving_day.name == "Thanksgiving Day")


# Test Checking Pay Days
pay_day_test_date = date(2018,12,1)
def test_pay_days_no_offset():
    real_pay_days_no_offset_expected = (date(2018,12,6), date(2018,12,21))
    real_pay_days_no_offset_results = get_real_pay_dates(today=pay_day_test_date, offset=0)
    assert(real_pay_days_no_offset_expected == real_pay_days_no_offset_results)

def test_pay_days_with_offset():
    real_pay_days_with_offset_expected = (date(2019,1,4), date(2019,1,22))
    real_pay_days_with_offset_results = get_real_pay_dates(today=pay_day_test_date, offset=1)
    assert(real_pay_days_with_offset_expected == real_pay_days_with_offset_results)
