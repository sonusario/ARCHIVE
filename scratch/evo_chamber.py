from random import randrange
from time import time

def depth_reacher(depth):
    return depth + 1 if randrange(2) else depth_reacher(depth+1)

def test(depth_to_reach, min_limit):
    start_time = time()
    iteration_count = 0
    depth = 0
    greatest_depth = 0
    greatest_depths = {0:1}
    #'''
    while time() - start_time < 60 * min_limit and depth < depth_to_reach:
        depth = 0
        depth = depth_reacher(depth)
        if depth > greatest_depth:
            greatest_depth = depth
            greatest_depths[depth] = [1, [iteration_count]]
        elif depth == greatest_depth:
            greatest_depths[depth][0] += 1
            greatest_depths[depth][1].append(iteration_count)
        iteration_count += 1
    #'''
    return greatest_depth, greatest_depths, iteration_count, time() - start_time

def supertest(min_limit):
    print("\nSuper-Test started...")
    print("="*77)
    start_time = time()
    depth_to_reach = 0
    greatest_depth = 0
    greatest_depths = {}
    iteration_library = {}
    iteration_count = 0
    timer = 0
    #'''
    while timer < 60 * min_limit:
        greatest_depth, greatest_depths, iteration_count, timer = test(depth_to_reach, min_limit)
        if timer >= 60 * min_limit and depth_to_reach-1 > greatest_depth:
            timer = 0
            depth_to_reach -= 1
        elif timer >= 60 * min_limit: continue
        depth_to_reach += 1
        if depth_to_reach in iteration_library:
            iteration_library[depth_to_reach] += iteration_count
        else:
            iteration_library[depth_to_reach] = iteration_count
    #'''
    print("Depth to reach:", depth_to_reach)
    print("Greatest depth:", greatest_depth)
    print("Local iterations for greatest depth:", iteration_count)
    print("Global iterations for the greatest depth:",
          iteration_library[greatest_depth])
    print("Size of depth dictionary:", len(greatest_depths))
    print("-"*77)
    print("Completion time: ", (time()-start_time)/60, "minutes\n")

    return greatest_depths, iteratoin_library

gds, lib = supertest(12)
