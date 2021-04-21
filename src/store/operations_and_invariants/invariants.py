class Invariant:
    dic_name_inv = {}
    name = None

    @staticmethod
    def calculate(**kwargs):
        pass

class Utils:

    @staticmethod
    def approx_to_int(number, error=0.00001):
        if abs(round(number) - number) <= error:
            return float(round(number))
        else:
            return number

    @staticmethod
    def is_there_integer(group):
        for number in group:
            if Utils.approx_to_int(number).is_integer():
                return True
        return False

    @staticmethod
    def is_integer(number):
        return Utils.approx_to_int(number).is_integer()

    @staticmethod
    def integral(group):
        for number in group:
            if not Utils.approx_to_int(number).is_integer():
                return False
        return True