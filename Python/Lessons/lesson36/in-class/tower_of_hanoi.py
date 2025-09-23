class TowerOfHanoi:
    def __init__(self, num_plates):
        self.num_plates = num_plates

    def move(self, plate, origin, destination, buffer):
        if plate == 1:
            print(f'Move plate size-{plate} from {origin} to {destination}')
            return
        self.move(plate - 1, origin, buffer, destination)
        print(f'Move plate size-{plate} from {origin} to {destination}')
        self.move(plate - 1, buffer, destination, origin)

    def solve(self):
        self.move(self.num_plates, 'origin', 'destination', 'buffer')

if __name__ == "__main__":
    hanoi = TowerOfHanoi(4)
    hanoi.solve()