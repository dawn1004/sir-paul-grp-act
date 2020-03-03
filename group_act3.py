

def menu():  # Answer in no.1.... function menu with no agruments....
    print("[1] Add to-do list")  # display lang tong tatlo
    print("[2] View to-do list")
    print("[3] Exit")

    # user input that will store in userinput variable
    userinput = int(input(""))
    # if userinput is equal to 1 then proceed sa no. 4 (addTodo() funtion)
    if userinput == 1:
        addToDo()
    # if userinput is equal to 2 go to no.2 (viewTodo() funtion)
    elif userinput == 2:
        viewToDo()
    elif userinput == 3:  # if userinput is equql to 3 just return to exit
        return()


def viewToDo():  # answer no.2 viewTDo() funtion with no arguments that display list of to-dos
    # open todolist.txt with reading permission and stored in var file
    file = open("todolist.txt", "r")

    if file.read() == "":  # so if file is empty just print there are no to dos
        print("There are no to-dos!")
        menu()  # just return to menu because that is the rule in no.2
        return 0
    else:  # esle sure ng malaman si todolist.txt so just print the title just remember.... TITLE IS ALWAYS AT INDEX ZERO
        file.seek(0)  # seek zero para yung cursor mabalik sa unahan
        print("##### To-do list #####")  # print lang to
        num = 1  # num will use sa numbering lang
        for list in file:  # so loop file as list.. each line of the file will hold by list variable
            # so naget na yung individial lines kaya need naman isplit para mapag hiwa hiwalay mga content at title
            list = list.split("#")
            # so need lang naman si list index zero kasi need lang natin ng title muna idisplay
            # si num, numbering lang yung wag kayo malito
            print("[{}] {}".format(num, list[0]))
            num += 1  # increment lang si num para 1,2,3,4,5,.....
        # print lang to para mag muka may option si user
        print("[0] Main menu")
        file.close()  # close lang tong file
        # so si con var mag hohold ng input na converted sa int kasi yung rile sa no.3
        con = int(input(""))

        if con == 0:  # so if con is equal to zero then exit sa view todo tapos back sa menu
            menu()

        # else sure na may todo content sya gusto makita sa go lang sa viewTodoContents(con) function with agrument of int pos
        else:
            viewTodoContents(con)


# no. 3 viewToDoContents(pos) function with agrument of pos as integer
# eto pinaka nakakalito
# so gagawin lang dito gagawa ng loop ni file and si x and pos icocompare lang lagi kung equal sila para makuha yung line na hinahanap natin sa file
def viewTodoContents(pos):
     x = 1  # start kay one
    file = open("todolist.txt", 'r') #open file as reading

    for list in file: #loop lang
        if x == pos: #so kung yung x ay equal na sa pos sure na tayong nasa hinahanap natin line tayo
            title_and_content = list.split("#")  #so split lang si list para mahiwalay title at mga content
            # so si title_and_content ay list ah so
            # sa loop na to gagamit lang tayo ng enumerate search nyo na lang kung ano yun
            # so si variable content hohold niya is yung elements ni title_and_content so kasama dun yung title and contents
            # si idex naman hohold nya lang si start =1 na nag start nga sa one tapos autonmatic siyang nag iincrement kaya no need to increment it inside the loop
            for index, content in enumerate(title_and_content, start=1): 
                if index == 1: #if index is equal to one sure naman tayo na eto yung title
                    print("##### {} #####".format(content))
                else: #kapang hindi equal to one sure tayong eto yung contents
                    print("{}. {}".format(index-1, content))
        x += 1 #increment lang si x paalala ah si x ginagamit para mahanap yung line sa file
    print("[1] Go back") #print nyo lang to choices
    print("[0] Main menu")
    file.close() #close uli
    con = int(input(""))  #get the user input

    if con == 0:
        menu() #if it equal to 0 then go back to menu() function
    elif con == 1:
        viewToDo() #else go back to viewToDo() funtion



# no. 4 addToDo() function with no parameter
def addToDo():
    print("##### To-do list #####") #print this out adaksndahdfjahsdfjahdiua 
    listcontent = [] #create lang tayo ng list na empty
    title = input("Title:") #kunin natin input ng title
    x = 1 #x numbering lang uli yan wag malitoooooooo
    while True:
        content = input("{}. ".format(x)) #so kunin natin si content
        if content == "0":  #pag nag equal na sa zero break na kasi yung rule
            break
        else: #pag hindi equal sa zero continue appending lang kay listcontent 
            listcontent.append(content)
        x += 1 #increment numbering lang to
    saveToDo(title, listcontent) #so ang rule is ipapasa kay savToDo() function si title as string and si listcontent as alist


# saving lang to sa file ah galing kay addToDo() function
def saveToDo(title, listcontent): #so eto wa lilinawin ko one string and one list ang pinapasa natin
    # so si newTodo mag hohold ng magkakadikit ng title at content kunwarin ganoto "morning todo#wake up# sleep again# go to school if have time"
    newTodo = title  

    for content in listcontent: #so iloop lang si listcontent
        newTodo += "#{}".format(content) #append lang natin si content kay newTodo

    file = open("todolist.txt", "a") #open todolist.txt with appending permission
    file.write(newTodo+"\n") #so write lang natin si newTodo and dont forget si backslash N para mag create ng new line pagkatapos nung new todo

    file.close()

    print("To-do list added")

    menu() #back lang sa menu kasi yun yung rule


menu()
