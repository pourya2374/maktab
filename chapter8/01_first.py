
commands = []
while True:
    try:
        commands.append(input())
    except EOFError:
        break

users = []
find_count = 1

for command in commands:
    in_str = command.split(' ')
    if len(in_str) == 5:
        _, name, gender, age, id = in_str
        users.append({'id': id, 'name': name, 'gender': gender, 'age': age})
        print('User {} added successfully'.format(id))
    elif len(in_str) == 2:
        _, query = in_str
        tmp_list = []
        for item in users:
            if item['id'].startswith(query):
                tmp_list.append(item)

        tmp_list.sort(key=lambda x: x['id'])
        result_counter = 0
        for item in tmp_list:
            if item['id'].startswith(query):
                result_counter += 1
                print('{} {} {} {} {}'.format(
                    find_count, item['name'], item['gender'], item['age'], item['id'])
                )
            if result_counter >= 10:
                break
        if result_counter == 0:
            print('{} No user found'.format(find_count))
        find_count += 1
