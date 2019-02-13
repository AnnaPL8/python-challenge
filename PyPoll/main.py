#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:31:18 2019

@author: user
"""
import pandas as pd
df = pd.read_csv("Resources/election_data.csv")
print(df.head())

size = df.shape

rows = size[0]

print(rows)

# A complete list of candidates who received votes

received_votes = df["Candidate"].unique()

print(received_votes)

#The percentage of votes each candidate won
# First, how many votes each candidate got

khan_votes = sum(df["Candidate"] =="Khan")
print(khan_votes)

correy_votes = sum(df["Candidate"] == "Correy")
print(correy_votes)   

li_votes = sum(df["Candidate"] == "Li")
print(li_votes) 

otooley_votes = sum(df["Candidate"] == "O'Tooley") 
print(otooley_votes) 

 #The percentage of votes each candidate won 
 
khan_perct = (khan_votes/rows)*100
print(khan_perct)               

correy_perct = (correy_votes/rows)*100
print(correy_perct)

li_perct = (li_votes/rows)*100
print(li_perct) 

otooley_perct = (otooley_votes/rows)*100
print(otooley_perct) 

# The winner of the election based on popular vote. 

winner = max([khan_perct, correy_perct, li_perct, otooley_perct])

#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
##Winner: Khan
#-------------------------

print("Election Results")
print("-------------------------")
print("Total votes:", rows)
print("-------------------------")
print("Khan:" ,khan_perct, "(",khan_votes,")")
print("Khan:" ,correy_perct, "(",correy_votes,")")
print("Khan:" ,li_perct, "(",li_votes,")")
print("Khan:" ,otooley_perct, "(",otooley_votes,")")
print("-------------------------")
print("winner:khan")
print("-------------------------")

