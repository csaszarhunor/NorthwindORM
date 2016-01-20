# -*- coding: utf-8 -*-
from customer import Customer
import pprint
import mysql.connector


def get_csv_rows(file_loc):
    with open(file_loc, 'r', encoding="utf8") as file:
        rows = file.read().splitlines()
    return rows[1:len(rows)]


def get_db_records(cursor_obj, table):
    cursor_obj.execute("SELECT * FROM {}".format(table))
    records = cursor_obj.fetchall()
    csv_rows = []
    for rec in records:
        row = ""
        for column in rec:
            if column == None:
                row += ";"
            else:
                row += column + ";"
        csv_rows.append(row[:-1])
    return csv_rows


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


def export_to_csv(db_table, clss, csv_loc):
    cnx = mysql.connector.connect(user='root', password="F0i1b1o2n3a5c8c13i21", database='northwind')
    cursor = cnx.cursor()
    csv_rows = get_db_records(cursor, db_table)
    with open(csv_loc, 'w', encoding="utf8") as csv_file:
        for row in csv_rows:
            csv_file.write(row + "\n")
    cursor.close()
    cnx.close()

