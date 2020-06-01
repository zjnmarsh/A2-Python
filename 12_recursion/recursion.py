def countdown(n):
    if n == 0:
        print("end")
    else:
        print(n)
        countdown(n-1)

countdown(10)
