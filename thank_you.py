# skript na etiketu na víno jako poděkování lektorům Digitální akademie

from czechitas import gratitude
import random

czechitas_hearts = ["💙", "💛"]

participants = []

with open(
    "DA_participants.csv", 
    mode = "r",
    encoding = "utf-8"
    ) as grateful_participants:
    for participant in grateful_participants:
        participants.append(participant.strip())

print("Moc moc moc děkujeme!")

for name in participants:
    print(f"{name} {random.choice(czechitas_hearts)}")




# Digitální akadiemie: Data
# podzim 2023






