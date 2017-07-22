from mentor import Mentor
from events import *
from abc import ABCMeta
from datetime import date

class Menu:

    __metaclass__ = ABCMeta

    def __init__(self, options, headline):
        self.headline = headline
        self.options = options

    def __str__(self):
        return_string = '----------\n'
        return_string += self.headline + '\n' + '----------\n\n'

        for i in range(len(self.options)):
            id = i+1
            return_string += '{}. {}\n'.format(id, self.options[i])
        return return_string

    def show(self):
        print(self)

    def get_menu_input(self):
        menu_input = input(": ")
        if int(menu_input) not in range(len(self.options) + 1):
            raise ValueError
        return menu_input

    @staticmethod
    def bad_input():
        print('Inappropriate choice. ')


class MainMenu(Menu):

    headline = "Choose option: "
    options = [
                "Book private mentoring",
                "Book checkpoint",
                "Show all my events"
              ]

    def __init__(self):
        super().__init__(self.__class__.options, self.__class__.headline)


class MentorsMenu(Menu):

    def __init__(self):
        super().__init__(mentor.mentors, 'Select Mentor')


class Options:

    @staticmethod
    def print_all_events():
        for event in event.events:
            print(event)

    @staticmethod
    def print_goodbye():
        print("Bye bye")

    @staticmethod
    def get_choice():
        return input("Choose option: ")

    @staticmethod
    def get_event_date():
        while True:
            try:
                month = input('Enter month from 1-12:  ')
                day = input('enter day:')
                event_date = date(2017, month, day)
                return event_date
            except TypeError, ValueError:
                print("Enter propper date.")


def get_checkpoint_details():

    return self.get_event_date()


def get_event_date():

    return input("Enter date dd-mm-yyyy: ")


def get_goal(self):

    return input("Enter your goal: ")
