while True:
    try:
        res=int(input())
    except Exception:
        print("Again...")
    else:
        print("At last!!!", res)
        break
