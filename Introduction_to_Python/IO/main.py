def create_txt_file():
    data = range(0,100)
    with open('file.txt', 'w') as file:
        for i in data:
            file.write(f'{i}\n')

def read_txt_file():
    with open('file.txt', 'r') as file:
        print(file.read())

create_txt_file()
read_txt_file()
