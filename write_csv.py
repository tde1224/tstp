"""
Take items in list of list and write them to CSV file
"""
import csv

my_list = [["Top Gun", "Risky Business", "Minority Report"],
           ["Titanic", "The Revenant", "Inception"],
           ["Training Day", "Man on Fire", "Flight"]]

with open("list.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(my_list[0])
    w.writerow(my_list[1])
    w.writerow(my_list[2])
