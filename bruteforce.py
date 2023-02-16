from pandas import read_csv as rf


# import timeit # pour calcul du temps d' execution


def read_file():
    """
    Viens lire et mettre en forme le fichier de la premiere partie dans le repertoire Data"
    :return: Dataframe du premier fichier
    """

    def pourcent(x):
        return int(x.replace("%", "")) / 100

    part_one = rf("data/Partie2_virgules - Copie.csv", names=["stock", "price", "profit"], header=0,
                  converters={"profit": pourcent})
    print(part_one)
    return part_one


def combinations(iterable, r):
    """

    :param iterable:
    :param r:
    :return: "Return r length subsequences of elements from the input iterable."
    """
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = list(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield list(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield list(pool[i] for i in indices)


def algorithme(array_data):
    """

    :return:
    """

    combinations_result = []

    for n in range(1, len(array_data) + 1):
        combinations_result += combinations(array_data, n)
    return combinations_result


def put_price(array_result, dataframe):
    price_array = []

    def replace(string_actions):
        for row in range(len(dataframe)):
            print(string_actions)
            print(str(dataframe.loc[row, "stock"]))
            if str(string_actions) == str(dataframe.loc[row, "stock"]):
                return dataframe.loc[row].to_numpy()

    print(array_result)

    # print(array_result_string)
    for tuple_actions in array_result:
        combination_array = []
        combination_array += map(replace, tuple_actions)
        price_array += tuple(combination_array[i] for i in range(len(combination_array)))

    # print(array_result_string)

    # print(price_array)
    return price_array


def main():
    dataframe = read_file()
    array_data = dataframe["stock"].to_numpy()
    # print(dataframe.to_numpy())

    # pour calcul du temps de l'algorithme
    # test3 = timeit.Timer(algorithme)
    # print(test3.timeit(10))
    result = put_price(algorithme(array_data), dataframe)
    print(result)


if __name__ == '__main__':
    main()
