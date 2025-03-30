class Person:
    def __init__(self, name, phone, key):
        self.name = name
        self.phone = phone
        self.key = key


class PhoneDirectory:
    def __init__(self):  
        self.directory = {}

    def add_contact(self, person):
        self.directory[person.key] = person
        print(f"Contact {person.name} added successfully.")

    def search_contact(self, key):
        person = self.directory.get(key)
        if person:
            return f"{person.name}: {person.phone}"
        return "Contact not found"

    def delete_contact(self, key):
        if key in self.directory:
            removed = self.directory.pop(key)
            print(f"Contact {removed.name} deleted successfully.")
        else:
            print("Contact not found.")

    def show_directory(self):
        if self.directory:
            for person in self.directory.values():
                print(f"{person.name}: {person.phone}")
        else:
            print("The directory is empty.")



directory = PhoneDirectory()
directory.add_contact(Person("Camila", "312-578-4590", "1"))
directory.add_contact(Person("Mariana", "987-123-4567", "2"))
directory.add_contact(Person("Juana Perez", "123-456-7890", "3"))
directory.add_contact(Person("Luisa Martinez", "987-654-3210", "4"))
print(directory.search_contact("3"))
directory.show_directory()
directory.delete_contact("4")
directory.show_directory()



