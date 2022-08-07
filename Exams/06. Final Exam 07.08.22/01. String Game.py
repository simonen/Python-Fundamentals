string = input()

command = input()

while command != "Done":
    command = command.split()
    action = command[0]
    if action == "Change":
        char = command[1]
        new_char = command[2]
        string = string.replace(char, new_char)
        print(string)
    elif action == "Includes":
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif action == "End":
        end_subs = command[1]
        len_sub = len(end_subs)
        if end_subs == string[-len_sub::]:
            print("True")
        else:
            print("False")
    elif action == "Uppercase":
        string = string.upper()
        print(string)
    elif action == "FindIndex":
        char_i = command[1]
        print(string.index(char_i))
    elif action == "Cut":
        start_i = int(command[1])
        count = int(command[2])
        string = string[start_i:start_i + count]
        print(string)

    command = input()