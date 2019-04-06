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

                debug_cursor = db.cursor()
                debug_cursor.execute("select exp_key from man where qty <= 0")
                debug = debug_cursor.fetchall()
                for d in debug:
                    debug_cursor.execute("DELETE FROM man WHERE exp_key = %s", d)
    print("-----------------------------------")
    order_cursor = db.cursor()
    order_cursor.execute("select * from man where handle = 0")
    qorder = order_cursor.fetchall()

    for q in qorder:
        print(q[0], q[1], int(q[2]), q[3], q[5].strftime("%Y-%m-%d %H:%M:%S"))
    print("-----------------------------------")

    if qorder == None:
        print("There are no any order left.")
        main()
    else:
        order = input("Order ID: ")
        cursor2 = db.cursor()
        if cursor2.execute("select * from man where exp_key = %s", order):
            amount = input("How many? ")
            cursor_minus = db.cursor()
            cursor_minus.execute("select man.exp_key, man.item_no, inv.amount from inv join man on inv.product_id = man.item_no where exp_key = %s", order)
            inventory = cursor_minus.fetchone()
            if int(amount) > int(inventory[2]):
                print("Cannot not supply, not enough stock")
                main()
            else:
                reduction = int(inventory[2]) - int(amount)

                print("Which time slot? ")
                cursor4 = db.cursor()
                cursor4.execute("select * from time where available = 1")
                query = cursor4.fetchall()
                print("-----------------------------------")
                for q in query:
                    print(q[0], q[1].strftime("%Y-%m-%d %H:%M:%S"), q[2])
                print("-----------------------------------")
                time = input("Time slot ID: ")

                selecttime = db.cursor()
                selecttime.execute("select timeslot from time where time_id = %s", time)
                query2 = selecttime.fetchone()
                # update the inventory level----------------------------------------------------------------
                cursor_update1 = db.cursor()
                cursor_update1.execute("UPDATE inv SET amount = %s WHERE product_id = %s", (reduction, inventory[1]))
                db.commit()
                # update the order----------------------------------------------------------------
                cursor_update2 = db.cursor()
                cursor_update2.execute("update man set handle = 1 where exp_key = %s", inventory[0])
                db.commit()
                # update the selected time slot----------------------------------------------------------------
                updatetime = db.cursor()
                updatetime.execute("UPDATE time SET available = 0 WHERE time_id = %s", time)
                db.commit()
                # export to csv file----------------------------------------------------------------
                print("You are going to deliver " + amount + " piece of " + order + " on " + str(query2[0]))
                ex = input("Add to delivery queue? y/N? ")
                cursor3 = db.cursor()
                cursor3.execute(
                    "SELECT man.item_no, man.retailer_id, man.exp_key, time.timeslot FROM man JOIN time ON man.exp_key = %s WHERE time.time_id = %s", (order, time))
                query3 = cursor3.fetchone()
                if ex == 'y':
                    cursor_indeliv = db.cursor()
                    newtime = query3[3].strftime("%Y-%m-%d %H:%M:%S")
                    sql = "insert into delivery (item_id, retailer_id, order_id, timeslot) VALUES (%s,%s,%s,%s)"
                    var = (query3[0], query3[1], query3[2], newtime)
                    cursor_indeliv.execute(sql, var)
                    db.commit()
                    # generate the csv file with date----------------------------------------------------------------
                    date = str(datetime.datetime.now().date())
                    filename = date+"output.csv"
                    with open(filename, 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([query3[0], query3[1], query3[2], query3[3].strftime("%Y-%m-%d %H:%M:%S")])
                    print("Done. Added to the csv file.")
                    main()

        else:
            print("Your inventory do not have this item.")
            main()

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

                debug_cursor = db.cursor()
                debug_cursor.execute("select exp_key from man where qty <= 0")
                debug = debug_cursor.fetchall()
                for d in debug:
                    debug_cursor.execute("DELETE FROM man WHERE exp_key = %s", d)

        cursor.execute("select * from man where handle = 0")
        query = cursor.fetchall()
        for q in query:
            print(q[0], q[1], int(q[2]), q[3], q[5].strftime("%Y-%m-%d %H:%M:%S"))

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