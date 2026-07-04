class ContactBook:
    def __init__(self):
        # Each contact is a dict: {"name": ..., "phone": ..., "email": ...}
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)
        print(f"\nContact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found. Your contact book is empty.")
            return

        print("\n" + "=" * 50)
        print("               ALL CONTACTS")
        print("=" * 50)
        for i, c in enumerate(self.contacts, start=1):
            print(f"{i}. Name : {c['name']}")
            print(f"   Phone: {c['phone']}")
            print(f"   Email: {c['email']}")
            print("-" * 50)

    def search_contact(self, keyword):
        keyword = keyword.strip().lower()
        results = [c for c in self.contacts if keyword in c["name"].lower()]

        if not results:
            print(f"\nNo contacts found matching '{keyword}'.")
            return

        print("\n" + "=" * 50)
        print(f"       SEARCH RESULTS FOR '{keyword}'")
        print("=" * 50)
        for i, c in enumerate(results, start=1):
            print(f"{i}. Name : {c['name']}")
            print(f"   Phone: {c['phone']}")
            print(f"   Email: {c['email']}")
            print("-" * 50)

    def delete_contact(self, name):
        keyword = name.strip().lower()
        matches = [c for c in self.contacts if c["name"].lower() == keyword]

        if not matches:
            print(f"\nNo contact found with the name '{name}'.")
            return

        for match in matches:
            self.contacts.remove(match)
        print(f"\nContact '{name}' deleted successfully.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def main():
    book = ContactBook()

    menu = """
========================================
           CONTACT BOOK MENU
========================================
1. Add a new contact
2. View all contacts
3. Search contact by name
4. Delete a contact
5. Exit
========================================
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = get_non_empty_input("Enter name: ")
            phone = get_non_empty_input("Enter phone number: ")
            email = get_non_empty_input("Enter email: ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            keyword = get_non_empty_input("Enter name to search: ")
            book.search_contact(keyword)

        elif choice == "4":
            name = get_non_empty_input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == "5":
            print("\nGoodbye! Your contact book session has ended.")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()