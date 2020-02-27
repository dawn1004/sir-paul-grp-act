import os


def menu():
    print("[1] Add to-do list")
    print("[2] View to-do list")
    print("[3] Exit")

    userinput = int(input(""))
    if userinput == 1:
        os.system("cls")
        addToDo()
    elif userinput == 2:
        os.system("cls")
        viewToDo()


def viewToDo():
    file = open("todo-list.txt", "r")

    if file.read() == "":
        print("There are no to-dos!")
        return 0
    else:
        file.seek(0)
        print("##### To-do list #####")
        num = 1
        for list in file:
            list = list.split("#")
            print("[{}] {}".format(num, list[0]))
            num += 1
        print("[0] Main menu")
        file.close()
        con = int(input(""))

        if con == 0:
            os.system("cls")
            menu()
        else:
            os.system("cls")
            viewTodoContents(con)


def viewTodoContents(pos):
    x = 1
    file = open("todo-list.txt", 'r')

    for list in file:
        if x == pos:
            title_and_content = list.split("#")
            for index, content in enumerate(title_and_content, start=1):
                if index == 1:
                    print("#####{}#####".format(content))
                else:
                    print("{}. {}".format(index-1, content))
        x += 1
    print("[1] Go back")
    print("[0] Main menu")
    file.close()
    con = int(input(""))

    if con == 0:
        os.system("cls")
        menu()
    elif con == 1:
        os.system("cls")
        viewToDo()


def addToDo():
    print("##### To-do list #####")
    listcontent = []
    title = input("Title:")
    x = 1
    while True:
        content = input("{}. ".format(x))
        if content == "0":
            break
        else:
            listcontent.append(content)
        x += 1
    os.system("cls")
    saveToDo(title, listcontent)


def saveToDo(title, listcontent):
    newTodo = title

    for content in listcontent:
        newTodo += "#{}".format(content)

    file = open("todo-list.txt", "a")
    file.write(newTodo+"\n")

    file.close()

    print("To-do list added")

    menu()


menu()
