import json
import pymysql

db = pymysql.connect("localhost","root","","agile" )

cursor = db.cursor()



with open('parsed.json' , 'r') as reader:
    jf = json.loads(reader.read())

print(jf)
dict = jf


for item in jf:
    item_no = item['item_no']
    # print(item_no)
    qty = item['qty']
    # print(qty)
    price = item['price_per_item']
    rid = item['retailer_id']
    date = item['expected_shipment_date']
    mid = item['manufacturer_id']
    # print(item_no, qty, price, rid, date, mid)

    sql = "insert into parsed (item_no, expected_shipment_date, qty, price_per_item, manufacturer_id, retailer_id) values (%s,%s,%s,%s,%s,%s)"
    var = (item_no, date, int(qty), int(price), mid, rid)
    # print(var)

    cursor.execute(sql, var)

    db.commit()

    # all = cursor.fetchall()
    #
    # print(all)

    # db.close()

    print(item)