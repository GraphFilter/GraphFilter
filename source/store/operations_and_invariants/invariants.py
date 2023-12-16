import numpy as np
import numpy.linalg as la


class Invariant:
    dic_name_inv = {}
    name = None
    code = None
    is_a_function = None

    @staticmethod
    def calculate(**kwargs):
        pass

    @staticmethod
    def print(**kwargs):
        pass


class UtilsToInvariants:

    @staticmethod
    def approx_to_int(number, error=10 ** -8):
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
        return np.around(array, decimals=5)

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
    def print_matrix(matrix, precision, name=""):
        if isinstance(matrix, str):
            return matrix

        if name == "Randic Matrix" or name == "Normalized Laplacian Matrix":
            formatted_rows = []
            column_widths = [max(len(f"{cell:.{precision}f}") for cell in col) for col in zip(*matrix)]

            for row in matrix:
                formatted_row = []
                for i, cell in enumerate(row):
                    width = column_widths[i]
                    formatted_cell = f"{cell:{width + 1}.{precision}f}" if cell < 0 else f" {cell:{width}.{precision}f}"
                    formatted_row.append(formatted_cell)
                formatted_rows.append(" ".join(formatted_row))

            return "\n".join(formatted_rows)
        else:
            if matrix.size > 0:
                max_cell_width = max(len(str(cell)) for row in matrix for cell in row)
                formatted_rows = []
                for row in matrix:
                    formatted_row = []
                    for cell in row:
                        if cell == float('inf') or cell == float('-inf'):
                            cell_str = f"{cell}".rjust(max_cell_width + 1)
                        else:
                            cell_str = f" {cell}" if not str(cell).startswith("-") else f"{cell}"
                            if cell_str.endswith(".0"):
                                cell_str = cell_str[:-2].ljust(max_cell_width)
                            else:
                                cell_str = cell_str.ljust(max_cell_width + 1)
                        formatted_row.append(cell_str)
                    formatted_rows.append(" ".join(formatted_row))

                return "\n".join(formatted_rows)
            else:
                return ""

    @staticmethod
    def print_dict(value, precision):
        if type(value) is str:
            return value
        else:
            return ' | '.join(f'{x}: {np.around(y, decimals=precision)}' for x, y in value.items())

    @staticmethod
    def print_eigenvectors_and_eigenvalues(value, precision):
        vectors = value[1]
        spectrum = ''
        if type(value) is str:
            return value
        for i, x in enumerate(value[0]):
            if UtilsToInvariants.is_integer(x):
                spectrum = spectrum + f"{round(x)} \u2192 V{i} ={vectors[:, i].tolist()} \n"
            else:
                spectrum = spectrum + f'{np.around(x, decimals=precision)} \u2192 V{i}={vectors[:, i].tolist()} \n'
        return spectrum

    @staticmethod
    def print_list(value, precision):
        values = []
        if type(value) is str:
            return value
        for x in value:
            if UtilsToInvariants.is_integer(x):
                values.append(round(x))
            else:
                values.append(np.around(x, decimals=precision))
        return str(values)

    @staticmethod
    def print_numeric(value, precision):
        if value == 10 ** 10:
            return 'infinite'
        else:
            return str(np.around(value, precision))

    @staticmethod
    def print_boolean(value, precision):
        return str(value)

    @staticmethod
    def print_set(set_values, precision):
        return f"value= {len(set_values)}, set= " + np.array2string(np.array(set_values),
                                                                    precision=precision,
                                                                    separator=" , "
                                                                    )

    @staticmethod
    def max_line_of_string(text: str):
        list_text = str(text).split("\n")
        return len(max(list_text, key=len))

    @staticmethod
    def main_eigenvalue(matrix: np.ndarray):
        eigenvalues, vectors = la.eigh(matrix)
        eigenvalues = np.around(eigenvalues, decimals=10)
        vectors = np.around(vectors, decimals=10)
        one = np.ones(matrix.shape[0])
        mains = set()
        for i, value in enumerate(eigenvalues):
            if UtilsToInvariants.approx_to_int(np.dot(one, vectors[:, i])) != 0:
                mains.add(value)
        return mains

    @staticmethod
    def spectrum(matrix: np.ndarray):
        return UtilsToInvariants.approx_array_to_int(la.eigvalsh(matrix).tolist())

    @staticmethod
    def largest_eigen(matrix: np.ndarray):
        return UtilsToInvariants.approx_array_to_int(la.eigvalsh(matrix).tolist())[matrix.shape[0] - 1]

    @staticmethod
    def second_largest_eigen(matrix: np.ndarray):
        return UtilsToInvariants.approx_array_to_int(la.eigvalsh(matrix).tolist())[matrix.shape[0] - 2]

    @staticmethod
    def smallest_eigen(matrix: np.ndarray):
        return UtilsToInvariants.approx_array_to_int(la.eigvalsh(matrix).tolist())[0]

    @staticmethod
    def eigenvectors(matrix: np.ndarray):
        values, vectors = la.eigh(matrix)
        return values, UtilsToInvariants.approx_array_to_int(vectors)

    @staticmethod
    def energy(matrix: np.ndarray):
        trace = matrix.trace()
        eig = UtilsToInvariants.spectrum(matrix)
        return sum([np.absolute(x - (float(trace) / float(matrix.shape[0]))) for x in eig])
