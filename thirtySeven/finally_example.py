def func():
    try:
        arr = [1, 2, 3, 4, 5]
        val = int(input("Enter the index you want to access\n"))
        print(arr[val])
        return 1
    except:
        print("Some error occurred")
        return 0
    # agar ye finally ke andr na hota to ye statement kabhi execute na hoti
    finally:
        print("I will always executed")
        return 1


print(func())
