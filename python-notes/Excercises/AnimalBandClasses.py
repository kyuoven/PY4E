class AnimalBand(object):
    def __init__(self, animal, instrument, song, description):
        self.animal = animal
        self.instrument = instrument
        self.song = song
        self.description = description

First_act = AnimalBand(
    "Dog",
    "Guitar",
    "Sweet Home Alabama",
    """The lousy dog lazily strokes the strings of his out-of-tune guitar, almost barely getting the notes right."""
    )

Second_act = AnimalBand(
    "Cat",
    "Piano",
    "Moonlight Sonata",
    """The cat rolls over the notes with as much glamour as well as cockiness."""
    )

Third_act = AnimalBand(
    "Bird",
    "Flute",
    "Jingle Bells",
    """The bird knows it is the best at its art, for it does not need an instrument to sing."""
    )

print("Here we have the First act! Our animal: " , First_act.animal)
print("And their instrument of choice: " , First_act.instrument)
print("They will be playing: " , First_act.song)
print(First_act.description)
print("\n")

print("Here we have the Second act! Our animal: " , Second_act.animal)
print("And their instrument of choice: " , Second_act.instrument)
print("They will be playing: " , Second_act.song)
print(Second_act.description)
print("\n")

print("Here we have the First act! Our animal: " , Third_act.animal)
print("And their instrument of choice: " , Third_act.instrument)
print("They will be playing: " , Third_act.song)
print(Third_act.description)





    