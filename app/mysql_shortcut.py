""" LIBRAIRIES OF SQL SHORTCUT """

import mysql.connector

# MySql SHORTCUT

cnx = mysql.connector.connect(
    user='USER_A', password='USER_A', database='Alimentation')
cursor = cnx.cursor(buffered=True)

# Mysql instructions

add_product    = ("INSERT INTO Product "
                  "(product_name, nutriscore, stores, url) "
                  "VALUES (%s, %s, %s, %s)")
add_category   = ("INSERT INTO Category "
                  "(id, category_name) "
                  "VALUES (%s, %s)")
fill_sub_table = ("INSERT INTO Substitute"
                  "(product_id, substituted_id)"
                  "VALUES(%s, %s)")

update_category_id = ("UPDATE Product set category_id = '%s' WHERE category_id IS NULL")

query_product_data           = ("SELECT id, product_name, nutriscore, stores, url FROM Product WHERE id = '{}'")
query_substituted_data       = ("SELECT product_name, nutriscore, url FROM Product WHERE id = {}")
query_category_id            = ("SELECT id FROM Category WHERE category_name = '{}' ")
query_prod_where_cat_id      = ("SELECT id, product_name, nutriscore FROM Product WHERE category_id = '{}' ORDER BY id")
query_prod_id_where_cat_id   = ("SELECT id FROM Product WHERE category_id = '{}' ")
query_nutr_where_prod_id     = ("SELECT nutriscore FROM Product WHERE id = '{}' ")
query_best_nutr_from_prod    = ("SELECT id, nutriscore FROM Product WHERE nutriscore = '{}' AND category_id = '{}'")
query_all_id_from_cat        = ("SELECT id FROM Category")
query_all_sub_id_from_sub    = ("SELECT substituted_id FROM Substitute")
query_all_prd_id_from_sub    = ("SELECT product_id FROM Substitute")
query_category               = ("SELECT * FROM Category ORDER BY id")
query_sub                    = ("SELECT product_name, nutriscore, stores, url, substituted_id "
                                "FROM Product INNER JOIN Substitute ON Product.id = Substitute.product_id")

del_sub_tab = ("DELETE FROM Substitute")
