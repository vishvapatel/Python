test_cases = int(input())
for case in range(test_cases):
    players = int(input())
    villans_strength = [int(i) for i in input().split(' ')]
    players_energy = [int(i) for i in input().split(' ')]

    players_energy.sort()
    villans_strength.sort()
    flag = 0
    for i in range(players):
        if players_energy[i] < villans_strength[i]:
            flag = 1
            break
        else:
            flag = 0

    if flag == 0:
        print("WIN")
    else:
        print("LOSE")
