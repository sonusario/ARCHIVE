def A(initial,rate,iterations):
    return initial*((1+rate)**iterations)

def schedule():
    current_amount = 13.636363636363636
    week = 0
    store = 0
    while week < 52:
        week += 1
        current_amount = A(current_amount,0.1,1)
        if week % 4 == 2: store = current_amount
        elif week % 4 == 0: current_amount = store
        print("Week:",week,
              "\tTime(min):",current_amount,
              "\tWarmup(min):",current_amount*0.2)

schedule()
