""" Display File """

from app.mysql_shortcut import (cursor, query_product, query_category,
                                query_prod_from_cat,
                                query_sub, query_sub_name)

from app.constants import (principal_menu, select_action_msg, small_barre,
                           menu_opt_0_msg, menu_opt_1_msg, menu_opt_2_msg,
                           barre, save_msg, save_opt_0, save_opt_1,
                           category_menu, select_cat_msg, opt_0_cat_menu,
                           space, product_msg, select_product_msg,
                           best_product_msg, replace_msg, substituted_msg)


def display_menu():

    print(principal_menu)
    print(select_action_msg)
    print(small_barre)
    print(menu_opt_0_msg)
    print(menu_opt_1_msg)
    print(menu_opt_2_msg)
    print(barre)


def display_save_msg():

    print(save_msg)
    print(small_barre)
    print(save_opt_0)
    print(save_opt_1)
    print(barre)


def display_category():

    print(category_menu)
    print(select_cat_msg)
    print(small_barre)
    print(opt_0_cat_menu)

    cursor.execute(query_category)

    for id, category_name in cursor:
        print("| ", id, " || ", category_name,
              space * (72 - len(category_name)), "|")

    print(barre)


def display_product_from_category(id_cat):

    print(product_msg)
    print(select_product_msg)
    print(small_barre)

    cursor.execute(query_prod_from_cat.format(id_cat))

    for id, product_name, nutriscore in cursor:
        print("|", id, "||", product_name,
              space * (67 - len(product_name)), "|| Nutriscore : ", nutriscore)

    print(barre)


def display_substitute_proposition(product_id, substitute_id):

    print(barre)
    print(best_product_msg)
    print(small_barre)

    cursor.execute(query_product.format(substitute_id))

    for id, product_name, nutriscore, stores, url in cursor:
        print("| Nom du produit  |   ", product_name,
              space * (59 - len(product_name)), "|")
        print("| Nutriscore      |   ", nutriscore, space * 58, "|")
        print("| Magasins        |   ", stores,
              space * (59 - len(stores)), "|", "\n| URL             |   ", url)
        print(small_barre)
        print(replace_msg)
        print(small_barre)

    cursor.execute(query_product.format(product_id))

    for id, product_name, nutriscore, stores, url in cursor:
        print("| Nom du produit  |   ", product_name,
              space * (59 - len(product_name)), "|")
        print("| Nutriscore      |   ", nutriscore, space * 58, "|")
        print("| Magasins        |   ", stores,
              space * (59 - len(stores)), "|", "\n| URL             |   ", url)
        print(small_barre)
        print(barre)


def display_substitutes():

    print(substituted_msg)

    cursor.execute(query_sub)
    list_of_sub = cursor.fetchall()

    for product_name, nutriscore, stores, url, substituted_id in list_of_sub:
        print(small_barre)
        print("| Nouveau produit |   ", product_name,
              space * (59 - len(product_name)), "|")
        print("| Nutriscore      |   ", nutriscore, space * 58, "|")
        print("| Magasins        |   ", stores,
              space * (59 - len(stores)), "|", "\n| URL             |   ", url)

        cursor.execute(query_sub_name.format(substituted_id))

        for product_name, nutriscore, url in cursor:
            print(small_barre)
            print("| Ancien produit  |   ", product_name,
                  space * (59 - len(product_name)), "|")
            print("| Nutriscore      |   ", nutriscore, space * 58, "|")
            print("| URL             |   ", url)
            print(small_barre)
            print(barre)
