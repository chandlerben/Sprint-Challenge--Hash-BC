#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(length):
        hash_table_insert(
            hashtable, tickets[i].source, tickets[i].destination)

    current_source = "NONE"
    for i in range(length):
        route[i] = hash_table_retrieve(hashtable, current_source)
        current_source = hash_table_retrieve(hashtable, current_source)

    return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# test_tickets = [ticket_1, ticket_2, ticket_3]

# reconstruct_trip(test_tickets, 3)
