import syrupy

class View:
    direction: str = ""

    def __init__(self, direction: str):
        self.direction = direction


class Window:
    views = set()

    def __init__(self, views: set[View]):
        self.views = views


class Room:
    name = ""
    windows = []

    def __init__(self, name: str, windows: list[Window]):
        self.name = name
        self.windows = windows


class Mansion:
    rooms = []

    def __init__(self, rooms: list[Room]):
        self.rooms = rooms


def test_failing_test(snapshot: syrupy.SnapshotAssertion):
    """Supposed to fail as I'm trying to recreate the 'Click to see difference' text in the PyCharm test runner."""
    assert Mansion(rooms=[Room(name="kitchen", windows=[Window(views={View("NE"), View("E")})])]) == snapshot
