import sys

from common import print_tour, read_input
from solver_greedy import solve

def two_opt(tour, dist):
    n = len(tour)
    while True:
        cnt = 0
        for i in range(n - 2):
            for j in range(i + 2, n):  
                if j == n-1:  #jはnを超えてしまうので、その場合1つ目の辺に変更
                    j23 = 0
                else:
                    j23 = j+1
                l1 = dist[tour[i]][tour[i+1]]
                l2 = dist[tour[j]][tour[j23]]
                l3 = dist[tour[i]][tour[j]]
                l4 = dist[tour[i+1]][tour[j23]]
                if l1 + l2 > l3 + l4:  #変更後の辺の合計が小さければ変更
                    new_tour = tour[i+1 : j+1]
                    tour[i+1 : j+1] = new_tour[::-1]
                    cnt += 1 
            
        if cnt == 0:  #改善がみられなかったら終了
            break
    return tour




if __name__ == "__main__":
    assert len(sys.argv) > 1
    tour, dist = solve(read_input(sys.argv[1]))
    tour = two_opt(tour, dist)
    print_tour(tour)