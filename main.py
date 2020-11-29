from utils.database import Database
from utils.utils import Utils
from builder.query_builder import Builder 
from query.query import Query
import uuid

def main():  

    response_dic = {}
    response = []

    query = Query(Database("localhost", "python_database", "root", ""))

    response = query.selectJoin({
        "fields" : ("content", "author"),
        "table" : "blog",
        "another_table" : "user",
        "relation" : "blog.id_author=user.id",
        "condition" : "where blog.id_author=%s",
        "values" : ("5",)
    })

    print(response)

if __name__ == "__main__":
    main()