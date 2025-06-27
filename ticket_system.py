import sqlite3

class TicketSystem:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT,
                language TEXT,
                sentiment TEXT,
                response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def create_ticket(self, message, language, sentiment):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tickets (message, language, sentiment) VALUES (?, ?, ?)",
                       (message, language, sentiment))
        self.conn.commit()
        return cursor.lastrowid

    def update_ticket(self, ticket_id, response):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tickets SET response = ? WHERE id = ?", (response, ticket_id))
        self.conn.commit()
