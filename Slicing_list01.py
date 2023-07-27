def main(numbers):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    return numbers[::2]
print(main([1,3,4,7,77]))