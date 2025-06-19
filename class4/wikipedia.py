import sys
import collections

class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # Read the pages file into self.titles.
        with open(pages_file, encoding='utf-8') as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()

    
    def show(self):
        """titlesとlinksの中身を表示"""
        i = 0
        for key in self.titles.keys():
            print(key, self.titles[key])
            if i == 10:
                break
            i += 1

        i = 0
        for key in self.links.keys():
            print(key, self.links[key])
            if i == 10:
                break
            i += 1


    # Example: Find the longest titles.
    def find_longest_titles(self):
        titles = sorted(self.titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()


    # Example: Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.titles.keys():
            link_count[id] = 0

        for id in self.titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.titles[dst], link_count_max)
        print()


    # Homework #1: Find the shortest path.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    def find_shortest_path(self, start, goal):
        visited = set()
        queue = collections.deque()
        path = {}  #訪問したノードの親子関係を{child:parent}の形で格納
        for key, value in self.titles.items():  #startのlinkをqueueにappend
            if value == start:
                visited.add(key)
                queue.append(key)
                path[key] = None
                break
        if not queue:  #スタートの文字が含まれなかった場合の例外処理
            print('Tere is not the word in wikipedia.')
            exit(1)
        
        while queue:
            node = queue.popleft()
            if self.titles[node] == goal:
                ans = []
                current = node
                while current:  #ゴールが見つかったら経路をたどって返す
                    ans.append(current)
                    current = path[current]
                print('Shortest path is')
                [print(self.titles[i]) for i in ans[::-1]]
                return
            for child in self.links[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
                    path[child] = node
        else:
            print('There is no path start to goal')





    # Homework #2: Calculate the page ranks and print the most popular pages.
    def find_most_popular_pages(self):

        pass


    # Homework #3 (optional):
    # Search the longest path with heuristics.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    def find_longest_path(self, start, goal):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        pass


    # Helper function for Homework #3:
    # Please use this function to check if the found path is well formed.
    # 'path': An array of page IDs that stores the found path.
    #     path[0] is the start page. path[-1] is the goal page.
    #     path[0] -> path[1] -> ... -> path[-1] is the path from the start
    #     page to the goal page.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    def assert_path(self, path, start, goal):
        assert(start != goal)
        assert(len(path) >= 2)
        assert(self.titles[path[0]] == start)
        assert(self.titles[path[-1]] == goal)
        for i in range(len(path) - 1):
            assert(path[i + 1] in self.links[path[i]])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)
    
    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    # # Example
    # wikipedia.find_longest_titles()
    # # Example
    # wikipedia.find_most_linked_pages()
    # # Homework #1
    wikipedia.find_shortest_path("渋谷", "小野妹子")
    
    # # Homework #2
    # wikipedia.find_most_popular_pages()
    # # Homework #3 (optional)
    # wikipedia.find_longest_path("渋谷", "池袋")