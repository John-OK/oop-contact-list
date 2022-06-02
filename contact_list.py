from functools import cmp_to_key

class ContactList():
    def __init__(self, list_name, contacts):
        self.list_name = list_name
        self.contacts = contacts


    # def sort_by_name(self, a, b):
    #     self.a = a
    #     self.b = b
    #     if a['name'] > b['name']:
    #         return 1
    #     if a['name'] > b['name']:
    #         return -1
    #     if a['name'] > b['name']:
    #         return 0

    def add_contact(self, name_to_add, phone_num):
        contact = {}
        contact['name'] = name_to_add
        contact['number'] = phone_num
        self.contacts.append(contact)
        # self.contacts = sorted(self.contacts['name'])
        # self.contacts = sorted(self.contacts, key = cmp_to_key(self.sort_by_name))


    def remove_contact(self, name_to_remove):
        for person in self.contacts:
            if person['name'] == name_to_remove:
                self.contacts.remove(person)

    def find_shared_contacts(self, contact_list):
        shared_contacts = []
        for person in self.contacts:
            if person in contact_list.contacts:
                shared_contacts.append(person)
        return ContactList('shared_contacts', shared_contacts)



# friends = ContactList('friends')
# friends.add_contact('bob', '415-555-1212')
# friends.add_contact('alice', '415-555-1213')
# friends.add_contact('zoe', '415-555-1214')
# friends.add_contact('mel', '415-555-1215')
# print(friends.contacts)
# friends.remove_contact('alice')
# print(friends.contacts)
friends = [{'name': 'Alice', 'number': '867-5309'},
           {'name': 'Bob', 'number': '555-5555'}]
work_buddies = [{'name': 'Alice', 'number': '867-5309'},
                {'name': 'Carlos', 'number': '555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]
print(friends_i_work_with.contacts)
