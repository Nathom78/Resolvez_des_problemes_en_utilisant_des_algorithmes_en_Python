import pandas as pd
# import timeit  # pour calcul du temps execution
from datetime import datetime

MAX_EXPENDITURE = 500
FILEPATH = "data/Partie1_virgules - Copie.csv"


def read_file():
    """
    Viens lire et mettre en forme le fichier de la premiere partie dans le repertoire Data"
    :return: Dataframe du premier fichier
    """
    def pourcent(x):
        return float(x.replace("%", "")) / 100

    part_one = pd.read_csv(FILEPATH, names=["stock", "price", "profit"], header=0,
                           converters={"profit": pourcent})
    return part_one


def combinations(iterable, r):
    """
    'R' length subsequences, of elements from the input iterable.
    :param iterable:
    :param r:
    :return: tuple()
    """
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def algorithme():
    """
    :return: list(tuple(numpy.ndarray))
    """
    dataframe = read_file()
    dataframe["profit_amount"] = dataframe["price"] * dataframe["profit"]
    dataframe["profit_amount"].round(decimals=2)
    array_data = dataframe.to_numpy()
    combinations_result = []

    for n in range(1, len(array_data) + 1):
        combinations_result += combinations(array_data, n)
    return combinations_result


def filter_for_max(list_result):
    list_filtered = []

    def less_than(actions):
        add_price = 0
        if len(actions) > 1:
            for action in actions:
                add_price += action[1]
        else:
            add_price = actions[0][1]
        return add_price < MAX_EXPENDITURE

    for tuple_actions in list_result:
        combination_array = tuple(filter(less_than, (tuple_actions,)))
        list_filtered += combination_array

    return list_filtered


def best_profit(filtered_list):
    def sum_profit(actions):
        add_profit = 0
        if len(actions) > 1:
            for action in actions:
                add_profit += action[3]
        else:
            add_profit = actions[0][3]
        return add_profit

    new_list = sorted(filtered_list, key=sum_profit, reverse=True)
    best_combination = tuple(new_list[0])
    return best_combination


def main():
    # pour calcul du temps de l'algorithme
    # test3 = timeit.Timer(algorithme)
    # print(test3.timeit(10))
    debut = datetime.now()
    print("Heure de début", str(debut))
    combinations_possible = algorithme()
    print("combinaisons, faites", str(datetime.now()))
    list_filtered = filter_for_max(combinations_possible)
    print("portefeuilles trop chers écartés", str(datetime.now()))
    best_combination = best_profit(list_filtered)
    print("trie pour le meilleur, ok", str(datetime.now()))
    # Rajout à la meilleure combinaison d'une ligne pour le total
    pd_best_combination = pd.DataFrame(best_combination, columns=["stock", "price", "profit", "profit_amount"])
    row_total = {"stock": ["total"], "price": [pd_best_combination["price"].sum()],
                 "profit_amount": [pd_best_combination["profit_amount"].sum()]}
    df_row_total = pd.DataFrame(row_total)
    sum_profit = [pd_best_combination, df_row_total]
    total = pd.concat(sum_profit)

    print("best combination :\n", total)
    fin = datetime.now()
    print("Heure de fin", str(fin))
    print("Fait en", str(fin-debut))


if __name__ == '__main__':
    # test4 = timeit.Timer(main)
    # print(test4.timeit(10))
    main()
