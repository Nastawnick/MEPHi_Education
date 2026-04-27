def filter_above_threshold(numbers: list, threshold: float) -> list:
    try:
        answer = [i for i in numbers if float(i)>threshold]
    except (ValueError, TypeError) as error:
        raise type(error)('В списке должны быть только числа, а в качестве порогового значения - дробное число')
    return answer
