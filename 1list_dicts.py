def run():
    my_list = [1,"Hello", True, 4.5]
    my_dict = {"name":"Carlos", "last_name":"Garcia"}

    super_list = [
        {"name":"Carlos", "last_name":"Garcia"},
        {"name":"Max", "last_name":"Garcia"},
        {"name":"Anthony", "last_name":"Garcia"}
    ]

    super_dict = {
        "natural_nums": [1 , 2, 3, 4, 5, 6],
        "integer_nums": [1.1 , 1.5, 2.6, 2.5],
        "boolean_num": [0,1]
    }


    for value, key in super_dict.items():
        print(value, key)

    for items in super_list:
        print(items)

# The entrypoint
if __name__ == '__main__':
    run()