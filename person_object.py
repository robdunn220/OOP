class Person(object):
    def __init__(self, name, email, phone, friends, greeting_count, greet_list, num_of_people_greeted):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = greeting_count
        self.greet_list = []
        self.num_of_people_greeted = 1

    def __repr__(self):
        return "%s" % (self.name)

    def greet(self, other_person):
        print 'Hello %s, I am %s' % (other_person.name, self.name)
        self.greeting_count += 1
        self.greet_list.append(other_person.name)

    def num_unique_people_greeted(self):
        y = 0
        for x in self.greet_list:
            if x == self.greet_list[y + 1]:
                y += 1
                pass
            else:
                self.num_of_people_greeted += 1
        print self.num_of_people_greeted

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)
        print "Friend's: "
        for p in self.friends:
            print p

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print "%s has %d friends" % (self.name, len(self.friends))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', '', 0, '', 1)
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', '', 0, '', 1)
john = Person('John', 'papajohns@inthehouse.com', '404-983-PZZA', '', 0, '', 1)

sonny.add_friend(jordan)
sonny.add_friend(john)

sonny.greet(jordan)
sonny.greet(john)
sonny.greet(jordan)
sonny.greet(jordan)
print sonny.num_unique_people_greeted()
