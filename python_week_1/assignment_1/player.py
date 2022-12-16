import pickle


class Player:
    instances = set()

    def __init__(self, name, position=0):
        self.name = name
        self.position = position
        Player.instances.add(self)

    @staticmethod
    def save_player_info():
        f = open("player info", "wb")
        pickle.dump(list(Player.get_instances()), f)
        f.close()

    def update_position(self, new_position):
        self.position = new_position
        Player.save_player_info()

    @classmethod
    def get_instances(cls):
        return cls.instances

