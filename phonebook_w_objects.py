import pickle

class Contact:
    def __init__(self, name, address, work, cell):
        self.name = name
        self.address = address
        self.work = work
        self.cell = cell

class Phonebook:
    def __init__(self, filename):
        self.filename = filename
        self.store = {}
        self.load()

    def load(self):
        my_file = open('phonebook.pickle', 'r')
        self.filename = pickle.load(my_file)

    def save(self):
        with open(self.filename) as f:
            pickle.dump(self.store, f)

    def get(self, name):
        if name in self.store:
            return self.store[name]
        return None

    def add(self, person):
        self.store[comtact.getName()] = contacts
        self.save()


rob = Contact('Rob', '20 T Place', '404', '678')
Phonebook.get('Rob')
