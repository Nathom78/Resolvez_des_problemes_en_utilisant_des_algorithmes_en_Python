import pandas as pd
# import timeit  # pour calcul du temps execution
from datetime import datetime

MAX_EXPENDITURE = 500
FILEPATH = "data/Partie1_virgules - Copie.csv"


def read_file():
    """
    Viens lire et mettre en forme le fichier de la premiere partie dans le repertoire Data
    :return: Dataframe du premier fichier
    """

    def pourcent(x):
        return float(x.replace("%", "")) / 100

    part_one = pd.read_csv(FILEPATH, names=["stock", "price", "profit"], header=0,
                           converters={"profit": pourcent})
    return part_one


def delete_bad_data(array_data):
    new_list = tuple()
    for action in array_data:
        if action[1] <= 0:
            continue
        elif action[1] > 0:
            new_list += (action,)
    return new_list


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
    debut = datetime.now()
    print("Heure de début", str(debut))
    # Lecture du fichier
    dataframe = read_file()
    # rajout d'une colonne montant du profit
    dataframe["profit_amount"] = dataframe["price"] * dataframe["profit"]
    dataframe["profit_amount"].round(decimals=2)

    sorted_actions = best_actions(dataframe).to_numpy()

    filtered_actions = delete_bad_data(sorted_actions)

    tuple_actions = take_best_for_max(filtered_actions)

    # remise en DataFrame de la liste de résultats
    pd_best_combination = pd.DataFrame(tuple_actions, columns=["stock", "price", "profit", "profit_amount"])
    # Sommes des profits et des prix des différentes actions
    # ajout de la ligne total au tableau des résultats
    row_total = {"stock": ["total"], "price": [pd_best_combination["price"].sum()],
                 "profit_amount": [pd_best_combination["profit_amount"].sum()]}
    df_row_total = pd.DataFrame(row_total)
    sum_profit = [pd_best_combination, df_row_total]
    total = pd.concat(sum_profit)
    print(total.sort_values(by=["stock"]))
    fin = datetime.now()
    print("Heure de fin", str(fin))
    print("Fait en", str(fin - debut))


if __name__ == '__main__':
    # test4 = timeit.Timer(main)
    # print(test4.timeit(10))
    main()
