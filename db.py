import pymysql
import pymysql.cursors



connect = pymysql.connect(host='localhost:3306', user='nairi_nairi', password='nairi.nairi2004', db='nairi_link_shortener')

a = conn.cursor()

sql = 'SELECT * FROM `suggestions`'
a.execute(sql)

countrow = a.execute(sql)


bot.send_sticker(message.chat.id, countrow)