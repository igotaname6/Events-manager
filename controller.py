from datetime import date
# import date_handle
import view
import events


class UserController:

    def start(self):
        main_menu = view.MainMenu()
        while True:
            choice = self.__class__.handle_menu(main_menu)

            if choice == "1":
                self.book_private_mentoring()
            elif choice == "2":
                self.book_checkpoint()
            elif choice == "3":
                self.print_all_events()
            else:
                self.say_goodbye()

    @staticmethod
    def handle_menu(main_menu):
        main_menu.show()
        choice = None
        while True:
            try:
                try_input = main_menu.get_menu_input()
                choice = try_input
                return choice
            except ValueError:
                main_menu.bad_input()


    def print_all_events(self):

        view.print_all_events(events.Event.get_events())

    def book_event(self):

        pass

    def book_checkpoint(self):

        date = view.get_event_date()
        date = self.__class__.convert_date(date)
        events.Checkpoint(date)

    def book_private_mentoring(self):

        date = view.get_event_date()
        date = self.__class__.convert_date(date)
        events.PrivateMentoring(date)

    def say_goodbye(self):

        view.print_goodbye()

    @staticmethod
    def convert_date(date_str):

        date_list = date_str.split("-")
        return (date(int(date_list[2]), int(date_list[1]), int(date_list[0])))
