import os
import sys
import time
from csv import excel
import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def title():
  print("Luegendetektor von Jan Kappelmann und Philipp Weil")

excel_datei = pd.read_excel("Tabelle_Luegendetektor.xlsx")