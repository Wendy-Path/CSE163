"""
Testing the functions in the EDA.py.
Note: I did not create a smaller file to test with.
Instead I used functions in excel to find the values for
the seven number summaries for each variable of interest.
"""
import EDA
import pandas as pd
GHG_AND_AQI_FILE = "GHG_plus_AQI.csv"


def test_has_missing_values(df: pd.DataFrame):
    """
    Tests has_missing_values function.
    """
    assert EDA.has_missing_values(df) is False


def test_num_rows_and_num_columns(df: pd.DataFrame):
    """
    Tests num_rows_and_num_columns function.
    """
    num_rows, num_columns = EDA.num_rows_and_num_columns(df)
    print(num_rows)
    assert num_rows == 325
    assert num_columns == 4


def test_seven_number_summary(df: pd.DataFrame):
    """
    Tests seven_number_summary function.
    """
    mean, std, min_value, q1, median, q3, max_value = (
        EDA.seven_number_summary(df, "Reported Emissions (MTCO2e)")
    )
    assert 1551437 == round(mean)
    assert 2062147 == round(std)
    assert 13358 == min_value
    assert 172915 == q1
    assert 587700 == round(median)
    assert 2023914 == q3
    assert 10894290 == max_value

    mean, std, min_value, q1, median, q3, max_value = (
        EDA.seven_number_summary(df, "Median AQI")
    )
    assert 31 == round(mean)
    assert 9 == round(std)
    assert 16 == min_value
    assert 24 == q1
    assert 29 == round(median)
    assert 38 == q3
    assert 55 == max_value


def main():
    df = pd.read_csv(GHG_AND_AQI_FILE)
    test_has_missing_values(df)
    test_num_rows_and_num_columns(df)
    test_seven_number_summary(df)
    print("All tests passed!")


if __name__ == "__main__":
    main()
