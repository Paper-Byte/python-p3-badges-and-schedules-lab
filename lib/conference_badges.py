def badge_maker(name):
    return str(f'Hello, my name is {name}.')


def batch_badge_creator(names):
    return [(f'Hello, my name is {name}.') for name in names]


def assign_rooms(names):
    assignmeant = []
    room = 1
    for name in names:
        assignmeant.append(
            f"Hello, {name}! You'll be assigned to room {room}!")
        room += 1
    return assignmeant


def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
