import os
import time
import sys

class UI:
    @staticmethod
    def build_table(headers, table):

        retable = []
        width_list = []
        parsed_table = [headers] + table

        # calculate longest string in the content
        for i in range(len(parsed_table[0])):
            longest_string = 0
            for row in parsed_table:
                if len(str(row[i])) > longest_string:
                    longest_string = len(str(row[i]))
            width_list.append(longest_string)

        # print header
        retable.append("╔")
        for column in range(len(parsed_table[0])):
            retable.append("{0:═^{w}}".format("═", w=width_list[column] + 2))
            if column + 1 != len(parsed_table[0]):
                retable.append("╦")
        retable.append("╗\n")
        # print content
        for row_number, row in enumerate(parsed_table):
            for column, cell in enumerate(row):
                retable.append("║{0:^{w}}".format(str(cell), w=width_list[column] + 2))
            retable.append("║\n")
            if row_number + 1 != len(parsed_table):
                retable.append("╠")
                for column, cell in enumerate(row):
                    retable.append("{0:═^{w}}".format("═", w=width_list[column] + 2))
                    if column + 1 != len(parsed_table[0]):
                        retable.append("╬")
                retable.append("╣\n")
            # print footer
            if row_number + 1 == len(parsed_table):
                retable.append("╚")
                for column, cell in enumerate(row):
                    retable.append("{0:═^{w}}".format("═", w=width_list[column] + 2))
                    if column + 1 != len(parsed_table[0]):
                        retable.append("╩")
                retable.append("╝")

        return ("".join(retable))

    @staticmethod
    def print_result(result):
        os.system('clear')
        print(result)

    @staticmethod
    def welcome_screen():
        os.system('clear')
        print("WELCOME")
        time.sleep(2)
        os.system('clear')
        print("Loading data . . . \n\nPlease wait")
        time.sleep(3)

    @staticmethod
    def print_menu():
        os.system('clear')
        print("""What would you like to do:
   (1) List statistics
   (2) Display 3 cities with longest names
   (3) Display county's name with the largest number of communities
   (4) Display locations, that belong to more than one category
   (5) Advanced search
   (0) Exit program
""")

    @staticmethod
    def user_input(message):
        return input(message)