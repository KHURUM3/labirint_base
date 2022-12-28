
import mysql.connector ## MySQL

class SavingToMySQLPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection= mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '123456',
            database = 'labirint'

        )
        self.curr = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_db(item)
        #we need to return the item below as Scrapy expects us to!
        return item

    def store_db(self, item):
        self.curr.execute(""" insert into labirint_books (authors, name, publisher, series, genre, price) values (%s, %s, %s, %s,%s,%s)""", (
            item["authors"],
            item["name"],
            item["publisher"],
            item["series"],
            item["genre"],
            item["price"],
            # item["description"]

        ))
        self.connection.commit()

