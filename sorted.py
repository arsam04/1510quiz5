def is_sorted(list):
    """

    :param List:
    :return:
    >>> unsorted_list = [5, 5, 5,3]
    >>> sorted_list = ["A", "B", "C", "a"]

    >>> is_sorted(unsorted_list)
    False
    >>> is_sorted(sorted_list)
    True
    """
    index = 0
    while index <= len(list) - 2:
        if list[index] > list[index + 1]:
            sorted_check = False
            break
        else:
            sorted_check = True
            index += 1

    return sorted_check


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
