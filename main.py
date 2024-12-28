
notes= []
def noteBook():
    global notes
    print("1: Take Notes")
    print("2: Check Notes")
    print("3: Go back")
    choose = int(input())
    if choose == 1:
        NewNotes = input("Write your notes here:")
        notes.append(NewNotes)
        noteBook()
    elif choose==2:
        print(notes)
        noteBook()
    elif choose==3:
        print("")
noteBook()