import random

# Insert Graphs Data: Key == Vertex ( int ), Values == Edges ( int ) ( array structured ) ( No Limits so far )
pool = {int(): [], int(): [], int(): [], int(): [], int(): [], int(): [],
        int(): [], int(): [], int(): []}

# Final stations of Euler Tour
final_e_tour = []


def euler_tour():
    # Set Starting Point ( Key, Value / Index in array )
    final_e_tour.append(pool[1][0])

    not_finished = True

    while not_finished is True:
        final_e_tour_last_element = final_e_tour[-1]
        next_station = random.sample(pool[final_e_tour_last_element], 1)
        final_e_tour.extend(next_station)
        # Set Control if all stations have been past
        final_set = set(final_e_tour)
        # Halt Condition
        if len(final_set) == len(pool) and final_e_tour[-1] == final_e_tour[0]:
            print("Stations Past:", final_set)
            print("Euler Tour:", final_e_tour)
            not_finished = False


euler_tour()


