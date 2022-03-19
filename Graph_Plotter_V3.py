import pandas as pd
import matplotlib.pyplot as plt

############################################################################
'''Customize graph specifications at the bottom of the program (line 30)'''#
############################################################################

# Uses Pandas library to convert raw data excel file into a data frame
def getDataFrame(filePath: str):

    return pd.read_excel(filePath)
#########################################

# Removes ambient temperature and pressure rows
def parseData(df: pd.core.frame.DataFrame):

    if "Ambient" in df.columns[0]:

        df.columns = df.iloc[1]

        df.drop(axis=0, index=[0,1], inplace=True)
#########################################


# Function to create graph (DON'T TOUCH)
def makeGraph(filePath: str, i_var: str, d_var: list, axis_label: dict, title: str):

    data = getDataFrame(filePath)

    parseData(data)

    x = list(data[i_var])

    for DV in d_var:

        y = list(data[DV[0]])

        plt.plot(x, y, label=DV[1])


    plt.title(title)
    plt.xlabel(axis_label['x'])
    plt.ylabel(axis_label['y'])

    plt.legend()
    plt.grid(True)
    plt.show()
# END OF FUNCTION


# CREATE GRAPH SPECIFICATIONS BELOW #############################################################################################

file_path = "C:\\Users\\chdar\\OneDrive - University of Toronto\\Programming\\Python\\MIE210 Lab\\Lab 2\\Lab 2 - Part 2a Set 1.xlsx"

independent_variable = "Time(s)"

dependent_variable = [["delta_T","\u0394T"]]
#                    [[Column header, Graph label], ...]

axes_labels = {
                'x': "Time (s)",
                'y': "Temperature (K)"     # Deg C symbol = \u2103
                }

graph_title = "Temperature Drop Across the Left Tank Wall (Part 2a)"

########################################################################################
makeGraph(file_path, independent_variable, dependent_variable, axes_labels, graph_title)
########################################################################################