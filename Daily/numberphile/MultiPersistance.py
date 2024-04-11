def per(n,itr=0):
    if len(str(n)) == 1:
        print("Last:",n)
        print("Number of steps:", itr)
        return "Done"

    digits = list(map(lambda x: int(x), list(str(n))))

    result = 1
    for d in digits:
        result *= d
    print(result)
    itr += 1
    per(result,itr)

