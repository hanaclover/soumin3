#!/usr/bin/env python
# 入力データの先頭行のラベルと行末改行は削除すること。
# pref_code：01 ⇨ 1にしておく。:w

import pymysql.cursors
from pprint import pprint

# MySQLへの接続
connection = pymysql.connect(
    host='localhost',
#    port='',
    user='edmaps_user',
    password='souminn3',
    db='Edmaps',
    charset='utf8',
    # cursorclassを指定することで
    # Select結果をtupleではなくdictionaryで受け取れる
    cursorclass=pymysql.cursors.DictCursor)

for line in open('prefCode.csv', 'r'):
    line = line.rstrip()
    itemList = line.split(',')

    # SQLを実行する
    with connection.cursor() as cursor:
        sql = 'INSERT INTO Edmaps.pref_code(pref_code, pref_name, pref_name_spoken) VALUES(%s, %s, %s)'
        cursor.execute(sql, (itemList[0], itemList[1], itemList[2]))
        # autocommitではないので、明示的にコミットする
        connection.commit()
        print(itemList)
#        # Select結果を取り出す
#        results = cursor.fetchall()
#        for r in results:
#            print(r)
# MySQLから切断する
connection.close()
