#!/usr/bin/env python

############################################
############################################
############################################
##########                        ##########
##########   LaTeX Table Creater  ##########
##########                        ##########
##########     Max Rossmannek     ##########
##########   Zürich, 30/07/2016   ##########
##########       Version 0.1      ##########
##########                        ##########
############################################
############################################
############################################

# Last edited: 30/07/2016

title='''\
   __      _____    __  __  _____      _     _          ___               _             
  / /  __ /__   \___\ \/ / /__   \__ _| |__ | | ___    / __\ __ ___  __ _| |_ ___  _ __ 
 / /  / _` |/ /\/ _ \\\  /    / /\/ _` | '_ \| |/ _ \  / / | '__/ _ \/ _` | __/ _ \| '__|
/ /__| (_| / / |  __//  \   / / | (_| | |_) | |  __/ / /__| | |  __/ (_| | || (_) | |   
\____/\__,_\/   \___/_/\_\  \/   \__,_|_.__/|_|\___| \____/_|  \___|\__,_|\__\___/|_|   
                                                                                        
'''

usage='''\


Welcome to the LaTeX Table Creator!


You will be able to create highly customizable
LaTeX tables from your raw data files. This will
save you a lot of typing time and produce equal
results throughout your whole work.

During the process you will have to provide your
raw data in an acceptable file format and will be
given a number of different choices to style and 
customize your tables accordingly.

I hope you enjoy this program. Please notify me
on any problems or bugs and do not hesitate to
make suggestions on new features you would like
to see in this program.


Happy TeXing!

 - M

'''



import sys,os
import numpy as np


# introduction
print(title)
print(usage)

# read in raw data
raw = input('Please submit your raw data: \n')
user_file = open(raw,'r')
rows=0
cols=0
for line in user_file:
  rows=rows+1
  cols=len(line.split(' '))
data=np.empty((rows,cols),dtype=object)
user_file = open(raw,'r')
row_current=0
for line in user_file:
  data[row_current]=line.split(' ')
  row_current=row_current+1
user_file.close()

# check for user config file
config = input('Please provide the name of your CONFIG file or press ENTER \n')

if (config!=""):
  configs=["" for x in range(7)]
  config_current=0
  config_file = open(config,'r')
  for line in config_file:
    configs[config_current]=line
    config_current=config_current+1
  config_file.close()
  caption = configs[0]
  center = configs[1]
  align = configs[2]
  header = configs[3]
  col1_align = configs[4]
  horizs = configs[5]
  vertics = configs[6]
else:
  # get user specific customization
  caption = input('Please provide the optional caption of the table below: [Skip with ENTER] \n')
  center = input('Would you like the table to be centered? [y/n] \n')
  align = input('How shall the table content by aligned? [l/c/r] \n')
  header = input('Do you have a header row? [y/n] \n')
  col1_align = input('How shall the first column be aligned? [l/c/r] [ENTER=same] \n')
  horizs = input('Would you like to have horizontal bars in your table? [y/n] \n')
  vertics = input('Would you like to have vertical bars in your table? [y/n] \n')

# definitions
lines=['\\toprule \n','\\midrule \n','\\bottomrule \n']
finish = '''\
'''

# piece it together
print("Writing table into table.tex ...\n")
tbl = open('table.tex','w')

if (center=='y'):
  tbl.write('\\begin{center} \n')
  finish+='\\end{center} \n'
else:
  pass


tbl.write('\\begin{table} \n')
finish='\\end{table} \n'+finish


if (center=='y'):
  tbl.write('\\centering \n')
else:
  pass


if (caption!=""):
  tbl.write('\\caption{'+caption+'} \n')
else:
  pass


if (vertics=='y'):
  align='|'+align
  del lines
  lines=['\\hline \n','\\hline \n','\\hline \n']
else:
  pass

if (col1_align==''):
  col1_align=align


tbl.write('\\begin{tabular}{'+col1_align+align*(cols-1)+'{frame}'.format(frame='|' if vertics=='y' else '')+'} \n')
finish='\\end{tabular} \n'+finish

tbl.write(lines[0])

if (header=='y'):
  tbl.write('\\textbf{')
  tbl.write(''.join(str(data[0,k])+'} & \\textbf{' for k in range(cols-1))+str(data[0,cols-1])+'} \\\\ \n')
  rows=rows-1
else:
  pass

if (horizs=='y'):
  tbl.write(lines[1])
else:
  if (header=='y'):
    tbl.write(lines[1])
  else:
    pass

for i in range(rows):
  if (header=='y'):
    x=i+1
  else:
    x=i
  tbl.write(''.join(str(data[x,j])+' & ' for j in range(cols-1))+str(data[x,cols-1])+' \\\\ \n')
  if (horizs=='y'):
    if (i==(rows-1)):
      pass
    else:
      tbl.write(lines[1])
  else:
    pass

tbl.write(lines[2])
tbl.write(finish)

print("Saving table.tex\n")
tbl.close()

print("Done!\n")
print("To compile your newly created table run  make -f make_table.mk \n")

