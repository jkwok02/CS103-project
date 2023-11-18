#!/usr/bin/env python
# coding: utf-8

# # Project Milestone Template

# ### Step 1a: Planning 
# #### Identify the information in the file your program will read
# 
# Describe (all) the information that is available. Be sure to note any surprising or unusual features. (For example, some information sources have missing data, which may be blank or flagged using values like -99, NaN, or something else.)

# <font color="blue">
#     
# Put your answer here. Please don't delete the two HTML tags on either end of this paragraph. It's to make your answer blue so the TAs can easily spot it.
# 
# </font>

# ### Step 1b: Planning 
# #### Brainstorm ideas for what your program will produce
# #### Select the idea you will build on for subsequent steps
# 
# You must brainstorm at least three ideas for graphs or charts that your program could produce and choose the one that you'd like to work on. You can choose between a line chart, histogram, bar chart, scatterplot, or pie chart.
# 
# If you would like to change your project idea from what was described in the proposal, you will need to get permission from your project TA. This is intended to help ensure that your new project idea will meet the requirements of the project. Please see the project proposal for things to be aware of when communicating with your project TA.

# <font color="blue">
#     
# Put your answer here. Please don't delete the two HTML tags on either end of this paragraph. It's to make your answer blue so the TAs can easily spot it.
# 
# </font>

# ### Step 1c: Planning 
# #### Write or draw examples of what your program will produce
# 
# You must include a **hand-drawn image** that shows what your chart or plot will look like. You can insert an image using Edit -> Insert Image.

# Insert your image into this cell.

# ### Step 2a: Building
# #### Document which information you will represent in your data definitions
# 
# Before you design data definitions in the code cell below, you must explicitly document here which information in the file you chose to represent and why that information is crucial to the chart or graph that you'll produce when you complete step 2c.

# <font color="blue">
#     
# Put your answer here. Please don't delete the two HTML tags on either end of this paragraph. It's to make your answer blue so the TAs can easily spot it.
# 
# </font>

# #### Design the data definitions

# In[ ]:


from cs103 import *
import csv
from typing import NamedTuple, List


# In[ ]:


##################
# Data Definitions

Consumed = ...



# List[Consumed]
# interp. a list of Consumed

LOC0 = []

@typecheck
def fn_for_loc(loc: List[Consumed]) -> ...:
    ... # choose which template body to use for List[Consumed]


# ### Step 2b: Building
# #### Design a function to read the information and store it as data in your program
# 
# Complete this step in the code cell below. Your `read` function should remove any row with invalid or missing data but otherwise keep all the data. I.e., you should **not** design the `read` function such that it only returns the data you need for step 2c.
# 
# You can choose to continue to build on this file when completing the final submission for the project (as opposed to copying your code over to the `project_final_submission_template.ipynb` file). However, if this is the approach you are taking, please go to the `project_final_submission_template.ipynb` file and read through the "Step 2b and 2c: Building" section. This section contains crucial information about common issues students encounter. We expect that you will be familiar with this information.

# In[ ]:


###########
# Functions

@typecheck
def read(filename: str) -> List[Consumed]:
    """    
    reads information from the specified file and returns ...
    """
    #return []  #stub
    # Template from HtDAP
    # loc contains the result so far
    loc = [] # type: List[Consumed]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            # you may not need to store all the rows, and you may need
            # to convert some of the strings to other types
            c = Consumed(row[0], ... ,row[n])
            loc.append(c)
    
    return loc


# Begin testing
start_testing()

# Examples and tests for read
expect(..., ...)

# show testing summary
summary()


# In[ ]:


# Be sure to select ALL THE FILES YOU NEED (including csv's) 
# when you submit. Also, UNLIKE USUAL, YOU CAN EDIT THIS CELL!
# That's in case you want to switch the ASSIGNMENT code for the final
# submission. Run this cell to start the submission process.
from cs103 import submit

COURSE = 123409
ASSIGNMENT = 1615245
#ASSIGNMENT = 1615244 # UNCOMMENT for final submission and COMMENT line above

submit(COURSE, ASSIGNMENT)

# If your submission fails, SUBMIT by downloading your files and uploading them to 
# Canvas. You can learn how on the page "How to submit your Jupyter notebook" on 
# our Canvas site.


# # Please double check your submission on Canvas to ensure that the right files (Jupyter file + CSVs) have been submitted and that the files do not contain unexpected errors.
# 
# <font color="red">**You should always check your submission on Canvas. It is your responsibility to ensure that the correct file has been submitted for grading.**</font> Regrade or accomodation requests using reasoning such as "I didn't realize I submitted the wrong file"/"I didn't realize the submission didn't work"/"I didn't realize I didn't save before submitting so some of my work is missing" will not be considered.
