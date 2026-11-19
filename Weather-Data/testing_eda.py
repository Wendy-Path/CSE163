import EDA_computation


def test_median() -> None:
    """
    Test the median method
    """
    assert (2 == EDA_computation.median([1, 2, 3]))
    assert (2.5 == EDA_computation.median([1, 2, 3, 4]))


def test_summary() -> None:
    """
    Test the seven_number_summary method
    """
    assert ('Mean: 3.0 | Standard Deviation: 1.4142135623730951 | ' +
            'Minimum: 1 | First quartile: 1.5 | Median: 3 | ' +
            'Third quartile: 4.5 | Maximum: 5' ==
            EDA_computation.seven_number_summary([1, 2, 3, 4, 5]))
    assert ('Mean: 1.0 | Standard Deviation: 0.0 | Minimum: 1 | ' +
            'First quartile: 1.0 | Median: 1 | Third quartile: 1.0 | ' +
            'Maximum: 1' ==
            EDA_computation.seven_number_summary([1, 1, 1, 1, 1]))
    assert ('Mean: 15.0 | Standard Deviation: 5.477225575051661 ' +
            '| Minimum: 5 | First quartile: 13 | Median: 15 | ' +
            'Third quartile: 17 | Maximum: 25' ==
            EDA_computation.seven_number_summary([5, 13, 14, 15, 16, 17, 25]))


def test_sorting_data() -> None:
    """
    Test the sorting_data method
    """
    import pandas as pd
    df = pd.DataFrame({'A': [3, 1, 2]})
    sorted_list = EDA_computation.sorting_data(df, 'A')
    assert (sorted_list == [1, 2, 3])


def main():
    test_median()
    test_summary()
    test_sorting_data()
    print('hi')


if __name__ == '__main__':
    main()
