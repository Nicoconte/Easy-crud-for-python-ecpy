from typing import final

from mysql.connector.connection import MySQLConnection
from builder.query_builder import Builder
from utils.utils import Utils

import mysql.connector

class Query:
    __db = None
    __connector = None
    __cursor = None
    __records = None
    __builder = Builder()

    __success = False
    __response_container = []

    def __init__(self, database):
        self.__db = database


    def insert(self, config):
        try:
            self.__connector = self.__db.setConnection() 
            self.__cursor = self.__connector.cursor(prepared=True)

            self.__cursor.execute(
                self.__builder.insertQuery(config["fields"], config["table"]),
                config["values"]
            )

            self.__connector.commit()
            self.__success = Utils.query_done(self.__cursor.rowcount)

        except mysql.connector.Error as error:
            print(f"No se pudo guardar el registro => {error}")
        
        finally:
            Utils.close_connections(self.__cursor, self.__connector) 

        return self.__success


    #* --------------------------------------------------------------------------------------------------
    def udpate(self, config):
        try:
            self.__connector = self.__db.setConnection()
            self.__cursor = self.__connector.cursor(prepared=True)

            self.__cursor.execute(
                self.__builder.updateQuery(config['fields'], config['table'], config['condition']),
                config['values']
            )
            
            self.__connector.commit()
            self.__success = Utils.query_done(self.__cursor.rowcount)

        except mysql.connector.Error as error: 
            print(f"No se pudo actualizar el reporte => {error}")

        finally:
            Utils.close_connections(self.__cursor, self.__connector)

        return self.__success


    #* --------------------------------------------------------------------------------------------------    
    def delete(self, config):
        try:
            self.__connector = self.__db.setConnection()
            self.__cursor = self.__connector.cursor(prepared=True)

            self.__cursor.execute(
                self.__builder.deleteQuery(config["table"], config["condition"]),
                config["values"]
            )

            self.__connector.commit()
            self.__success = Utils.query_done(self.__cursor.rowcount)

        except mysql.connector.Error as error:
            print(f"No se pudo eliminar el registro => {error}")

        finally:
            Utils.close_connections(self.__cursor, self.__connector)

        return self.__success


    #* --------------------------------------------------------------------------------------------------
    def select(self, config):
        try:
            self.__connector = self.__db.setConnection()
            self.__cursor = self.__connector.cursor(buffered=True)


            if 'values' in config:
                self.__cursor.execute(
                    self.__builder.selectQuery(config['fields'], config['table'], config['condition']), config['values'] )
            else:
                self.__cursor.execute(self.__builder.selectQuery(config['fields'], config['table'], config['condition']))

            self.__connector.commit()
            
            if self.__cursor.rowcount == 1:
                self.__records = self.__cursor.fetchone()
                return Utils.generate_dictionary(config['fields'], self.__records)

            elif self.__cursor.rowcount > 1:
                self.__records = self.__cursor.fetchall()
                for result in self.__records:
                    self.__response_container.append(Utils.generate_dictionary(config['fields'], result))
                
                return self.__response_container

            else:
                raise ValueError("No hay resultados")  

        except mysql.connector.Error as error:
            print(f"No se pudo obtener los datos => {error}")

        finally:
            Utils.close_connections(self.__cursor, self.__connector)
    
    #* --------------------------------------------------------------------------------------------------
    def selectAll(self, config):
        try:
            self.__connector = self.__db.setConnection()
            self.__cursor = self.__connector.cursor(buffered = True)

            self.__cursor.execute(
                self.__builder.selectAllQuery(config['fields'], config['table'])
            )

            self.__connector.commit()
            self.__records = self.__cursor.fetchall()

            if len(self.__records) > 0:
                for result in self.__records:
                    self.__response_container.append(Utils.generate_dictionary(config['fields'], result))
                
                return self.__response_container

        except mysql.connector.Error as error:
            print(f"No se pudo obtener los registros => {error}")

        finally:
            Utils.close_connections(self.__cursor, self.__connector)


    #* --------------------------------------------------------------------------------------------------
    def selectJoin(self, config):
        try:
            self.__connector = self.__db.setConnection()
            self.__cursor = self.__connector.cursor(buffered=True)

            self.__cursor.execute(
                self.__builder.selectInnerJoinQuery(config['fields'], config['table'], config['another_table'], config['relation'], config['condition']),
                config['values']
            )
            
            self.__connector.commit()
            self.__records = self.__cursor.fetchall()

            if self.__cursor.rowcount > 0:
                for result in self.__records:
                    self.__response_container.append(Utils.generate_dictionary(config['fields'], result))

                return self.__response_container

            else:
                raise ValueError("No hay resultados")

        except mysql.connector.Error as error:
            print(f"No se pudo obtener los registros {error}")

        finally:
            Utils.close_connections(self.__cursor, self.__connector) 


