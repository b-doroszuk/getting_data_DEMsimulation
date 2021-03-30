import time
from edempy import Deck
import numpy as np
from edempy import BoxBin, CylinderBin
import matplotlib.pyplot as plt
import matplotlib;

matplotlib.use("TkAgg")
from time import strftime

# time_step = 200
deck_name = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"
deck = Deck(deck_name)

print("liczba krokow czasowych", deck.numTimesteps)
print(deck.particleNames)

L_boxbin = BoxBin([0, -0.8, -0.75], 3, 0.25, 1.5)
R_boxbin = BoxBin([0, 0.8, -0.75], 3, 0.25, 1.5)


def left_right_box_graph_all(time_step=200):
    czas = deck.timestepKeys[time_step]
    mass_L = 0
    mass_R = 0

    """LUPEK"""
    binned_ids_L0 = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[0].getIds(),
                                              deck.timestep[time_step].particle[0].getPositions())
    binned_ids_R0 = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[0].getIds(),
                                              deck.timestep[time_step].particle[0].getPositions())

    for i in binned_ids_L0:
        mass_L += deck.timestep[time_step].particle[0].getMass(id=i)
    for i in binned_ids_R0:
        mass_R += deck.timestep[time_step].particle[0].getMass(id=i)

    """PIASEK"""
    binned_ids_L1 = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[1].getIds(),
                                              deck.timestep[time_step].particle[1].getPositions())
    binned_ids_R1 = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[1].getIds(),
                                              deck.timestep[time_step].particle[1].getPositions())

    for i in binned_ids_L1:
        mass_L += deck.timestep[time_step].particle[1].getMass(id=i)
    for i in binned_ids_R1:
        mass_R += deck.timestep[time_step].particle[1].getMass(id=i)

    """DOLOMIT"""
    binned_ids_L2 = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[2].getIds(),
                                              deck.timestep[time_step].particle[2].getPositions())
    binned_ids_R2 = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[2].getIds(),
                                              deck.timestep[time_step].particle[2].getPositions())

    for i in binned_ids_L2:
        mass_L += deck.timestep[time_step].particle[2].getMass(id=i)
    for i in binned_ids_R2:
        mass_R += deck.timestep[time_step].particle[2].getMass(id=i)
    return mass_L, mass_R, czas


def left_right_box_graph_lupek(time_step=200):
    """LUPEK"""
    czas = deck.timestepKeys[time_step]
    mass_L = 0
    mass_R = 0

    binned_ids_L0 = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[0].getIds(),
                                              deck.timestep[time_step].particle[0].getPositions())
    binned_ids_R0 = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[0].getIds(),
                                              deck.timestep[time_step].particle[0].getPositions())

    for i in binned_ids_L0:
        mass_L += deck.timestep[time_step].particle[0].getMass(id=i)
    for i in binned_ids_R0:
        mass_R += deck.timestep[time_step].particle[0].getMass(id=i)
    return mass_L, mass_R, czas


def left_right_box_graph_piaskowiec(time_step=200):
    """PIASEK"""
    czas = deck.timestepKeys[time_step]
    mass_L = 0
    mass_R = 0

    binned_ids_L1 = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[1].getIds(),
                                              deck.timestep[time_step].particle[1].getPositions())
    binned_ids_R1 = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[1].getIds(),
                                              deck.timestep[time_step].particle[1].getPositions())

    for i in binned_ids_L1:
        mass_L += deck.timestep[time_step].particle[1].getMass(id=i)
    for i in binned_ids_R1:
        mass_R += deck.timestep[time_step].particle[1].getMass(id=i)
    return mass_L, mass_R, czas


def left_right_box_graph_dolomit(time_step=200):
    """DOLOMIT"""
    czas = deck.timestepKeys[time_step]
    mass_L = 0
    mass_R = 0

    binned_ids_L2 = L_boxbin.getBinnedObjects(deck.timestep[time_step].particle[2].getIds(),
                                              deck.timestep[time_step].particle[2].getPositions())
    binned_ids_R2 = R_boxbin.getBinnedObjects(deck.timestep[time_step].particle[2].getIds(),
                                              deck.timestep[time_step].particle[2].getPositions())

    for i in binned_ids_L2:
        mass_L += deck.timestep[time_step].particle[2].getMass(id=i)
    for i in binned_ids_R2:
        mass_R += deck.timestep[time_step].particle[2].getMass(id=i)
    return mass_L, mass_R, czas


def main(min_timestep=1, max_timestep=260, timestep_interval=10,
         is_left=True, is_draw_left=True, is_save_left=False,
         is_right=True, is_draw_right=True, is_save_right=False):

    mass_leftbox = []
    mass_rightbox = []
    time = []

    for i in range(min_timestep, max_timestep, timestep_interval):
        mass_L, mass_R, czas = left_right_box_graph_all(time_step=i)
        mass_leftbox.append(round(mass_L, 2))
        mass_rightbox.append(round(mass_R, 2))
        time.append(round(float(czas), 2))
        print(i)

    if is_left:
        fig = plt.figure(figsize=(7, 6))
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.plot(time, mass_leftbox)
        axes.set_xlabel("czas")
        axes.set_ylabel("masa")
        axes.set_title("Left BinBox")
        if is_save_left:
            plt.savefig(f"Left_BinBox_{strftime('%m_%d_%Y-%H_%M_%S')}.png")
        if is_draw_left:
            plt.show()

    if is_right:
        fig = plt.figure(figsize=(7, 6))
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes.plot(time, mass_rightbox)
        axes.set_xlabel("czas")
        axes.set_ylabel("masa")
        axes.set_title("Right BinBox")
        if is_save_right:
            plt.savefig(f"Right_BinBox_{strftime('%m_%d_%Y-%H_%M_%S')}.png")
        if is_draw_right:
            plt.show()

main()
