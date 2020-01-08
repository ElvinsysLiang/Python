# This python program used to test a game. 
# The game is, a man in a terrible city.
# He's mission is to save a lady.
# He must go throught the garden, building,
#    at last, into a room to save the lady.
# In the mission there have some weapon he
#    can used to help him.

import os
from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "This scens is not yet configured.\
          Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    
    quips = [
        "Unfortunately, You are died.",
        "---------Game Over----------",
        "-----Thank you for play-----"
    ]
    
    def enter(self):
        for line in self.quips:
            print line
        exit(1)

class City(Scene):

    def enter(self):
        print "!!!!!"
        print "You're the hero in the city!"
        print "Now, you must to go into the building, to save a beautiful lady."
        print "The problem is, you must to get some weapons!"
        print "Oh, there are two weapons at there, a RPG and a Shutgun."
        print "But, you only can choose one of them. (this's setting by syetem, and can't be changed)"
        print "What do you choose? RPG or Shutgun?"
        
        action = raw_input(">")
        os.system("clear")
        
        print "OK, Now you got a %s, and go into a Gardon..." % action
        print "\n-------------------------------\n"
        print "Oh shit! There is a dragon, you must do someting!"
    
        if action == "RPG":
            print "You take the RPG, shot it!"
            print "Year! You kill the dragon!"
            return 'building'

        elif action == "Shutgun":
            print "You take the Shutgun, shot it!"
            print "The dragon is so strong, You can't do anything with the shutgun."
            print "Then the dragon fire you, that is hurt!"
            return 'death'

        else:
            print "That is not a good choice!"
            return 'city'

class Building(Scene):

    def enter(self):
        print "The dragon is so strong, but you're a super hero, kill a dragon is so easy,right?!"
        print "Go throught the Gardon, you go into a building."
        print "The RPG is unuseful in the building, so you throw the RPG away."
        print "You must get a new weapon!"
        print "Hey, you're a lucky boy! You get a hand gun and a knife which are on the the table."
        print "And you search in the building very careful. There are something danguous there."
        print "Suddenly, a zombe appear and rush to bite you."
        print "You must to shot it! But where do you shot, head?body?or other part?"

        action = raw_input(">")

        print "PA~PA~~PA~~~~~~~~~~~~~~~"
      
        if action == "head":
            print "The zombe down. Ok, everyone know shot it head must be work!"
            print "You're alive."
            return 'room'

        else:
            print "You shot its %s part, but there isn't work! " % action
            print "The zombe catch you quickly, and bite you."
            print "You lose your leg, then can not escape."
            return 'death'
           
class Room(Scene):

    def enter(self):
        print "After killed the zombe, you get into a room."
        print "\n------------------------------------------------\n"
        print "A lady who must be save in your mission, stand up there."
        print "You shouted at she: hey, come on, let's go to the safty place."
        print "But she don't come with, even stay there, and shake the head."
        print "Then you see a zombe in the room, so the lady can't walk."
        print "You must kill the zombe, what do you do? shot? or knife?"

        action = raw_input(">")
        os.system("clear")
        
        if action == "shot":
            print "Unfortunately, the room is full of gas."
            print "When you shot, the room is boooooooooom!!"
            return 'death'

        elif action == "knife":
            
            print "\n------------------------------------------------\n"
            print "Before you shot, you smelled the gas! Oh, is so danguous. You can't shot."
            print "You thrust a knife into the zombe's head. Then zombe dead."
            print "At least, you take the beautiful lady to the safty place."
            print "Congretulation! You won!"
            print "Thank you for play this game!"
            return 'finished'
        
        else:
            print "Although you %s, but is not work!" % action
            print "The zombe bite you and lady."
            return 'death'

class Finished(Scene):

    def enter(self):
        print "\n"
        exit(1)

class Map(object):
    
    scenes = {
        'city' : City(),
        'building' : Building(),
        'room' : Room(),
        'death' : Death(),
        'finished' : Finished()
    }  

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('city')
a_game = Engine(a_map)
a_game.play()
































