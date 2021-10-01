from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    num_points = len(points)
    holder = [0]*len(points[0])
    for x in points:
        for j in range(len(x)):
            holder[j] += x[j]
    
    for sums in holder:
        sums = sums / num_points
    return holder


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    assign_set = set(assignments)
    k = len(assign_set)
    #print(k)
    centers = []
    for team in assign_set:
        temp_holder = []
        for i in range(len(dataset)):
            if (assignments[i] == team):
                temp_holder.append(dataset[i])

        centers.append(point_avg(temp_holder))  
    #print(k, len(centers))      
    return centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    #print(set(assignments), len(centers))     
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i])**2
    return res**(1/2)

def distance_squared(a, b):
    return distance(a, b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    init_p = []
    pindex = []
    while (len(pindex) < k):
        ind = random.randint(0,len(dataset) - 1)
        if(ind not in pindex):
            pindex.append(ind)
            init_p.append(dataset[ind])
    print(k, len(init_p))
    print(init_p)       
    return init_p

def cost_function(clustering):
    cost_sum = 0
    k = len(clustering)
    for i in range(k):
        center = point_avg(clustering[i])
        for points in clustering[i]:
            cost_sum += distance_squared(points, center)
    return cost_sum


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    init_p = []
    pindex = []
    pdf = []
    ind = random.randint(0,len(dataset) - 1)
    if(ind not in pindex):
        pindex.append(ind)
        init_p.append(dataset[ind])
    for i in range(len(dataset)):
        d2 = distance_squared(dataset[i], init_p[0])
        if i == 0:
            pdf.append(d2)
        else:
            pdf.append(d2 + pdf[i-1])
    cdf = [x/pdf[len(dataset) - 1] for x in pdf]

    while (len(pindex) < (k-1)):
        tp = random.random()
        ind = 0
        while(tp > cdf[ind]):
            ind += 1
        if(ind not in pindex):
            pindex.append(ind)
            init_p.append(dataset[ind])

    return init_p


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
