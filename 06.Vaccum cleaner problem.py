class VacuumCleaner:
    def __init__(self):
        self.location = 0  # 0 represents location A, 1 represents location B
        self.environment = ['Dirty', 'Dirty']  # Initial dirt condition in both locations

    def sense(self):
        return self.environment[self.location]

    def clean(self):
        self.environment[self.location] = 'Clean'

    def move(self):
        if self.location == 0:
            print("Moving to location B")
            self.location = 1
        else:
            print("Moving to location A")
            self.location = 0

    def run(self):
        print("Starting vacuum cleaner...")
        for _ in range(2):
            dirt_condition = self.sense()
            if dirt_condition == 'Dirty':
                print("Cleaning dirt...")
                self.clean()
            print("Moving to next location...")
            self.move()

        print("Cleaning complete!")


if __name__ == "__main__":
    vacuum = VacuumCleaner()
    vacuum.run()
