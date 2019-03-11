import sqlite3
from RecordsHolder.model import Record



database_file = 'records.sqlite'

table = 'recordHolders'
col1 ='playerName'
col2='country'
col3 ='catches'



class RecordsStore:
    """ Singleton class to hold and manage a database of record holders """

    instance = None

    class __RecordsStore:
        def __init__(self):
            self._db = sqlite3.connect(database_file)
            self._db.row_factory = sqlite3.Row

            with self._db as db:
                cur = db.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS '+ table +'('
                            + col1+' TEXT , '
                            + col2+' TEXT , '
                            + col3+' INT )')


# Your program should let the user add a new row for a record holder.
        def add_record(self,record):
            try:
                with self._db as db:
                    cur=db.cursor()
                    cur.execute('INSERT INTO '+ table+ ' values (?,?,?)',(record.name, record.country, record.number))
                    record.id = cur.lastrowid
            except sqlite3.Error as e:
                raise RecordError('Error adding record')


# Your program should also let the user search for a record holder, by name
        def record_holder_search(self, name):
            cur = self._db.cursor()
            search = f'%{name.upper()}%'
            cur.execute('SELECT * FROM '+
                        table+' WHERE UPPER ('+col1+') like ?', (search,))
            return self._cursor_to_recordlist(cur)

        def _cursor_to_recordlist(self,cur):
            return [self._row_to_record(row) for row in cur]
        def _row_to_record(self, row):
            if not row:
                return None
            record = Record(row[col1], row[col2], row[col3], row['rowid'])

            return record



# You should be able to update the number of catches for a record holder.
        def update_number_of_catches(self, name, new_number):
            try:
                with self._db as db:
                    cur = db.cursor()
                    search = f'%{name.upper()}%'
                    cur.execute('UPDATE recordHolders SET catches = ? WHERE UPPER(playerName) like ?', (new_number, search))
            except sqlite3.Error as e:
                raise RecordError('Error setting new record ') from e


# And, you should be able to delete a record, by record holder's name (for example, if a person's record was found to be invalid).

        def get_all_records(self):
            try:
                cur = self._db.cursor()
                cur.execute('SELECT rowid, * FROM '+table)
                return self._cursor_to_recordlist(cur)

            except sqlite3.Error as e:
                raise RecordError('Error getting all records') from e



    def __new__(cls):
        if not RecordsStore.instance:
            RecordsStore.instance = RecordsStore.__RecordsStore()
        return RecordsStore.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)



class RecordError(Exception):
    pass