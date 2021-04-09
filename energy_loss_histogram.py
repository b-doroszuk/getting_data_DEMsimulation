import edempy

filepath = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"
filepath2 = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\rock_example\\RockBox_Example.dem"


deck = edempy.Deck(filepath2)

#print(deck.timestepValues) wartosci w czasie
#print(deck.timestep[10].particle[0].getIds())
print(deck.timestep[160].energy.getLossFromContacts())
print(deck.timestep[160].energy.getLossFromCapping())
#print(deck.timestep[100].contact.surfGeom.getContacts())

print(len(deck.timestep[100].contact.surfSurf.getIds()))
for i in range(261):
    try:
        print(deck.timestep[i].collision.surfGeom.getIds())
        print("udalo sie", i)
    except Exception:
        continue
#print(deck.timestep[100].collision.surfSurf.)
#print(deck.timestep[100].energy.getSystemEnergy())

#print(deck.timestep[0].collision.surfGeom.getStartTime())

print(deck.timestep[20].collision.surfSurf.getNormalEnergy())