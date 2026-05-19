tasks=[]
while True:
    print("   TO DO LIST   ")
    print("1.add task")
    print("2.view task")
    print("3.remove task")
    print("4.exit")
    choice=input("enter your choice:")
    if choice=="1":
        task=input("enter your task:")
        tasks.append(task)
        print("task is added")
    elif choice=="2":
        if len(tasks)==0:
            print("no tasks available")
        else:
            print("your tasks:")
            for task in tasks:
                print(task)
    elif choice=="3":
        task=input("enter your task to remove:")
        if task in tasks:
            tasks.remove(task)
            print("task is removed:")
        else:
            print("task not found")
    elif choice=="4":
      print("exited")
      break
    else:
        print("invalid choice")
