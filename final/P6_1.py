#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:58:05 2017 @author: lingtoby
"""
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. '+self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        print('eric says: It is obvious that I believe that eric says: the sky is blue')
        return Person.say(self,self.lecture(stuff))
    def lecture(self, stuff):         
        #print('It is obvious that I believe that eric says: the sky is blue')
        return 'It is obvious that '+ Lecturer.lecture(self,stuff)

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')


"""
>>> pe.say('the sky is blue')
Prof. eric says: I believe that eric says: the sky is blue 

>>> ae.say('the sky is blue')
Prof. eric says: It is obvious that I believe that eric says: the sky is blue 
"""
