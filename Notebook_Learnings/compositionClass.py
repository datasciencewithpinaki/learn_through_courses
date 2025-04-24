from abc import ABC, abstractmethod
from dataclasses import dataclass

class FormatQuery(ABC):
    '''Generic class to read & format a query'''

    @abstractmethod
    def get_query(self):
        '''read query'''

    @abstractmethod
    def format_query(self):
        '''query to be used'''


class DataRead(ABC):
    '''Generic Data Read Class'''

    @abstractmethod
    def query_table(self):
        '''pull data from table'''


class SalesDataRead(DataRead):
    '''Class to Read Sales data'''

    def get_query(self):
        pass

    def format_query(self):
        pass

    def query_table(self):
        pass


class InvntDataRead(DataRead):
    '''Class to Read Sales data'''

    def get_query(self):
        pass

    def format_query(self):
        pass

    def query_table(self):
        pass