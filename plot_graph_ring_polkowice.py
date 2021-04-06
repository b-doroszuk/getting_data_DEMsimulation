import time
from edempy import Deck
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib; matplotlib.use("TkAgg")
import ring_polkowice


class Get_DEM_data():

    def __init__(self, enter_time_step=260, rock_number=0, is_save=False, is_draw=True, out_number=1):
        # "D:\Polkowice\Kruszarka_Polkowice.dem"
        # "RockBox_Example.dem"
        #"C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\rock_example\\RockBox_Example.dem"
        self.t = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"
        self.deck = Deck(self.t)
        self.time_step = enter_time_step
        self.rock_number = rock_number

        self.out_number = out_number
        self.is_save = is_save
        self.is_draw = is_draw

    def get_ids_set(self):
        """getting ID particle"""
        return self.deck.timestep[self.time_step].particle[self.rock_number].getIdsSet()

    def get_mass(self):
        """getting mass particles"""
        return self.deck.timestep[self.time_step].particle[self.rock_number].getMass()

    def get_dummy_mass(self):
        return self.deck.timestep[self.time_step].particle[5].getMass()

    def get_diameter(self):
        """getting diameters particles in millimeters"""
        return self.deck.timestep[self.time_step].particle[self.rock_number].getSphereRadii() * 2 * 1000

    def get_number_all_time_steps(self):
        return self.deck.numTimesteps

    def get_name(self, number):
        """getting rock name"""
        return self.deck.creatorData.particle[number].getName()

    def draw_plot(self, section_1=5, section_2=10, section_3=15, section_4=20, section_5=40, section_6=80):
        fig = plt.figure(figsize=(7, 6))
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        dol_m, dol_d = ring_polkowice.ring_bin_dolomit(time_step=self.time_step, deck_name=self.t)
        #dol_m = list(dol_m)
        #dol_d = list(dol_d)
        # dol_d = dol_diameter + lup_diameter + pia_diameter
        #dol_d = list(self.get_diameter)
        print(dol_d)
        # dol_m = dol_mass + lup_mass + pia_mass
        #dol_m = list(self.get_mass)
        print(dol_m)

        dummy_sum = 0.00001 # sum(self.get_dummy_mass)  #  #float(dummy[1]) + float(dummy[2]) + float(dummy[3])
        sum_dol_dum = sum(dol_m) + dummy_sum
        print(sum_dol_dum)

        dol_m.sort()
        dol_d.sort()

        dol_dd = [[], [], [], [], [], []]
        for i in dol_d:
            if i <= section_1:
                dol_dd[0].append(i)
            elif i <= section_2:
                dol_dd[1].append(i)
            elif i <= section_3:
                dol_dd[2].append(i)
            elif i <= section_4:
                dol_dd[3].append(i)
            elif i <= section_5:
                dol_dd[4].append(i)
            else:
                dol_dd[5].append(i)

        dol_dm = [[], [], [], [], [], []]
        j = 0
        if_0 = len(dol_dd[0])
        if_1 = (if_0 + len(dol_dd[1]))
        if_2 = (if_1 + len(dol_dd[2]))
        if_3 = (if_2 + len(dol_dd[3]))
        if_4 = (if_3 + len(dol_dd[4]))
        if_5 = (if_4 + len(dol_dd[5]))
        for i in dol_m:
            if j < if_0:
                dol_dm[0].append(i + (dummy_sum / len(dol_dd[0])))
                j += 1
            elif if_0 <= j < if_1:
                dol_dm[1].append(i)
                j += 1
            elif if_1 <= j < if_2:
                dol_dm[2].append(i)
                j += 1
            elif if_2 <= j < if_3:
                dol_dm[3].append(i)
                j += 1
            elif if_3 <= j < if_4:
                dol_dm[4].append(i)
                j += 1
            elif if_4 <= j < if_5:
                dol_dm[5].append(i)
                j += 1
            else:
                break

        print(len(dol_dm[0]))
        print()
        print(len(dol_dm[1]))
        print()
        print(len(dol_dm[2]))
        print()
        print(len(dol_dm[3]))
        print()
        print(len(dol_dm[4]))
        print()
        print(len(dol_dm[5]))
        print()
        print()
        print()
        print(len(dol_dd[0]))
        print()
        print(len(dol_dd[1]))
        print()
        print(len(dol_dd[2]))
        print()
        print(len(dol_dd[3]))
        print()
        print(len(dol_dd[4]))
        print()
        print(len(dol_dd[5]))
        print()

        # print(dol_dm)
        one = sum(dol_dm[0]) / sum_dol_dum
        two = sum(dol_dm[1]) / sum_dol_dum + one
        three = sum(dol_dm[2]) / sum_dol_dum + two
        four = sum(dol_dm[3]) / sum_dol_dum + three
        five = sum(dol_dm[4]) / sum_dol_dum + four
        six = sum(dol_dm[5]) / sum_dol_dum + five

        print("one", one)
        print("two", two)
        print("three", three)
        print("four", four)
        print("five", five)
        print("six", six)

        count_1 = 0
        f_1 = (0.80 * sum_dol_dum)
        s_value_1 = 0
        for i in dol_m:
            if s_value_1 <= f_1:
                if dol_dd[0]:
                    if count_1 <= len(dol_dd[0]):
                        s_value_1 += (i + (dummy_sum / len(dol_dd[0])))
                        count_1 += 1
                    else:
                        s_value_1 += i
                        count_1 += 1
                else:
                    break
            else:
                break
        # axes.plot(dol_d[count_1], 80, 'o', color='k')
        axes.text(dol_d[count_1] + 0.5, 80, f" {round(dol_d[count_1], 2)} w 80%")

        count_2 = 0
        f_2 = (0.50 * sum_dol_dum)
        s_value_2 = 0
        for i in dol_m:
            if s_value_2 <= f_2:
                if dol_dd[0]:
                    if count_2 <= len(dol_dd[0]):
                        s_value_2 += (i + (dummy_sum / len(dol_dd[0])))
                        count_2 += 1
                    else:
                        s_value_2 += i
                        count_2 += 1
                else:
                    break
            else:
                break
        # axes.plot(dol_d[count_2], 50, 'o', color='k')
        axes.text(dol_d[count_2] + 0.5, 50, f" {round(dol_d[count_2], 2)} w 50%")

        count_3 = 0
        f_3 = (0.15 * sum_dol_dum)
        s_value_3 = 0
        for i in dol_m:
            if s_value_3 <= f_3:
                if dol_dd[0]:
                    if count_3 <= len(dol_dd[0]):
                        s_value_3 += (i + (dummy_sum / len(dol_dd[0])))
                        count_3 += 1
                    else:
                        s_value_3 += i
                        count_3 += 1
                else:
                    break
            else:
                break

        """POINTS"""
        if dol_dm[4] and dol_dm[5]:
            tab_1 = [0, section_1, section_2, section_3, section_4, section_5, section_6]
            tab_2 = [0, one * 100, two * 100, three * 100, four * 100, five * 100, six * 100]
            if dol_d[count_1] > tab_1[5]:
                axes.plot([dol_d[count_1], tab_1[6]], [80, tab_2[6]], color='b')
                axes.plot([tab_1[0], tab_1[1]], [tab_2[0], tab_2[1]], color='b')
                print("pierwszy")
            else:
                axes.plot([tab_1[5], tab_1[6]], [tab_2[5], tab_2[6]], color='b')
                axes.plot([tab_1[0], tab_1[1]], [tab_2[0], tab_2[1]], color='b')

                print("drugi")
            print("laczy sie do 80%", [dol_d[count_1], tab_1[6]], [80, tab_2[6]])
            print("laczy sie do zwyklego", [tab_1[5], tab_1[6]], [tab_2[5], tab_2[6]])
            Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]],
                      [dol_d[count_3], 15], [tab_1[2], tab_2[2]], [dol_d[count_2], 50],
                      [dol_d[count_1], 80], [tab_1[3], tab_2[3]], [tab_1[4], tab_2[4]],
                      [tab_1[5], tab_2[5]], [tab_1[6], tab_2[6]]]
            Points.sort(key=lambda x: x[1])
            print(Points)

        elif dol_dm[4] and not dol_dm[5]:
            tab_1 = [0, section_1, section_2, section_3, section_4, section_5]
            tab_2 = [0, one * 100, two * 100, three * 100, four * 100, five * 100]
            if dol_d[count_1] > tab_1[4]:
                axes.plot([dol_d[count_1], tab_1[5]], [80, tab_2[5]], color='b')
                axes.plot([tab_1[0], tab_1[1]], [tab_2[0], tab_2[1]], color='b')
            else:
                axes.plot([tab_1[4], tab_1[5]], [tab_2[4], tab_2[5]], color='b')
                axes.plot([tab_1[0], tab_1[1]], [tab_2[0], tab_2[1]], color='b')
            Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]],
                      [dol_d[count_3], 15], [tab_1[2], tab_2[2]], [dol_d[count_2], 50],
                      [dol_d[count_1], 80], [tab_1[3], tab_2[3]], [tab_1[4], tab_2[4]],
                      [tab_1[5], tab_2[5]]]
            Points.sort(key=lambda x: x[1])

        else:
            tab_1 = [0, section_1, section_2, section_3, section_4]
            tab_2 = [0, one * 100, two * 100, three * 100, four * 100]
            if dol_d[count_1] > tab_1[3]:
                axes.plot([dol_d[count_1], tab_1[4]], [80, tab_2[4]], color='b')
                axes.plot([tab_1[0], tab_1[1]], [tab_2[0], tab_2[1]], color='b')
            else:
                axes.plot([tab_1[3], tab_1[4]], [tab_2[3], tab_2[4]], color='b')
                axes.plot([tab_1[0], tab_1[1]], [tab_2[0], tab_2[1]], color='b')

            Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]],
                      [dol_d[count_3], 15], [tab_1[2], tab_2[2]], [dol_d[count_2], 50],
                      [dol_d[count_1], 80], [tab_1[3], tab_2[3]], [tab_1[4], tab_2[4]]]
            Points.sort(key=lambda x: x[1])

        def CatmullRomSpline(P0, P1, P2, P3, nPoints=100):
            """
            P0, P1, P2, and P3 should be (x,y) point pairs that define the Catmull-Rom spline.
            nPoints is the number of points to include in this curve segment.
            """
            # Convert the points to numpy so that we can do array multiplication
            P0, P1, P2, P3 = map(np.array, [P0, P1, P2, P3])

            # Parametric constant: 0.5 for the centripetal spline, 0.0 for the uniform spline, 1.0 for the chordal spline.
            alpha = 0.3  # 0.5
            # Premultiplied power constant for the following tj() function.
            alpha = alpha / 2

            def tj(ti, Pi, Pj):
                xi, yi = Pi
                xj, yj = Pj
                return ((xj - xi) ** 2 + (yj - yi) ** 2) ** alpha + ti

            # Calculate t0 to t4
            t0 = 0
            t1 = tj(t0, P0, P1)
            t2 = tj(t1, P1, P2)
            t3 = tj(t2, P2, P3)

            # Only calculate points between P1 and P2
            t = np.linspace(t1, t2, nPoints)

            # Reshape so that we can multiply by the points P0 to P3
            # and get a point for each value of t.
            t = t.reshape(len(t), 1)
            A1 = (t1 - t) / (t1 - t0) * P0 + (t - t0) / (t1 - t0) * P1
            A2 = (t2 - t) / (t2 - t1) * P1 + (t - t1) / (t2 - t1) * P2
            A3 = (t3 - t) / (t3 - t2) * P2 + (t - t2) / (t3 - t2) * P3
            B1 = (t2 - t) / (t2 - t0) * A1 + (t - t0) / (t2 - t0) * A2
            B2 = (t3 - t) / (t3 - t1) * A2 + (t - t1) / (t3 - t1) * A3
            C = (t2 - t) / (t2 - t1) * B1 + (t - t1) / (t2 - t1) * B2
            return C

        def CatmullRomChain(P):
            """
            Calculate Catmull–Rom for a chain of points and return the combined curve.
            """
            sz = len(P)

            # The curve C will contain an array of (x, y) points.
            C = []
            for i in range(sz - 3):
                c = CatmullRomSpline(P[i], P[i + 1], P[i + 2], P[i + 3])
                C.extend(c)

            return C

        # Define a set of points for curve to go through
        # Points = [[tab_1[0], tab_2[0]], [tab_1[1], tab_2[1]], [tab_1[2], tab_2[2]],[dol_d[count_2], 50]

        # Calculate the Catmull-Rom splines through the points
        c = CatmullRomChain(Points)
        # Convert the Catmull-Rom curve points into x and y arrays and plot
        x, y = zip(*c)
        plt.plot(x, y, color='b')

        # Plot the control points
        # px, py = zip(*Points)
        # plt.plot(px, py, 'o', color='r')

        """Plotting points and additionals"""
        axes.plot(dol_d[count_2], 50, 'o', color='k')
        axes.plot(dol_d[count_1], 80, 'o', color='k')
        axes.plot(tab_1, tab_2, 'o', color='b')  # draw points

        blue_line = mlines.Line2D([], [], color='blue', marker='o', label=f'wychód {self.out_number}')
        plt.legend(handles=[blue_line])
        plt.title(f'wychód {self.out_number}')
        plt.xlabel('górna granica przedzialu')
        plt.ylabel('Σ masa %')

        if self.is_draw:
            plt.show()
        if self.is_save:
            plt.savefig(f"wychod{self.out_number}__{time.strftime('%m_%d_%Y-%H_%M_%S')}__{self.time_step}.png")

def main(args):
    """main function"""

    test = Get_DEM_data(enter_time_step=220)
    print(test.get_number_all_time_steps)

    test.draw_plot()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


