data = {
    1: [
        {"seat_name": "a1", "isTaken": True},
        {"seat_name": "a2", "isTaken": False},
        {"seat_name": "a3", "isTaken": True},
        {"seat_name": "a4", "isTaken": True},
        {"seat_name": "a5", "isTaken": False},
    ],
    2: [
        {"seat_name": "b1", "isTaken": False},
        {"seat_name": "b2", "isTaken": False},
        {"seat_name": "b3", "isTaken": True},
        {"seat_name": "b4", "isTaken": False},
        {"seat_name": "b5", "isTaken": True},
    ],
    3: [
        {"seat_name": "c1", "isTaken": False},
        {"seat_name": "c2", "isTaken": True},
        {"seat_name": "c3", "isTaken": True},
        {"seat_name": "c4", "isTaken": True},
        {"seat_name": "c5", "isTaken": False},
    ],
}


def findSeat(seats, start):
    top = start - 1
    bottom = start + 1
    while top >= 0 or bottom < len(seats):
        if top >= 0 and not seats[top]["isTaken"]:
            return top
        if bottom < len(seats) and not seats[bottom]["isTaken"]:
            return bottom
        top -= 1
        bottom += 1
    return -1


carriageNum = int(input("Enter a carriage number: "))
if carriageNum in data:
    seatName = input("Enter a seat name: ")
    for i, seat in enumerate(data[carriageNum]):
        if seat["seat_name"] == seatName:
            if not seat["isTaken"]:
                print("The seat is free")
            else:
                closest_index = findSeat(data[carriageNum], i)
                if closest_index >= 0:
                    closestSeat = data[carriageNum][closest_index]["seat_name"]
                    print(
                        f"The selected seat is taken. The closest available chair is {closestSeat}."
                    )
                else:
                    print("All chears are busy.")
            break
    else:
        print("Invalid seat name")
else:
    print("Invalid carriage number")
