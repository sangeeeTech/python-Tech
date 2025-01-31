def calculator():
    operations ={'1': '+', '2': '-','3':'*','4': '/'}
    choice = input("select operations (1: add, 2: subtracr, 3: multiply, 4: divide): ")
    if choice not in operations:
    print("Invalid choice!")
    return