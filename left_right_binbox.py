import time
from edempy import Deck
import numpy as np
from edempy import BoxBin, CylinderBin
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use("TkAgg")
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

def maintance_time(binbox_name="left", is_draw=True, is_save=False):
    #'ResidenceTime_Example.dem')
    deck = Deck(deck_name)
    nTimesteps = deck.numTimesteps

    # Step 1: Define size of a single timestep and bin x, y, z max/min
    tstep = deck.timestep[1].timestep  # Size of a single timestep

    if binbox_name == "left":
        boxbin = L_boxbin   #BoxBin([0, -0.8, -0.75], 3, 0.25, 1.5)
    elif binbox_name == "right":
        boxbin = R_boxbin   #BoxBin([0, 0.8, -0.75], 3, 0.25, 1.5)
    else:
        raise Exception("Insert name BinBox (Left or Right)")

    # Step 2: Create empty dict to count pID residence time
    insideBin = {}  # Use dict for speed {pID:count}

    for i in range(1, nTimesteps):
        # Step 3: Loop ids per timestep, if particle is inside bin add to the count in "insideBin"
        ids = deck.timestep[i].particle[0].getIds()
        pos = deck.timestep[i].particle[0].getPositions()
        p_ids = boxbin.getBinnedObjects(ids, pos)
        for p_id in p_ids:
            if p_id in insideBin:
                insideBin[p_id] = insideBin[p_id] + 1  # If already in dict add 1 to the count
            else:
                insideBin.update({p_id: 1})  # If not in the dict, add it, and add 1 to the count

    # Step 5: Plot data as a histogram
    #ids = np.array(list(insideBin.keys()))
    residenceTime = np.array(list(insideBin.values())) * tstep
    print(type(insideBin.values()))
    print(type(list(insideBin.values())))
    plt.hist(residenceTime, 11)
    plt.xlabel('Residence Time [s]')
    plt.ylabel('Frequency')
    plt.title(f'Residence Time Histogram where particle in {binbox_name} BinBox')
    if is_save:
        plt.savefig(f"Resistance_Time_{binbox_name}_BinBox_{strftime('%m_%d_%Y-%H_%M_%S')}.png")
    if is_draw:
        plt.show()


def main(min_timestep=1, max_timestep=260, timestep_interval=10,
         is_left=True, is_draw_left=True, is_save_left=False,
         is_right=True, is_draw_right=True, is_save_right=False):

    mass_leftbox = []
    mass_rightbox = []
    time = []

    if is_left and is_right:
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

main(False,False,False,False,False,False,)
