import time
from typing import Set, Any

from edempy import Deck
import numpy as np
from edempy import BoxBin, CylinderBin
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use("TkAgg")



filepath = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"

deck = Deck(filepath)
def ring_bin_all(time_step=50, deck_name=filepath):

    deck = Deck(deck_name)
    A_boxbin = BoxBin([0, 0, 0.9], 3.6, 2, 1.8)
    B_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.8)
    C_cylinderbin = CylinderBin([0, -1, 0], [0, 1, 0], 1.5)

    """LUPEK"""
    ids_0 = deck.timestep[time_step].particle[0].getIds()
    pos_0 = deck.timestep[time_step].particle[0].getPositions()

    binned_ids_A0 = set(A_boxbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_B0 = set(B_cylinderbin.getBinnedObjects(ids_0, pos_0))
    binned_ids_C0 = set(C_cylinderbin.getBinnedObjects(ids_0, pos_0))

    binned_ids_E0 = binned_ids_B0 - (binned_ids_A0 & binned_ids_B0)
    binned_ids_D0 = binned_ids_C0 - (binned_ids_A0 & binned_ids_C0)
    binned_ids_X0 = binned_ids_E0 - binned_ids_D0

    """PIASKOWIEC"""
    ids_1 = deck.timestep[time_step].particle[1].getIds()
    pos_1 = deck.timestep[time_step].particle[1].getPositions()

    binned_ids_A1 = set(A_boxbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_B1 = set(B_cylinderbin.getBinnedObjects(ids_1, pos_1))
    binned_ids_C1 = set(C_cylinderbin.getBinnedObjects(ids_1, pos_1))

    binned_ids_E1 = binned_ids_B1 - (binned_ids_A1 & binned_ids_B1)
    binned_ids_D1 = binned_ids_C1 - (binned_ids_A1 & binned_ids_C1)
    binned_ids_X1 = binned_ids_E1 - binned_ids_D1

    """DOLOMIT"""
    ids_2 = deck.timestep[time_step].particle[2].getIds()
    pos_2 = deck.timestep[time_step].particle[2].getPositions()

    binned_ids_A2 = set(A_boxbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_B2 = set(B_cylinderbin.getBinnedObjects(ids_2, pos_2))
    binned_ids_C2 = set(C_cylinderbin.getBinnedObjects(ids_2, pos_2))

    binned_ids_E2 = binned_ids_B2 - (binned_ids_A2 & binned_ids_B2)
    binned_ids_D2 = binned_ids_C2 - (binned_ids_A2 & binned_ids_C2)
    binned_ids_X2 = binned_ids_E2 - binned_ids_D2

    print(time_step, " \\ ", deck.numTimesteps)
    return binned_ids_X0, binned_ids_X1, binned_ids_X2


def draw_graph(x, y, is_save=False, is_draw=True):
    fig = plt.figure(figsize=(7, 6))
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    axes.plot(x, y)
    plt.title(f'wydajnosc od czasu')
    plt.xlabel('czas')
    plt.ylabel('Σ masa')

    if is_save:
        plt.savefig(f"wydajnosc_od_czasu__{time.strftime('%m_%d_%Y-%H_%M_%S')}.png")

    if is_draw:
        plt.show()


def main(args):
    start = time.time()
    mass_array = []     # y
    timestep_array = []     # x

    for i in range(1, 261, 50):
        try:
            ids_lup_current, ids_pias_current, ids_dol_current = ring_bin_all(time_step=i)
            ids_lup_prior, ids_pias_prior, ids_dol_prior = ring_bin_all(time_step=i-1)
            ids_lup = ids_lup_current - ids_lup_prior
            ids_pias = ids_pias_current - ids_pias_prior
            ids_dol = ids_dol_current - ids_dol_prior
            mass = 0
            for j in ids_lup:
                mass += deck.timestep[i].particle[0].getMass(j)
            for k in ids_pias:
                mass += deck.timestep[i].particle[1].getMass(k)
            for l in ids_dol:
                mass += deck.timestep[i].particle[2].getMass(l)
            timestep_array.append(round(float(deck.timestepKeys[i]), 2))
            mass_array.append(round(mass,4))
        except Exception:
            timestep_array.append(round(float(deck.timestepKeys[i]), 2))
            mass_array.append(0)
            continue

    print(mass_array)
    print(timestep_array)

    koniec = time.time()
    print("czas: ", koniec - start)

    draw_graph(timestep_array, mass_array)



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


