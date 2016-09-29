class Person(object):
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print 'Hello %s, I am %s' % (other_person.name, self.name)

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)
        print "Friend's: "
        for p in self.friends:
            print p

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print "%s has %d friends" % (self.name, len(self.friends))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', '')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', '')
john = Person('John', 'papajohns@inthehouse.com', '404-983-PZZA', '')

sonny.add_friend(jordan)
sonny.add_friend(john)

sonny.greet(jordan)
sonny.print_contact_info()

jordan.greet(sonny)
jordan.print_contact_info()

sonny.num_friends()
jordan.num_friends()
