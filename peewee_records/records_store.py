from peewee_records.model import Record
from peewee import IntegrityError

# Your program should let the user add a new row for a record holder.
def add_record(record):
    # try:
    record.save()
    # except IntegrityError as e:
    #     raise RecordError ('can not add new record')



# Your program should also let the user search for a record holder, by name
def record_holder_search(name):
    query = Record.select().where((Record.name.contains(name)))
    return list(query)



# You should be able to update the number of catches for a record holder.
def update_number_of_catches( name, new_number):
    rows_updated = Record.update(catches = new_number).where(Record.name==name).execute()
    if not rows_updated:
        raise RecordError
# And, you should be able to delete a record, by record holder's name (for example, if a person's record was found to be invalid).
def delete_record_holder( name):
    rows_deleted = Record.delete().where(Record.name==name).execute()
    if not rows_deleted:
        raise RecordError

def get_all_records():
    query = Record.select()
    return list(query)

class RecordError(Exception):
    pass