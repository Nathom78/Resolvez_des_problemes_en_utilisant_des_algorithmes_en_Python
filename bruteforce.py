from pandas import read_csv as rf


def read_file():
    """
    Viens lire et mettre en forme le fichier de la premiere partie dans le repertoire Data"
    :return: Dataframe du premier fichier
    """

    def pourcent(x):
        return int(x.replace("%", "")) / 100

    part_one = rf("data/Partie1_virgules - Copie.csv", names=["stock", "price", "profit"], header=0,
                  converters={"profit": pourcent})
    return part_one


def algorithme_part_one():
    """

    :return:
    """
    # création d'une colonne montant du benefice à 2 décimales prés
    array_data1 = read_file()
    array_data1["profit_amount"] = array_data1["price"] * array_data1["profit"]
    array_data1["profit_amount"].round(2)

    print(array_data1["profit_amount"])


algorithme_part_one()
