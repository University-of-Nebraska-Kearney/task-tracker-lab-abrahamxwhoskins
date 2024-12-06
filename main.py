# Import library of functions
import file_control

def main():
  # Get tasks from file
  tasks = load_tasks()

  # Create loop for menu
  while True:
    print("---Task Tracker Menu---")
    print("1. Display tasks",
         "\n2. Add tasks",
         "\n3. Mark task as complete",
         "\n4. Save and exit")

    # Get user choice
    choice = input()

    # Navigate user based on choice
    if choice == "1":
      display_tasks(tasks)
    elif choice == "2":
      add_tasks(tasks)
    elif choice == "3":
      complete(tasks)
    elif choice == "4":
      save_tasks(tasks)
      print("Thank you for using Task Tracker.")
      break
    else:
      print("That is not a valid option.")



# Create a function called display_tasks that takes a list of taks and
# displays every task in the list.

def display_task(task)
  # open the task file in read mode
  file = open('task.txt','r')
  # Read first line of file
  line = file.readline()
  #Loop if not end of file to continue reading and print 
  while line != '':
      print(line.rstrip('\n)'))
      line = file.readline()
  # Close the file
  file.close()
  
  #display /print all of the task
  print(task)
  continue


# Create a function called add_task that takes a list of tasks, prompts
# the user for another task, and then appends the new tasks to the 
# end of the list.

def add_tasks(tasks)
  # append to list of task by adding another list^
  file = open('task.txt', 'a')
  # prompt user for description
  name = input('What is the name of the task? ')
    # append to index 0
  # prompt user for description
  description = input('What is the task description? ')
    # append to index 1
  # prompt user for due date
  date = input('When is the task due by? ')
    # append to index 2
  # prompt user for status
  status = input('Has the task been done yet? ')
    # append to index 3
  newTask = [name,description,date,status]
  tasks.append(newTask)




# Create a function called complete that takes a lists of tasks,
# displays them to the user, and then lets the user choose one
# to mark as complete. It will then update the status of the 
# task in the list and return the updated list.
def complete(tasks)
  # Display the 0 index (title) of each index in tasks
  for title in tasks:
    print(title[0])
  # Prompt user to choose task
  userTask = input('Which task would you like to choose?')
    if not userTask.isdigit():
      userTask = input('Please choose a number option for your task or ''done'':')
    if userTask.isdigit():
      index = int(userTask) - 1
      # Change status of task to 'complete'
      for i in range(tasks.len())
        tasks[index][3] = 'complete'
        #return to main menu
        break
    #return to main menu
    if userTask == 'done':
      break
 

if __name__ == "__main__":
  main()
