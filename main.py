# -*- coding: utf-8 -*-
from customer import Customer
import pprint
import mysql.connector


def get_csv_rows(file_loc):
    with open(file_loc, 'r', encoding="utf8") as file:
        rows = file.read().splitlines()
    return rows[1:len(rows)]


def import_from_csv(csv, clss, db_table):
    cs_rows = get_csv_rows(csv)
    cnx = mysql.connector.connect(user='root', password="F0i1b1o2n3a5c8c13i21", database='northwind')
    cursor = cnx.cursor()
    for row in cs_rows:
        obj = clss.parse(row)
        try:
            obj.store_in_db(cursor, db_table)
        except mysql.connector.DataError:
            pass
        except mysql.connector.IntegrityError:
            pass
    cnx.commit()
    cursor.close()
    cnx.close()

import_from_csv("csv/customers.csv", Customer, "customersclone")
