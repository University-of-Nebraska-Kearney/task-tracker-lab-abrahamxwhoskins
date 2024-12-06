
list = ['']
# Create a function called load_tasks that reads tasks from a file
# into a list and then returns the list.

def load_task()
  # open the task file in read mode
  file = open('task.txt','r')
  #Creating a empty list to hold records
  task = []
  # Read first line of file
  line = file.readline()
  # Loop for if task list not being empty
  while line != '':
    # secondary list for holding the temporary field task
      new_task = []
      new_task.append(line.rstrip('\n)')) # Adding first field and stripping new line
      new_task.append(file.readline().rstrip("\n"))# Adding 2nd field and stripping new line
      new_task.append(file.readline().rstrip("\n"))# Adding 3rd field and stripping new line
      new_task.append(file.readline().rstrip("\n"))# Adding 4th field and stripping new line
      task.append(new_task) #Adding the fields 1-4 (record) to task list
      line = file.readline()
  file.close()
  
  # Returning the list back to be referenced in main
  return task


# Create a function called save_tasks that takes a list of tasks and 
# writes them to a file for long non-volatile storage.

def save_task(tasks)
  #Open file to appending complete list
  with open('task.txt','a') as finalTask:
      try:
    finalTask.write(endTask)
    endTask.append(line.rstrip('\n)')) 
    endTask(file.readline().rstrip("\n"))
    endTask.append(file.readline().rstrip("\n"))
    endTask.append(file.readline().rstrip("\n"))
    task.append(new_task)
    line = file.readline()
