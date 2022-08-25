# import csv
# import sys
import time
# from itertools import zip_longest
import pandas as pd


def player_menu(name):
      print("\n" * 100)
      df = pd.read_csv("PuttingStats.csv")
      print("-------{}'s Stats-------".format(name))
      print(df[(df == name).any(axis=1)])
      print("1 to view leaderboard")
      print("2 to add stats")
      ask = input()
      if(ask == "1"):
            main_menu()
      elif(ask == "2"):
            hits = input("Enter amount of new hits\n")
            try:
                  val = int(hits)
            except ValueError:
                  print("Enter a number")
                  player_menu(name)
            if (val < 1):
                  print("Enter a value greater than 0")
                  player_menu(name)
            else:
                  df.loc[df.Name == name, 'Hits'] += val

                  misses = input("How many misses?\n")

                  try:
                        missed = int(misses)
                  except ValueError:
                        print("Enter a number")
                        time.sleep(1)
                        player_menu(name)
                  if (missed < 0 or missed > val):
                        print("Enter a value greater than 0 or less than shots hit")
                        time.sleep(1)
                        player_menu(name)
                  else:
                        df.loc[df.Name == name, 'Misses'] += missed
                        df.loc[df.Name == name, 'Accuracy%'] = 100-((df.loc[df.Name == name, 'Misses'] / df.loc[df.Name == name, 'Hits']) * 100)
                        df.to_csv('PuttingStats.csv', index=False)

      else:
            print("Try again")
            time.sleep(1)
            player_menu(name)

      player_menu(name)


def main_menu():
      print("\n" * 100)
      df = pd.read_csv("PuttingStats.csv")
      print("----------Putting Rankings----------")
      print(df)
      print("1 for free play")
      print("2 to create the holes")
      print("3 to view the holes")
      print("4 to create new competition")
      print("5 to view competition results")

      check = input()
      if (check == "1"):
            add_player(check)

      elif(check == "2"):
            create_hole()

      elif(check == "3"):
            view_holes()

      elif(check == "4"):
            new_competition()

      elif(check == "5"):
            view_compeitions()
      else:
            main_menu()


def add_player(name):
      print("\n" * 100)
      df = pd.read_csv("PuttingStats.csv")

      name = input("Please enter your name!\n")

      if name not in df.values:
            new_entry = {'Name': name, 'Hits': 0, 'Misses': 0}
            check = input("Do you want to add {}?\n".format(name))
            if check == "y" or check == "Y" or check == "Yes" or check == "yes":
                  df = df.append(new_entry, ignore_index=True)
                  df.to_csv('PuttingStats.csv', index=False)
                  player_menu(name)
            else:
                  add_player()
      else:
            player_menu(name)


def view_holes():
      df = pd.read_csv("Holes.csv")
      print("----------Holes----------")
      print(df)
      print("Enter 1 to add a new hole")
      print("Enter 2 for main menu")
      check = input()
      if(check == "1"):
            create_hole()
      elif(check == "2"):
            main_menu()
      else:
            print("Invalid input")
            time.sleep(1)
            view_holes()


def create_hole():
      df = pd.read_csv("Holes.csv")
      print("Enter 'c' or 'cancel' at any time to stop the creation process")
      hole_name = input("Enter name of the hole ")
      check = input("Is -- {} -- correct? ".format(hole_name))
      if check == "y" or check == "Y" or check == "Yes" or check == "yes":
            hole_distance = input("Enter the distance of the hole in cm ")
            try:
                  hole_distance = int(hole_distance)
            except ValueError:
                  print("Enter a number")
                  time.sleep(1)
                  create_hole()
            check = input("Is -- {} -- correct? ".format(hole_distance))
            if check == "y" or check == "Y" or check == "Yes" or check == "yes":
                  hole_par = input("What is par for this hole? ")
                  try:
                        hole_par = int(hole_par)
                  except ValueError:
                        print("Enter a number")
                        time.sleep(1)
                        create_hole()
                  check = input("Is -- {} -- correct? ".format(hole_par))
                  if check == "y" or check == "Y" or check == "Yes" or check == "yes":
                        new_entry = {'Hole Name': hole_name, 'Distance': hole_distance, 'Par': hole_par}
                        df = df.append(new_entry, ignore_index=True)
                        df.to_csv('Holes.csv', index=False)
                        view_holes()

                  elif (check == "c" or check == "C" or check == "cancel" or check == "Cancel"):
                        view_holes()

                  else:
                        print("Restarting")
                        time.sleep(1)
                        create_hole()

            elif (check == "c" or check == "C" or check == "cancel" or check == "Cancel"):
                  view_holes()

            else:
                  print("Restarting")
                  time.sleep(1)
                  create_hole()

      elif(check == "c" or check == "C" or check == "cancel" or check == "Cancel"):
            view_holes()

      else:
            print("Restarting")
            time.sleep(1)
            create_hole()


def new_competition():
      df_holes = pd.read_csv("Holes.csv")
      comp_name = input("Enter competition name: ")
      player_count = input("How many players? ")
      try:
            player_count = int(player_count)
      except ValueError:
            print("Enter a number")
            time.sleep(1)
            new_competition()
      check = input("Is -- {} -- correct? ".format(player_count))
      if check == "y" or check == "Y" or check == "Yes" or check == "yes":
            lst = [None] * player_count
            for i in range(player_count):
                  lst[i] = input("Player {}'s name: ".format(i+1))

            num_holes = input("How many holes? ")
            try:
                  num_holes = int(num_holes)
            except ValueError:
                  print("Enter a number")
                  time.sleep(1)
                  new_competition()

            df_submit = pd.DataFrame(columns=['Player', 'Strokes', 'Hole Name', 'Par'])
            df = df_submit.append(df_submit, ignore_index=True)
            df.to_csv('{}.csv'.format(comp_name), index=False)
            for n in range(num_holes):
                  print(df_holes)
                  pick_hole = input("Pick hole {} name ".format(n+1))
                  if pick_hole in df_holes.values:
                        print("\n" * 100)
                        print(df_holes[(df_holes == pick_hole).any(axis=1)])
                        for p in lst:
                              print("\n" * 100)
                              print("Hole {}".format(n+1))
                              entry = input("{}'s score: ".format(p))
                              try:
                                    entry = int(entry)
                              except ValueError:
                                    print("Enter a number")
                                    time.sleep(1)
                                    new_competition()

                              new_entry = {'Player': p, 'Strokes': entry, 'Hole Name': pick_hole, 'Par': df_holes.loc[df_holes['Hole Name'] == pick_hole, 'Par'].values}
                              df = df.append(new_entry, ignore_index=True)
                              df.to_csv('{}.csv'.format(comp_name), index=False)


                  else:
                        print("Restarting")
                        time.sleep(1)
                        new_competition()

            print("\n" * 100)
            print("COMPETITION COMPLETE")
            df_display = pd.read_csv("{}.csv".format(comp_name))
            print(df_display)
            print("Enter to get back to main menu")
            check = input(" ")
            main_menu()





      else:
            print("Restarting")
            time.sleep(1)
            new_competition()


def view_compeitions():
      print("Enter competition name")
      entry = input(" ")
      find = pd.read_csv("{}.csv".format(entry))
      print(find)

      print("Enter to get back to main menu")
      check = input(" ")
      main_menu()



main_menu()









