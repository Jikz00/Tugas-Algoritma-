# editor Rizky AJi Santoso (220535608757)
#S1 Teknik Informatika Offering C
# tugas algoritma

name = input("hi").strip()

match name:
    case "Hello" | "Hello, Newman":
        print("0$")
    case "How you doing?":
        print("20$")
    case "What's happening":
        print("100$")
    case _:
        print("???")