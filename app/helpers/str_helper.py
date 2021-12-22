import re
from typing import Union


class StrHelper:
    @staticmethod
    def total_count(value: Union[str, int], lst: list) -> int:
        """Get total count given a value in a list.

        Parameters
        ----------
        value : int or str
            Value to find.

        lst : list
            A list to check if the value is in it.

        Returns
        -------
        lst : list
            Posible values.

        Example
        -------
        >>> StrHelper.total_count(1, [1, 1, 1, 2, 2, 3, 4])
        3

        """
        total = 0
        for item in lst:
            if value == item:
                total += 1
        return total

    @staticmethod
    def pascal_case_to_normal_case(input: str) -> Union[str, None]:
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', input)
