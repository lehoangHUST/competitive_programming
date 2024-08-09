# hash table : dictionary python {key1 : value1, key2 : value2}
# key is name player and value is point of player when finish game
 
def solve_2A(list):
    dict = {} # Dictionary in python
    _list = []
    # Step 1:
    for player in list:
        player = player.split(' ')
        if player[0] in dict.keys():
            dict[player[0]] += int(player[1])
        else:
            dict[player[0]] = int(player[1])
    # Step 2:
    max_value = max(dict.values())  
    for index in dict:
        if dict[index] == max_value:
            _list.append(index)
        dict[index] = 0
    # Step 3:
    for player in list:
        player = player.split(' ')
        if player[0] in _list:
            dict[player[0]] += int(player[1])
            if dict[player[0]] >= max_value:
                name = player[0]
                break
    print(name)
 
if __name__ == '__main__':
    n = int(input())
    list = ""
    for i in range(n):
        char = '\n' if i < n - 1 else ''
        list = list + input() + char
    
    list = list.split('\n')
    solve_2A(list)