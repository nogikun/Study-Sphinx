"""
This module provides a Calculator class for basic arithmetic operations.
"""

from typing import Union


class Calculator:
    """
    四則演算を行うクラス
    """

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        加算を行う関数

        Args:
            a (_type_): 数値1
            b (_type_): 数値2

        Returns:
            _type_: 加算結果
        """
        return a + b

    def sub(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        減算を行う関数

        Args:
            a (_type_): 数値1
            b (_type_): 数値2

        Returns:
            _type_: 減算結果
        """
        return a - b

    def mul(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        乗算を行う関数

        Args:
            a (Union[int, float]): 数値1
            b (Union[int, float]): 数値2

        Returns:
            Union[int, float]: 乗算結果
        """
        return a * b

    def div(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        除算を行う関数

        Args:
            a (Union[int, float]): 数値1
            b (Union[int, float]): 数値2

        Returns:
            Union[int, float]: 除算結果
        """


if __name__ == "__main__":
    calc = Calculator()

    print("加算：")
    print(calc.add(1, 2))
    print("減算：")
    print(calc.sub(1, 2))
    print("乗算：")
    print(calc.mul(1, 2))
    print("除算：")
    print(calc.div(1, 2))
