class StrHelper:
    @staticmethod
    def total_count(value, lst: list) -> int:
        """Get total count from a value searched in a list.

        Parameters
        ----------
        value : int or str
            Value to find.

        lst : list
            A list to check if the value is in it.

        Return
        ------
        lst : list
            Duplicated values.

        Example
        -------
        >>> StrHelper.total_count([1, 1, 1, 2, 2, 3, 4])
        [1, 2]

        """
        total = 0
        for item in lst:
            if value == item:
                total += 1
        return total
