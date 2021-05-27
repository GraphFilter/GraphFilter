import numpy
import numpy as np


class Invariant:
    dic_name_inv = {}
    name = None
    code = None
    is_a_function = None

    @staticmethod
    def calculate(**kwargs):
        pass


class UtilsToInvariants:

    @staticmethod
    def approx_to_int(number, error=0.00001):
        if abs(round(number) - number) <= error:
            return float(round(number, ndigits=5))
        else:
            return round(number, ndigits=5)

    @staticmethod
    def approx_array_to_int(array):
        if isinstance(array, list):
            for index, x in enumerate(array):
                array[index] = UtilsToInvariants.approx_to_int(x)
        if isinstance(array, np.ndarray):
            for index, x in np.ndenumerate(array):
                array[index] = UtilsToInvariants.approx_to_int(x)
        return array

    @staticmethod
    def is_there_integer(group):
        for number in group:
            if UtilsToInvariants.approx_to_int(number).is_integer():
                return True
        return False

    @staticmethod
    def is_integer(number):
        return UtilsToInvariants.approx_to_int(number).is_integer()

    @staticmethod
    def integral(group):
        for number in group:
            if not UtilsToInvariants.approx_to_int(number).is_integer():
                return False
        return True

    @staticmethod
    def print(value):
        precision = 5
        if isinstance(value, tuple):
            vectors = value[1]
            spectrum = ''
            for i, x in enumerate(value[0]):
                if UtilsToInvariants.is_integer(x):
                    spectrum = spectrum + f'{int(x)} \u2192 V{i}={vectors[:][i].tolist()} \n'
                else:
                    spectrum = spectrum + f'{np.around(x, decimals=precision)} \u2192 v{i}={vectors[:][i].tolist()} \n'
            return spectrum
        if isinstance(value, list):
            values = []
            for x in value:
                if UtilsToInvariants.is_integer(x):
                    values.append(int(x))
                else:
                    values.append(np.around(x, decimals=precision))
            return str(values)
        if isinstance(value, numpy.ndarray):
            return np.array2string(value, precision=precision)
        if isinstance(value, dict):
            return ' | '.join(f'{x}: {np.around(y, decimals=precision)}' for x, y in value.items())
        if isinstance(value, (bool, str, set)):
            return str(value)
        else:
            if value == 10 ^ 10:
                return 'infinite'
            else:
                return str(np.around(value, precision))

    @staticmethod
    def max_line_of_string(text: str):
        list_text = str(text).split("\n")
        return len(max(list_text, key=len))
