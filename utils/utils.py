class Utils:
    def __init__(self):
        pass


    @staticmethod
    def validate_fields(tup):
        return type(tup) == 'tuple'

    @staticmethod
    def query_done(row):
        return row >= 0

    @staticmethod
    def generate_dictionary(keys, values):
        dictionary = {}
        for i in range(len(keys)):
            dictionary.update(dict([( str(keys[i]), values[i])]))

        return dictionary

    @staticmethod
    def close_connections(cursor, connector):
        if connector.is_connected():
            connector.close()
            cursor.close()