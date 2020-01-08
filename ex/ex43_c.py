# -*- coding: utf-8 -*-

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
        print "这里没什么需要配置的.这个是一个基类入口."
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
        "非常遗憾的是，你挂了，血肉模糊那种.",
        "-------------游戏结束--------------",
        "-------------谢谢参与--------------"
    ]
    
    def enter(self):
        for line in self.quips:
            print line
        exit(1)

class City(Scene):

    def enter(self):
        print "!!!!!"
        print "你是一个英雄，而且很牛逼!"
        print "现在，你要冲入一座楼里，拯救一个漂亮的妹纸."
        print "那么，问题就来了，你身上并木有武器!"
        print "哟西，你发现了一把RPG火箭筒和一把散弹枪."
        print "但是，你只能选择其中一种武器. (没办法，系统就是这么设定的，只能一种)"
        print "你会选择什么武器咧？火箭筒？散弹枪？（用中文输入武器的名字试试，如“火箭筒”）"
        
        action = raw_input(">")
        os.system("clear")
        
        print "好吧，现在你拿到了%s， 然后兴致勃勃地进入了一个...花园！没错！是个菊花园" % action
        print "\n-------------------------------\n"
        print "惨了，有条龙向你飞了过来，你非常惊慌，必须做点什么！"
    
        if action == "火箭筒":
            print "你拿起了巨大的火箭筒，向巨龙打过去！"
            print "很好！你击中了巨龙，然后，那条龙就这样挂了！"
            return 'building'

        elif action == "散弹枪":
            print "你拿起了散弹枪对着他乱射！"
            print "那条龙太巨型了，你的散弹枪并没什么卵用."
            print "然后你被龙喷了一口火，你就变烧鸡了!"
            return 'death'

        else:
            print "这不是一个好的选择，请务必在“火箭筒”和“散弹枪”之中选一个!"
            return 'city'

class Building(Scene):

    def enter(self):
        print "那头龙虽然很丰满，不，是很强大，但你是个英雄，所以切它像切菜那样！"
        print "你通过菊花园，走进了那座大楼里."
        print "然后发现，你手上的RPG已经没卵用了，所以就把它丢了."
        print "你现在必须找到一些防身用的武器!"
        print "灰常幸运的是，你在一张桌子上捡到了一柄手枪，以及一把军刀.（别问这是哪里来的，肯定是刷出来的）"
        print "然后，你小心地在大楼里到处搜索，到处都充满着危险的味道."
        print "突然，一只僵尸出现了，并向你扑过来."
        print "你拿起了手枪，但突然蒙蔽了，应该射它的头？还是心脏？或者...JJ？（如果它有的话）"

        action = raw_input(">")

        print "PA~PA~~PA~~~~~~~~~~~~~~~"
      
        if action == "头":
            print "那个僵死挂了!所有人都知道，爆头是最有效率的！"
            print "你还活着."
            return 'room'

        else:
            print "你射了它的 %s , 但，并没卵用，它依然健在 " % action
            print "它灰常快的冲到你面前，并咬了你的丁丁."
            print "你没了丁丁，觉得人生已经没有意义了，所以就放弃逃跑了."
            return 'death'
           
class Room(Scene):

    def enter(self):
        print "你杀了那只僵尸之后，进入了其中的一个房间."
        print "\n------------------------------------------------\n"
        print "那个在你任务中要就得那个妹纸就在里面，一动不动."
        print "你对她大喊：嘿，妹纸，叔叔我带你去个安全的地方，然后啪啪啪吧."
        print "然而，那个妹纸并不鸟你，并且不断地摇头表示抗拒."
        print "然后你想，池面的你，没可能有妹纸会拒绝你，你突然发现了房间里面也有个僵尸."
        print "于是，你是要用你手中的手枪打它，还是用军刀去捅它咧？“打”或者“捅”选一个吧"

        action = raw_input(">")
        os.system("clear")
        
        if action == "打":
            print "非常遗憾的是，其实，整个房间都充满这煤气."
            print "你一开枪，就整个房间炸飞了!!"
            return 'death'

        elif action == "捅":
            
            print "\n------------------------------------------------\n"
            print "一开始，你是想用手枪的，但你发现了整个房间充满了煤气，所以你决定用你的刀子."
            print "你一刀捅进它的菊花，不，捅进它的头上，僵尸就挂了."
            print "最后，你带着妹纸，去到一个没人安全的地方，然后就过上幸福的二人世界了."
            print "恭喜你，你成为了人生淫家!"
            print "谢谢参与这个游戏!"
            return 'finished'
        
        else:
            print "虽然你不知道用了个 %s 的方法!" % action
            print "但，那个僵死并木有死，你和妹纸都被他吃掉了."
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
































