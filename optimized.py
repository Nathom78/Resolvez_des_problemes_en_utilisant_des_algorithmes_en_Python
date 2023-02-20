import pandas as pd
# import timeit  # pour calcul du temps execution
from datetime import datetime

MAX_EXPENDITURE = 500


def read_file():
    """
    Viens lire et mettre en forme le fichier de la premiere partie dans le repertoire Data
    :return: Dataframe du premier fichier
    """

    def pourcent(x):
        return int(x.replace("%", "")) / 100

    part_one = pd.read_csv("data/Partie1_virgules - Copie.csv", names=["stock", "price", "profit"], header=0,
                           converters={"profit": pourcent})
    return part_one


def best_actions(all_actions):
    new_list = all_actions.sort_values(ascending=False, by=["profit"])
    return new_list


def take_best_for_max(array_action):
    tuple_best = tuple()
    price = 0
    for action in array_action:
        price += action[1]
        if price <= MAX_EXPENDITURE:
            tuple_best += (action,)
        else:
            price -= action[1]
    return tuple_best


def main():
    dataframe = read_file()
    # rajout d'une colonne montant du profit
    dataframe["profit_amount"] = dataframe["price"] * dataframe["profit"]
    dataframe["profit_amount"].round(decimals=2)
    sorted_actions = best_actions(dataframe).to_numpy()
    tuple_actions = take_best_for_max(sorted_actions)

    pd_best_combination = pd.DataFrame(tuple_actions, columns=["stock", "price", "profit", "profit_amount"])
    row_total = {"stock": ["total"], "price": [pd_best_combination["price"].sum()],
                 "profit_amount": [pd_best_combination["profit_amount"].sum()]}
    df_row_total = pd.DataFrame(row_total)
    sum_profit = [pd_best_combination, df_row_total]
    total = pd.concat(sum_profit)
    print(total)


if __name__ == '__main__':
    # test4 = timeit.Timer(main)
    # print(test4.timeit(10))
    main()
