class VacuumCleanerEnvironment:
    def __init__(self, initial_status):
        self.location_status = initial_status
        self.vacuum_location = 'A'  # The vacuum starts at location A

    def get_location_status(self):
        return self.location_status[self.vacuum_location]

    def clean_location(self):
        print(f"Cleaning location {self.vacuum_location}")
        self.location_status[self.vacuum_location] = 0

    def move_to(self, location):
        print(f"Moving from {self.vacuum_location} to {location}")
        self.vacuum_location = location

class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment

    def decide_action(self):
        if self.environment.get_location_status() == 1:  # If the current location is dirty
            self.environment.clean_location()
        else:  # If the current location is clean, move to the other location
            if self.environment.vacuum_location == 'A':
                self.environment.move_to('B')
            else:
                self.environment.move_to('A')

def get_user_input():
    while True:
        try:
            a_status = int(input("Enter the status of location A (1 for dirty, 0 for clean): "))
            b_status = int(input("Enter the status of location B (1 for dirty, 0 for clean): "))
            steps = int(input("Enter the number of steps for the simulation: "))

            if a_status not in [0, 1] or b_status not in [0, 1] or steps < 0:
                print("Invalid input. Status must be 0 or 1, and steps must be a non-negative integer.")
                continue

            initial_status = {'A': a_status, 'B': b_status}
            return initial_status, steps

        except ValueError:
            print("Invalid input. Please enter integers only.")

def run_vacuum_cleaner():
    initial_status, steps = get_user_input()
    environment = VacuumCleanerEnvironment(initial_status)
    agent = VacuumCleanerAgent(environment)

    for step in range(steps):
        print(f"\nStep {step + 1}:")
        agent.decide_action()
        print(f"Current status: {environment.location_status}")

    print("\nFinal status of the environment:", environment.location_status)

if __name__ == "__main__":
    run_vacuum_cleaner()
