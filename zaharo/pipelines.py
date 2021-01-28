import sqlite3


class ZaharoPipeline:
    conn = sqlite3.connect('zaharo.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `zaharo` (
                                                                    title varchar(100),
                                                                    description text                                                                                 
                                                                    )'''
                            )
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title']
        description = item['description']

        self.cursor.execute(
            f"""select * from zaharo where title = '{title}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `zaharo`
                                                (`title`, `description`)
                                                values (?, ?)""", (title, description))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
