"""This module provides the solution of the dining philosophers problem."""

from threading import Semaphore, Thread
from time import sleep


class Philosopher(Thread):
    running = True

    def __init__(self, name, left_fork, right_fork, left_fork_number, right_fork_number):
        Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.left_fork_number = left_fork_number
        self.right_fork_number = right_fork_number

    def eat(self):
        print(f"{self.name} started eating\n")
        sleep(5)

    def think(self):
        print(f"{self.name} is thinking\n")
        sleep(2)

    def decide(self):
        while self.running:
            self.think()
            self.left_fork.acquire()
            print(f"{self.name} took left_fork fork number {self.left_fork_number}\n")
            locked = self.right_fork.acquire(False)
            if locked:
                print(f"{self.name} took right_fork fork number {self.right_fork_number}\n")
                break
            self.left_fork.release()
            print(f"{self.name} put the left fork number {self.left_fork_number} back\n")
        else:
            return
        self.eat()
        self.right_fork.release()
        self.left_fork.release()

    def run(self):
        self.decide()


def main():
    philosophers_list = ["Evola", "Heidegger", "Kierkegaard", "Plato", "Sartre"]
    forks = [Semaphore() for _ in range(5)]
    philosophers = [
        Philosopher(
            name=philosophers_list[number],
            left_fork=forks[number],
            right_fork=forks[(number + 1) % 5],
            left_fork_number=number,
            right_fork_number=number - 1 if number != 0 else 4,
        ) for number in range(5)
    ]

    for philosopher in philosophers:
        philosopher.start()
    sleep(20)
    Philosopher.running = False
    print("***Dinner is over***")


if __name__ == "__main__":
    main()
