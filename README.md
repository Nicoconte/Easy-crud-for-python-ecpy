# -- Easy Crud for python - ecpy :snake: --

## ecpy es una pequeña libreria escrita en python, para python y basado en EC4J.

### Manipula facilmente pequeñas / medianas base de datos sin la necesidad de perder tiempo creando las consultas desde 0 u ocurrir a librerias complejas.


### *Main*:

**Consultas disponibles** :white_check_mark:

  - SELECT FROM 
  - SELECT FROM WHERE
  - SELECT INNER JOIN
  - SELECT COUNT | SELECT AVG
  - SELECT MAX - MIN
  - UPDATE SET WHERE  
  - DELETE FROM WHERE  
  - INSERT INTO

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

```python
from utils.database import Database
from query.query import Query


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
```
