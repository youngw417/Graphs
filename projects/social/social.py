from util import Queue
import random
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {} # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}") # Create Frienships
        # Generate all possible friendship combinations
        possible_friendships = [] # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id)) # Shuffle the possible friendships
        random.shuffle(possible_friendships)
         # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        count = 0
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            count += 1
            # print(count)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        for shortest search, use bft
        create q and enqueue user_id in list
        get a visited list

        """
  
        q = Queue()
        q.enqueue([user_id])  # enqueue the first id
        visited = {}  # Note that this is a dictionary, not a set
        while q.size() > 0:
            path = q.dequeue()  
            id = path[-1]  # gt the last item in the path list
            if id not in visited: # if the last id (user or a friend) is not visited
                visited[id] = path  # use id as key and path list in value
  
                for friend in self.friendships[id]:  # get all friends in the given id, contained in set
                    new_path = path + [friend]  # append the friend in the list 
                    q.enqueue(new_path) # enqueue the new list
        print(f"There are {float(len(visited) - 1) / len(self.users) * 100}% users in user's network")
        print('\n')
        count2 = 0
        for key in visited:
            count2 += (len(visited[key]) - 1)
 
        avg_sep =  float(count2) / (len(visited) -1)
        format_avg = "{:.2f}".format(avg_sep)
        print(f'Average number of separation is {format_avg} \n')

        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    print('\n')
    connections = sg.get_all_social_paths(1)
    print(connections)
# {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}