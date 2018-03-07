class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class GoldFish(Fish):
    def swim_away(self):
        print("The fish is swimming away.")


samaki = GoldFish("Tilapia")
samaki.swim()
samaki.swim_backwards()
samaki.swim_away()