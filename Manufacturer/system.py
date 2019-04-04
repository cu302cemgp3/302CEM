import pymysql
import datetime
import csv
import urllib.request, json
import warnings

def inv():
    print("-----------------------------------\n"
          "------------Stock Level------------\n"
          "-----------------------------------\n")
    db = pymysql.connect("localhost", "root", "", "agile")
    cursor = db.cursor()
    cursor.execute("select * from inv")
    query = cursor.fetchall()
    for q in query:
        print(q)
    main()

def shipping():
    print("-----------------------------------\n"
          "-------------Time Slot-------------\n"
          "-----------------------------------\n")
    db = pymysql.connect("localhost", "root", "", "agile")
    cursor = db.cursor()
    cursor.execute("select * from time where available = 1")
    query = cursor.fetchall()
    for q in query:
        print(q[0], q[1].strftime("%m/%d/%Y, %H:%M:%S"), q[2])
    main()

def arrange():
    db = pymysql.connect("localhost", "root", "", "agile")
    cursor = db.cursor()
    print("Which order?")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url="https://302.winkoxd.com/manufacturer.php", headers=headers)
    with urllib.request.urlopen(req) as url:
        file_data = json.loads(url.read().decode())
        for i in file_data:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
            # print(i)
                exp_key = i['exp_key']
                item_no = i['item_no']
                qty = i['qty']
                price = i['price_per_item']
                rid = i['retailer_id']
                date = i['expected_shipment_date']
                mid = i['manufacturer_id']

                sql = "insert ignore into man (exp_key, item_no, expected_shipment_date, qty, price_per_item, manufacturer_id, retailer_id) values (%s,%s,%s,%s,%s,%s,%s)"
                var = (exp_key, item_no, date, qty, price, mid, rid)

                cursor.execute(sql, var)

                db.commit()

    order_cursor = db.cursor()
    order_cursor.execute("select * from man where handle = 0")
    qorder = order_cursor.fetchall()
    for q in qorder:
        print(q)
    order = input("Order ID: ")
    cursor2 = db.cursor()
    if cursor2.execute("select * from man where exp_key = %s", order):
        # query = cursor2.fetchone()
        # cursor2.close()
        amount = input("How many? ")
        cursor_minus = db.cursor()
        cursor_minus.execute("select man.exp_key, man.item_no, inv.amount from inv join man on inv.product_id = man.item_no where exp_key = %s", order)
        inventory = cursor_minus.fetchone()
        reduction = int(inventory[2]) - int(amount)
        cursor_update1 = db.cursor()
        cursor_update1.execute("UPDATE inv SET amount = %s WHERE product_id = %s", (reduction, inventory[1]))
        db.commit()
        cursor_update2 = db.cursor()
        cursor_update2.execute("update man set handle = 1 where exp_key = %s", inventory[0])
        db.commit()
        print("Which time slot? ")
        cursor4 = db.cursor()
        cursor4.execute("select * from time where available = 1")
        query = cursor4.fetchall()
        for q in query:
            print(q[0], q[1].strftime("%m/%d/%Y, %H:%M:%S"), q[2])
        time = input("Time slot ID: ")

        cursor5 = db.cursor()
        cursor5.execute("UPDATE time SET available = 0 WHERE time_id = %s", time)
        db.commit()
        cursor6 = db.cursor()
        cursor6.execute("select timeslot from time where time_id = %s", time)
        query2 = cursor6.fetchone()

        print("You are going to deliver " + amount + " piece of " + order + " on " + str(query2[0]))
        ex = input("Add to delivery queue? y/N? ")
        cursor3 = db.cursor()
        cursor3.execute(
            "SELECT man.item_no, man.retailer_id, man.exp_key, time.timeslot FROM man JOIN time ON man.exp_key = %s WHERE time.time_id = %s", (order, time))
        query3 = cursor3.fetchone()
        if ex == 'y':
            cursor_indeliv = db.cursor()
            print(query3[0])
            print(query3[1])
            print(query3[2])
            print(query3[3])
            print(query3)
            # var = (query3[0], query3[1], query3[2], query3[3])
            # sql = cursor_indeliv.execute("INSERT INTO `delivery`(`item_id`, `retailer_id`, `order_id`, `timeslot`) VALUES ('%s','%s','%s','%s')", var)
            # print(sql)
            date = str(datetime.datetime.now().date())
            filename = date+"output.csv"
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in query3:
                    writer.writerow(str(row))

    else:
        print("no such item")

def vieworder():
    print("-----------------------------------\n"
          "-------------View Order------------\n"
          "-----------------------------------\n")
    db = pymysql.connect("localhost", "root", "", "agile")
    cursor = db.cursor()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url="https://302.winkoxd.com/manufacturer.php", headers=headers)
    with urllib.request.urlopen(req) as url:
        file_data = json.loads(url.read().decode())
        for i in file_data:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                # print(i)
                exp_key = i['exp_key']
                item_no = i['item_no']
                qty = i['qty']
                price = i['price_per_item']
                rid = i['retailer_id']
                date = i['expected_shipment_date']
                mid = i['manufacturer_id']

                sql = "insert ignore into man (exp_key, item_no, expected_shipment_date, qty, price_per_item, manufacturer_id, retailer_id) values (%s,%s,%s,%s,%s,%s,%s)"
                var = (exp_key, item_no, date, qty, price, mid, rid)

                cursor.execute(sql, var)

                db.commit()

        cursor.execute("select * from man where handle = 0")
        query = cursor.fetchall()
        for q in query:
            print(q)

    main()


def main():
    print("\n"
          "--Manufacturer management system---")
    userinput = input("1 View Order\n"
                      "2 Stock Level\n"
                      "3 Shipping Time slot\n"
                      "4 Arrange\n"
                      "5 Exit\n"
                      "-----------------------------------\n"
                      "Your choice: ")

    if userinput == '1':
        vieworder()
    elif userinput == '2':
        inv()
    elif userinput == '3':
        shipping()
    elif userinput == '4':
        arrange()
    else:
        exit()

if __name__ == '__main__':
    main()