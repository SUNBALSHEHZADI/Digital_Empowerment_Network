class List_Application:
    def __init__(self): 
# list to store task as dictionaries
        self.tasks =[]
        self.task_id =1

#add_task
    def  add_task(self, description):
        task = {
            'task_id': self.task_id,
            'description': description,
            'completed': False
        }
        self.tasks.append(task) #append the task in the dictionary
        self.task_id += 1
        print("Task added  with ID succesfully.") 
        

#view_task
    def  view_task(self):
        if not self.tasks:
            print("Sorry! There is no task in the list.")
            return
        print("Current Tasks:")
        for task in self.tasks:
            status =" completed " if task ['completed'] else " Pending...."
            print(f"Task ID: {task['task_id']}, Description: {task['description']}, Status: {status}")
               
#remove_task
    def remove_task(self, task_id):
        for index, task in enumerate(self.tasks):
            if task['task_id'] == task_id:
                self.tasks.pop(index)
                print(f"Task with ID {task_id} has been removed successfully.")
                return
        print("Invalid task_ID")


#complete_task
    def complete_task(self, task_id):
        for task in self.tasks:
            if task['task_id'] == task_id:
                task['completed'] = True
                print(f'Task"{task["description"]}" marked as completed.')
                return
        print("Invalid  task ID")


#Edit_task
    def edit_task(self, task_id, new_description):
        for task in self.tasks:
            if task['task_id'] == task_id:
                task['description'] = new_description
                print(f'Task with ID {task_id} has been updated to "{new_description}".')
                return
        print("Invalid task ID")


#search_Task
    def search_task(self, keyword):
        found = False
        for task in self.tasks:
            if keyword.lower() in task['description'].lower():
                status = 'completed' if task['completed'] else 'pending'
                print(f"Task: {task['description']} - Status: {status}")
                found = True
        if not found:
            print("Sorry! Task is not  found in the list.")


#Filter Task
    def filter_task(self,task_status):
        found = False
        for task in self.tasks:
            if (task_status == 'completed' and task['completed']) or (task_status == 'pending' and not task['completed']):
                print(f"Task: {task['description']} - Status: {task_status}")
                found = True
        if not found:
            print("No tasks found with that status.")

#Clear Task
    def clear_task(self):
        self.tasks.clear()
        print("Task list cleared successfully!")


#sort_task
    def  sort_task(self, by = 'task_id'):
        if by == 'task_id':
            self.tasks.sort(key=lambda x: x['task_id'])
            print("Task list sorted by ID successfully!")
        elif by =='completed':
            self.tasks.sort(key=lambda x:x['completed'])
            print("Task list sorted by status successfully!")


#loop for menu:
def main():
    app = List_Application()

    while True:
        print("To-do List  Application\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("10. Exit")


        choice = input("Enter your choice : ")
        if  choice == "1":
            description = input("Enter task description:")
            app.add_task(description)
            
        elif choice == "2":
            app.view_task() 
            print(app.tasks)

        elif choice == "3":
            task_id = int(input("Enter task ID to remove:"))
            app.remove_task(task_id)


        elif choice == "4":
            task_id =  int(input("Enter task ID to mark as completed:"))
            app.complete_task(task_id)

        elif choice == "5":
            task_id = int(input("Enter task ID to edit: "))
            new_description = input("Enter the new description: ")
            app.edit_task(task_id, new_description)

        elif choice == "6":
            keyword = input("Enter the task keyword to search: ")
            app.search_task(keyword)

        elif choice == "7":
            status = input("Enter status to filter (completed/pending): ").lower()
            app.filter_task(status)

        elif choice == "8":
            app.clear_task()

        elif choice =="9":
            sort_by = input("Sort by (task_id/completed): ").lower()
            app.sort_task(sort_by)

        elif  choice == "10":
            print("Good BYe!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")



if __name__ == "__main__":
    main()












