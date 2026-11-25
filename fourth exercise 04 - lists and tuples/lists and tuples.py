films = []

while True :
    prog = int(input("\n enter 1 (add) ,2 (delete) , 3 (sort) or 4 (exit) for runningg a program: "))
    match prog:
        case 1:
            fname = input("\n enter a name for the film you want to add: ")
            fyear = int(input("\n enter a year for the film you want to add: "))
            fpoint = int(input("\n enter a point for the film you want to add: "))
            films.append((fname, fyear, fpoint))
            print("\n your list after adding the film : ")
            for item in (films):
                print("\n",item)

        case 2:
            fdelete = input("\n enter a name for the film you want to delete: ")
            for item in films:
                if item[0] == fdelete:
                    films.remove(item)
                    print(f"\n the film that you deleted is {item}")
            print("\n your list after deleting the film : ")
            for item in (films):
                print("\n",item)

        case 3:
            films.sort()
            for item in films:
                print("\n",item)

        case 4:
            break
