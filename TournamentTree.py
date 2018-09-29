CAPACITY = 16
Team_List = [1, 16, 8, 15, 9, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 5]
Total_Teams = len(Team_List)
Games = Total_Teams-1


class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class Tournament(object):
    def __init__(self):
        self.teams = []
        self.next_round = []
        self.count_comp = 0

    def insert(self, value):
        if len(self.teams) < Total_Teams:
            self.teams.append(Node(value))
        else:
            print("Tournament Full")

    def play_tournament(self, team_list):
        if len(self.teams) != Total_Teams:
            print("Can't play, tournament not full.")
        else:
            while len(self.teams) > 1:
                self.__play_round__(self.teams)

    def __play_round__(self, players):
        for i in range(0, len(players), 2):
            self.count_comp+=1
            winner = Node(max(players[i].data, players[i+1].data))
            winner.leftChild = players[i]
            winner.rightChild = players[i+1]
            self.__promote__(winner)
        self.teams = self.next_round
        self.next_round = []

    def __promote__(self, winner):
        self.next_round.append(winner)

    def find_second_best(self):
        node = self.teams[0]
        second_best = -1
        while node.rightChild and node.leftChild:
            self.count_comp += 1
            if node.rightChild.data == node.data:
                second_best = max(second_best,node.leftChild.data)
                node = node.rightChild

            elif node.leftChild.data == node.data:
                second_best = max(second_best,node.rightChild.data)
                node = node.leftChild

        return second_best


def main():
    T = Tournament()
    for i in range(0, Total_Teams):
        T.insert(Team_List[i])
    T.play_tournament(T.teams)

    print(T.find_second_best())
    print(T.count_comp)


if __name__ =='__main__':
    main()