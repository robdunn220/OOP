class Phonebook(object):
    def __init__(self, Contact):
        self.Contact = {}

    def print_info(self):
        print "Name: %s" % self.name
        print "Phone number: %s" % self.phone
        print "Address: %s" % self.address
        print "\n"

    def print_contacts(self):
        for p in self.Contacts:
            print p

class Contact(Phonebook):
    def __init__(self, name, address, phone):
        super(Contact, self).__init__(self.name)
        self.name = name
        self.address =  address
        self.phone = phone

    def add_contact(self):
        self.Contact.append()

rob = Contact('Rob', '14 Stuff', '404-983-3392')

ben = Contact('Ben', '20 Lane Place Ave. NWE', '414-993-3492')

rob.print_info()
ben.print_info()

new_name = raw_input('Please type a name to create a contact: ')
new_address = raw_input('Address: ')
new_number = raw_input('Number: ')
new_name = Contact(new_name, new_address, new_number)

new_name.print_info()
