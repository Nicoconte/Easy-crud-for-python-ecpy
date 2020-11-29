class Builder:

    def __init__(self):
        pass

    def updateQuery(self, fields, table, condition):
        return f"update {table} set { ','.join([f'{field}=%s' for field in fields]) } {condition}"

    def insertQuery(self, fields, table):
        return f"insert into {table} values ({','.join(['%s' for i in range(len(fields))])})"

    def deleteQuery(self, table, condition):
        return f"delete from {table} {condition}"

    def selectQuery(self, fields, table, condition=""):
        return f"select {','.join([field for field in fields])} from {table} {condition}"
    
    def selectAllQuery(self, fields, table, condition=""):
        return f"select {','.join([field for field in fields])} from {table} {condition}"

    def selectInnerJoinQuery(self, fields, table, relation, condition):
        return f"select {','.join([field for field in fields])} from {table[0]} inner join {table[1]} on {relation} {condition}"