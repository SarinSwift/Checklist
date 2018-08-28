
checklist = list()


def create(item):
    checklist.append(item)

def read(index):
    item = checklist[int(index)]
    return item

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def mark_completed(index):
    update(index, "{} {}".format("/", checklist[index]))


def user_input(prompt):
    user_input = raw_input(prompt)
    return user_input


def select(function_code):
    if function_code == "C":
        input_item = user_input("Input Item: ")
        create(input_item)
    elif function_code == "R":
        item_index = user_input("Index Number? ")
        print(read(item_index))
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

running = True
while running:
    selection = user_input("Press C to add to list, R to read from list, P to display list, and Q to quit: ")
    running = select(selection)
