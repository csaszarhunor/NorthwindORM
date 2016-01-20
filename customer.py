class Customer:

    customerID = ""
    company_name = ""
    contact_name = ""
    contact_title = ""
    address = ""
    city = ""
    region = ""
    postal_code = ""
    country = ""
    phone = ""
    fax = ""

    @staticmethod
    def parse(csv_row: str):
        data = csv_row.split(';')
        Customer.customerID = data[0]
        Customer.company_name = data[1]
        Customer.contact_name = data[2]
        Customer.contact_title = data[3]
        Customer.address = data[4]
        Customer.city = data[5]
        Customer.region = data[6]
        Customer.postal_code = data[7]
        Customer.country = data[8]
        Customer.phone = data[9]
        Customer.fax = data[10]
        return Customer

    def persist(self):
        pass

    @staticmethod
    def to_csv():
        csv_row = Customer.customerID + ';' + Customer.company_name + ';' + Customer.contact_name + ';' + \
                  Customer.contact_title + ';' + Customer.address + ';' + Customer.city + ';' + Customer.region + ';' +\
                  Customer.postal_code + ';' + Customer.country + ';' + Customer.phone + ';' + Customer.fax
        return csv_row

    @staticmethod
    def store_in_db(cursor_obj, table):
        insert = "INSERT INTO {} VALUES ('".format(table) + Customer.customerID + "', '" + Customer.company_name + \
                 "', '" + Customer.contact_name + "', '" + Customer.contact_title + "', '" + Customer.address + "', '" \
                 + Customer.city + "', '" + Customer.region + "', '" + Customer.postal_code + "', '" + Customer.country\
                 + "', '" + Customer.phone + "', '" + Customer.fax + "')"
        cursor_obj.execute(insert)
