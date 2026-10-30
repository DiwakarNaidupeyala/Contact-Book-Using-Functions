contact={}
def add_contact():
    name=input("Enter name")
    phone=input("Enter phone num")
    contact[name]=phone
    print("conttact added successfully")
def search_contact():
    name=input("search contact")
    if name in contact:
        print("phone num", contact[name])
    else:
        print("contact not found")
def update_contact():
    name=input("search contact")
    if name in contact:
        phone=input("Enter phone num")
        contact[name]=phone
        print("contact updated successfully")
    else:
        print("contact not found")
def delete_contact():
    name=input("search contact")
    if name in contact:
       
        del contact[name]
        print("contact deleted successfully")
    else:
        print("contact not found")
def view_contact():
    if len(contact)==0:
        print("no contacts is there")
    else:
        for name,phone in contact.items():
            print(name,":",phone)
def show_menu():
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.View Contacts")
    print("6.Exit")

while True:
    show_menu()
    choice = int(input("Enter your choice "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        update_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        view_contact()
    elif choice == 6:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
    
