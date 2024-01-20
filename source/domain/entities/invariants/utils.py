import numpy as np
import numpy.linalg as la


def approx_to_int(number, error=10 ** -8):
    if abs(round(number) - number) <= error:
        return float(round(number, ndigits=5))
    else:
        return round(number, ndigits=5)


def approx_array_to_int(array):
    if isinstance(array, list):
        for index, x in enumerate(array):
            array[index] = approx_to_int(x)
    if isinstance(array, np.ndarray):
        for index, x in np.ndenumerate(array):
            array[index] = approx_to_int(x)
    return np.around(array, decimals=5)


def is_there_integer(group):
    for number in group:
        if approx_to_int(number).is_integer():
            return True
    return False


def is_integer(number):
    return approx_to_int(number).is_integer()


def integral(group):
    for number in group:
        if not approx_to_int(number).is_integer():
            return False
    return True


def print_matrix(value, precision):
    if type(value) is str:
        return value
    return np.array2string(value, precision=precision, separator=" ")


def print_dict(value, precision):
    if type(value) is str:
        return value
    else:
        return ' | '.join(f'{x}: {np.around(y, decimals=precision)}' for x, y in value.items())


def print_eigenvectors_and_eigenvalues(value, precision):
    vectors = value[1]
    spectrum_value = ''
    if type(value) is str:
        return value
    for i, x in enumerate(value[0]):
        if is_integer(x):
            spectrum_value = spectrum_value + f"{round(x)} \u2192 V{i} ={vectors[:, i].tolist()} \n"
        else:
            spectrum_value = spectrum_value + \
                             f'{np.around(x, decimals=precision)} \u2192 V{i}={vectors[:, i].tolist()} \n'
    return spectrum_value


def print_list(value, precision):
    values = []
    if type(value) is str:
        return value
    for x in value:
        if is_integer(x):
            values.append(round(x))
        else:
            values.append(np.around(x, decimals=precision))
    return str(values)


def print_numeric(value, precision):
    if value == 10 ** 10:
        return 'infinite'
    else:
        return str(np.around(value, precision))


def print_boolean(value, precision):
    return str(value)


def print_set(set_values, precision):
    return f"value= {len(set_values)}, set= " + np.array2string(np.array(set_values),
                                                                precision=precision,
                                                                separator=" , "
                                                                )


def max_line_of_string(text: str):
    list_text = str(text).split("\n")
    return len(max(list_text, key=len))


def main_eigenvalue(matrix: np.ndarray):
    eigenvalues, vectors = la.eigh(matrix)
    eigenvalues = np.around(eigenvalues, decimals=10)
    vectors = np.around(vectors, decimals=10)
    one = np.ones(matrix.shape[0])
    mains = set()
    for i, value in enumerate(eigenvalues):
        if approx_to_int(np.dot(one, vectors[:, i])) != 0:
            mains.add(value)
    return mains


def spectrum(matrix: np.ndarray):
    return approx_array_to_int(la.eigvalsh(matrix).tolist())


def largest_eigen(matrix: np.ndarray):
    return approx_array_to_int(la.eigvalsh(matrix).tolist())[matrix.shape[0] - 1]


def second_largest_eigen(matrix: np.ndarray):
    return approx_array_to_int(la.eigvalsh(matrix).tolist())[matrix.shape[0] - 2]


def smallest_eigen(matrix: np.ndarray):
    return approx_array_to_int(la.eigvalsh(matrix).tolist())[0]


def eigenvectors(matrix: np.ndarray):
    values, vectors = la.eigh(matrix)
    return values, approx_array_to_int(vectors)


def energy(matrix: np.ndarray):
    trace = matrix.trace()
    eig = spectrum(matrix)
    return sum([np.absolute(x - (float(trace) / float(matrix.shape[0]))) for x in eig])
