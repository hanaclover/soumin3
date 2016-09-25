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

# 都道府県辞書の生成
prefList = {}
for line in open('../pref/prefCode.csv', 'r'):
    line = line.split(',')
    prefList[line[1]] = line[0]

# 市区町村データの読み込み
for line in open('cityCode.csv', 'r'):
    line = line.rstrip()
    itemList = line.split(',')
    # SQLを実行する
    with connection.cursor() as cursor:
        sql = 'INSERT INTO Edmaps.city_code(city_code, pref_code, city_name, city_name_spoken) VALUES(%s, %s, %s, %s)'
        cursor.execute(sql, (itemList[0], prefList[itemList[1]], itemList[2], itemList[3]))
        # autocommitではないので、明示的にコミットする
        connection.commit()
        print(itemList)
#        # Select結果を取り出す
#        results = cursor.fetchall()
#        for r in results:
#            print(r)
# MySQLから切断する
connection.close()
