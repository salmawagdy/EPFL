option = input('What do you want to do?\nPress 1 to add a note\nPress 2 to search for a note\n: ')

if option == "1":
    note = input('Please enter your note:\n')
    file = open("notes.txt", "a")
    file.write(note + "\n")
    file.close()
    print("Note added successfully!")

elif option == "2":
    search = input('Please enter text to search:\n')
    file = open("notes.txt", "r")
    content = file.read()
    file.close()

    notes = content.split("\n")
    found = False

    for note in notes:
        if search in note and note.strip() != "":
            print(note)
            found = True

    if not found:
        print("Not found")
