import numpy as np

#Standartabweichung 
list = [95,      
95,
95,
72,
72,
71,
71,
71,
71,
71,
73,
73,
80,
80,
80,
75,
75,
98,
98,
98,
87,
87,
80,
80,
73,
73,
80,
80,
81,
81,
70,
70,
70,
71,
81,
72,
73,
71,
71,
71,
83,
83,
70,
70,
72,
72,
76,
76,
72,
75,
75,
74,
76,
76,
71,
71,
70,
73,
71,
71,
73,
73,
74,
84,
84,
80,
80,
80,
77,
77,
77,
78,
81,
81,
73,
73,
73,
69,
72,
72,
72,
74,
75,
75,
86,
76,
71,
71,
71,
74,
75,
79,
79,
72,
72,
78,
68,
68,
67,
71,
73,
73,
73,
75,
76,
78,
78,
74,
75,
78,
78,
74,
74,
74,
72,
86,
86,
73,
78,
78,
94,
94,
78,
78,
80,
76,
77,
77,
77,
78,
97,
97,
97,
78,
78,
79,
74,
74,
84,
84,
78,
78,
77,
76,
92,
92,
87,
87,
76,
84,
84,
76,
76,
76,
76,
76,
81,
86,
86,
86,
75,
75,
89,
84,
87,
74,
82,
82,
82,
]


st_dev = np.std(list)

print("Standartabweichung: " + str(st_dev))

#print(st_dev) st_dev ist standartabweichung

if st_dev == 0:
  print("Die Wahrscheinlichkeit, dass Sie die Wahrheit sagen liegt bei 99,9%")
if st_dev > 0 and st_dev < 1:
  print("Die Wahrscheinlichkeit, dass Sie die Wahrheit sagen liegt bei 31,8%")
if st_dev > 1 and st_dev < 2:
  print("Die Wahrscheinlichkeit, dass Sie die Wahrheit sagen liegt bei 4,6%")
if st_dev > 2 and st_dev < 3:
  print("Die Wahrscheinlichkeit, dass Sie die Wahrheit sagen liegt bei 0,4%")
if st_dev > 3 and st_dev < 4:
  print("Die Wahrscheinlichkeit, dass Sie die Wahrheit sagen liegt bei 0,2%")
if st_dev > 4 and st_dev < 5:
  print("Die Wahrscheinlichkeit, dass Sie die Wahrheit sagen liegt bei 	0,006%")
if st_dev > 5 and st_dev < 6:
  print("Die Wahrscheinlichkeit, dass Sie die Wahrheit sagen liegt bei 0,00006%")
if st_dev > 6 and st_dev < 7:
  print("Die Wahrscheinlichkeit, dass Sie die Wahrheit sagen liegt bei 	0,0000002%")
