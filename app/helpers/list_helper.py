from collections import Counter


class ListHelper:
    @staticmethod
    def duplicates(lst: list) -> list:
        """Get only duplicated values from a list.

        Parameters
        ----------
        lst : list
            TODO: pending to define

        Returns
        -------
        lst : list
            Duplicated values.

        Example
        -------
        >>> ListHelper.duplicates([1, 1, 1, 2, 2, 3, 4])
        [1, 2]

        """
        return [item for item, count in Counter(lst).items() if count > 1]
