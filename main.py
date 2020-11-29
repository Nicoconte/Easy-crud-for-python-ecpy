from utils.database import Database
from query.query import Query

from utils.utils import Utils

def test():
    print( Utils.trim_field_operation("count(bills)") )

def main():  

    query = Query(Database("localhost", "python_database", "root", ""))
    
    query.insert({
        "fields" : ("id", "name", "password"),
        "table" : "user",
        "values" : ("1", "admin", "123")
    })

    query.udpate({
        "fields" : ("name",),
        "table" : "user",
        "condition" : "where id=%s",
        "values" : ("super admin", "1")
    })
    
    query.delete({
        "table" : "user",
        "condition" : "where id=%s",
        "values" : ("2",)
    })

    query.select({
        "fields" : ("name", "password"),
        "table" : "user",
        "condition" : "where id=%s",
        "values" : ("1",)
    })


    query.select({
        "fields" : ("name", "password"),
        "table" : "user",
        "condition" : "where name like %s",
        "values" : ("%a%",)
    })

    query.select({
        "fields" : ("name", "password"),
        "table" : "user",
        "condition" : "order by name"
    })

    query.select({
        "fields" : ("name", "password"),
        "table" : "user",
        "condition" : "group by name"
    })
    
    query.selectAll({
        "fields" : ("id", "name", "password"),
        "table" : "user"
    })   

    query.select({
        "fields" : ("count(name)",),
        "table" : "user"
    })

    query.select({
        "fields" : ("avg(bills)",),
        "table" : "payments",
        "condition" : "where id_user=%s",
        "values" : ("1",)
    })    
    
if __name__ == "__main__":
    main()