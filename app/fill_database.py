""" Fill_database file """
import requests
import mysql.connector

import analysis_request_data as ad
import product as prod
import category as cat

from constants import CATEGORYS

cnx = mysql.connector.connect(
    user='USER_A', password='USER_A', database='Alimentation')
cursor = cnx.cursor(buffered=True)

### INITIALIZE ANALYSIS METHODES ###
analysis = ad.Analysis_data()
product = prod.Product()


def load_data(category):

    ### TRUNCATE URI ###
    url_begin = 'https://fr.openfoodfacts.org/categorie'
    nb_page = 1
    url_end = 'json'
    url = "{}/{}/{}.{}".format(url_begin, category, nb_page, url_end)

    ### INITIALIZE CLASS FOR BUILD OBJECT ###

    ### INITIALIZE VAR nb_of_products ###
    nb_of_products = 0

    while nb_of_products < 20:

        ### BUILD URL FOR REQUEST ###
        url = "{}/{}/{}.{}".format(url_begin, category, nb_page, url_end)
        ### REQUEST ###
        response = requests.get(url)
        products = response.json()

        ### INITIALIZE ATTRIBUTS FOR PRODUCT ###
        product_name = None
        nutriscore = None
        product_url = None
        stores = None

        ### LOOP FOR BUILD PRODUC OBJECT ###
        for prod in products["products"]:

            product_name = prod.get("product_name_fr", None)
            nutriscore = prod.get("nutrition_grade_fr", None)
            stores = prod.get("stores", None)
            product_url = prod.get("url", None)
            p_data = (product_name, nutriscore, stores, product_url)

            ### ANALYSIS EMPTY FIELD, DUPLICATE NAME AND DUPLICATE URL ###
            analysis_p_data = analysis.data_checking(p_data)

            ### DATA IS OK (TRUE) ADD IT TO DATABASE ###
            if analysis_p_data is True:
                product.add(product_name, nutriscore, stores, product_url)
                ### ADD product TO VAR (TO EXIT THE LOOP) ###
                nb_of_products += 1

        nb_page += 1

    ### AFTER ADDING PRODUCTS OF THE SAME CATEGORY ###
    ### INITIALIZE CATEGORY AND ADD IT INTO DB ###
    ### AND UPDATE category_id INTO TABLE Product ###
    categ = cat.Category()
    categ.add(category)
    categ.update(category)


if __name__ == "__main__":

    ### LOOP FOR LOAD ALL CATEGORYS ONE BY ONE ###
    for category in CATEGORYS:
        load_data(category)

    print("Les données ont été remplacé par de nouvelles données")
