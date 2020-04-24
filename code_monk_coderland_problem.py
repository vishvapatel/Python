t=int(input())
for i in range(t):
    checkpoints=int(input())
    cost_per_liter=[int(i) for i in input().split()]
    min_liters = [int(i) for i in input().split()]
    petrol_left=min_liters[0]
    cost=petrol_left*cost_per_liter[0]
    for i in range(1,checkpoints,1):
        if min_liters[i] > min_liters[i-1]:
            diff = min_liters[i] - min_liters[i-1]
            cost = cost + min_liters[i]*cost_per_liter[i]
    print(cost)
