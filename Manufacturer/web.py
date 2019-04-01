import tkinter as tk
from tkinter import filedialog
import pymysql
import urllib.request, json
import csv
import os

db = pymysql.connect("localhost","root","","agile" )

cursor = db.cursor()


root=tk.Tk()
root.withdraw()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url="https://302.winkoxd.com/manufacturer.php", headers=headers)
with urllib.request.urlopen(req) as url:
    file_data = json.loads(url.read().decode())
    # print(file_data)
    answer=input("Continue importing? Y/N: ")
    if answer=="Y":
        dict = file_data
        for item in dict:
            exp_key = item['exp_key']
            item_no = item['item_no']
            qty = item['qty']
            price = item['price_per_item']
            rid = item['retailer_id']
            date = item['expected_shipment_date']
            mid = item['manufacturer_id']

            sql = "insert ignore into man (exp_key, item_no, expected_shipment_date, qty, price_per_item, manufacturer_id, retailer_id) values (%s,%s,%s,%s,%s,%s,%s)"
            var = (exp_key, item_no, date, qty, price, mid, rid)

            cursor.execute(sql, var)

            db.commit()
        print("Import successful")


    else:
        input="Import cancelled."

call = db.cursor()

call.execute("select * from man")

all = list(call.fetchall())

col_names = [col[0] for col in call.description]

data = {}
alldata = {}

exp_ans = input("Export to CSV file? Y/N: ")
if exp_ans == "Y":
    with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            coll=[col_names[0], col_names[1], col_names[2], col_names[3], col_names[4], col_names[5], col_names[6]]
            writer.writerow(coll)
            for row in all:
                writer.writerow(row)

    print("Done. CSV file in " + os.getcwd())

elif exp_ans == "N":
    print("Done")