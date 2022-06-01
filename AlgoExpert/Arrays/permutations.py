


def get_permutations(lst):
    """Get all permutations of a list.

    Args:
        lst (List): Input List

    Returns:
        List: List of permutations
    """
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i, value in enumerate(lst):

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        rem_lst = lst[:i] + lst[i+1:]

        # Generating all permutations where m is first
        # element
        for p in get_permutations(rem_lst):
            l.append([value] + p)
    return l


if __name__ == '__main__':
    print(get_permutations([1, 2, 3]))
