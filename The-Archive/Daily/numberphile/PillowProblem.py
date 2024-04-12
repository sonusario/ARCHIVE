from random import randrange

class new_bag:
    def __init__(self):
        self.refresh()

    def iterate(self):
        pulled_out = self.ball_1 if randrange(2) else self.ball_2
        print("You pulled out a " + pulled_out + " ball!")
        print("This " + pulled_out + " ball has been placed back into the bag.")

    def contents(self):
        print("The bag contains a red ball and a " + self.ball_2 + " ball.")
        print("The bag contents will now be refreshed...")
        self.refresh()

    def refresh(self):
        self.ball_1 = "red"
        self.ball_2 = "red" if randrange(2) else "green"
        print("Papa's got a brand new bag!")

bag = new_bag()
bag.iterate()



