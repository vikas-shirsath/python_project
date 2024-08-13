class Node:
    def __init__(self,name,disease,priority):
        self.name = name
        self.disease = disease
        self.priority = priority
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def delete_node(self):
        if self.head == None :
            print("List is Empty")
            return
    
        search_name = input("Enter patient's name : ")

        previous_node = None
        current_node = self.head
        while current_node.name != search_name and current_node != None:
            previous_node = current_node
            current_node = current_node.next

        if current_node.next.name == None :
            print("Patient is not found ")
            return

        if previous_node == None :
            self.head = current_node.next
        else :
            previous_node.next = current_node.next
        print(f"Data of patient named {search_name} has been deleted.")

    def display(self):
        current_node = self.head
        if self.head == None :
            print("List is empty.")
            return
        
        while current_node != None:
            print(f"[{current_node.name},{current_node.disease},{current_node.priority}]", end=(" -->  "))
            current_node = current_node.next
        print("End")

    def search(self):
        if self.head == None :
            print("List is Empty")
            return

        print("Search by name")        
        search_name = input("Enter patient's name : ")

        current_node = self.head
        while current_node.name != search_name and current_node != None:
            current_node = current_node.next

        if current_node.name == None :
            print("Patient is not found ")
            return
        
        if current_node.name == search_name :
            print(f"[{current_node.name},{current_node.disease},{current_node.priority}]")

    def add_after_severe(self,name,disease,priority):
        new_node = Node (name, disease, priority)
        if self.head == None :
            self.head = new_node
            return
        
        current_node = self.head

        while current_node.next is not None and current_node.next.priority == "Severe":
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
     
    def add_after_internediate(self,name,disease,priority) :
        new_node = Node (name, disease, priority)
        if self.head == None :
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None and current_node.next.priority == "Intermediate":
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node  
            
    def add_at_end(self,name,disease,priority)  :
        new_node = Node (name, disease, priority)
        if self.head == None :
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next :
            current_node = current_node.next
        current_node.next = new_node

    def add_node(self):
        name = input("Enter name of patient : ")
        disease = input("Disease of pateint : ")
        priority = input("Priority of pateint [Severe / Intermediate / Mild] : ")

        if priority == "Severe" :
            self.add_after_severe(name,disease,priority)
        elif priority == "Intermediate":
            self.add_after_intermediate(name,disease,priority)
        else:
            self.add_at_end(name,disease,priority)
            return

def menu():
    print("1. Add ")
    print("2. Search")
    print("3. Display")
    print("4. Delete patient data")
    print("5. Exit")
    choice = int(input("Enter your choice : "))
    return choice


def main():

    print(" PATIENT MANAGEMENT SYSTEM ")

    list = linked_list()
    
    while True:
        choice = menu()
        if choice == 1:
            list.add_node()
        elif choice == 2:
            list.search()
        elif choice == 3:
            list.display()
        elif choice == 4:
            list.delete_node()
        elif choice == 5:
                print("Exiting.....")
                break
        else:
                print("Invalid choice")


if __name__ == "__main__":
    main()
