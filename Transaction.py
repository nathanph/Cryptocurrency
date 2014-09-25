__author__ = 'Nathan Hernandez'

class Transaction:
    def __init__(self,
                 version,
                 tx_in_count, tx_in_array,
                 tx_out_count, tx_out_array,
                 lock_time):
        self.version = version
        self.tx_in_count = tx_in_count
        self.tx_out_count = tx_out_count
        self.tx_out_array = tx_out_array
        self.lock_time = lock_time

