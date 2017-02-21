"""
Data source: Dutour Sikirić, Mathieu, Olaf Delgado-Friedrichs, and Michel Deza. “Space Fullerenes: a Computer Search for New Frank-Kasper Structures” Acta Crystallographica Section A Foundations of Crystallography 66.Pt 5 (2010): 602–615.

Cage composition:
 (12,14,15,16) = (12,10,4,2,)
"""

pairs="""
87 157
75 123
140 63
87 136
135 117
42 141
18 110
13 83
4 111
49 135
13 77
46 125
130 43
50 122
79 120
97 90
136 133
12 39
115 103
85 105
94 76
21 20
17 126
88 44
121 117
46 7
27 56
89 20
57 11
69 86
118 71
80 62
106 108
75 57
104 112
54 126
6 152
148 154
99 83
33 144
80 94
39 89
51 61
60 55
36 40
91 153
38 9
30 132
120 90
53 55
142 100
140 52
104 152
30 148
37 157
87 145
4 134
75 92
108 111
92 66
140 83
57 20
44 58
126 137
152 48
148 39
30 31
48 29
9 118
90 101
105 24
8 16
63 36
152 118
6 108
12 54
135 58
82 153
22 24
98 94
47 85
3 99
129 141
74 45
121 9
129 35
123 119
30 7
14 62
74 96
125 150
130 31
47 32
43 143
101 68
145 155
103 70
40 84
1 102
137 71
124 51
129 23
61 32
138 79
72 70
146 58
52 116
51 117
121 47
13 45
20 154
34 90
64 10
69 133
98 105
14 147
16 147
124 144
132 91
123 23
146 35
97 107
114 81
46 136
6 33
102 55
139 118
8 68
45 109
3 19
110 155
82 124
12 71
49 113
28 108
18 41
78 129
63 66
53 146
59 34
158 157
0 36
64 105
21 112
98 32
95 155
115 34
34 114
39 139
72 22
38 127
106 70
27 40
41 151
50 133
77 65
24 2
17 127
84 138
36 149
86 137
126 19
65 122
26 153
15 159
5 123
53 156
70 2
66 99
145 127
16 158
88 54
18 134
28 77
106 134
26 52
80 16
25 149
95 102
81 113
27 158
95 38
43 50
22 8
69 151
73 101
107 79
150 128
93 76
119 100
91 111
25 84
107 72
82 139
110 35
103 26
96 19
50 37
45 3
15 130
96 56
115 91
4 47
144 83
87 147
131 120
93 100
93 99
148 153
128 58
71 151
74 65
158 138
0 10
26 29
1 9
114 131
59 68
60 2
46 151
141 37
15 109
119 66
38 137
110 55
62 19
107 122
146 132
97 103
115 156
113 116
51 113
59 111
149 116
130 141
73 109
93 62
28 68
43 92
27 5
94 10
95 11
142 42
41 67
86 96
116 112
6 82
104 64
41 48
37 79
74 133
75 88
98 8
31 67
78 155
80 56
136 109
124 52
63 122
69 143
106 48
23 44
31 35
17 44
64 149
73 42
29 154
143 67
25 81
125 145
22 138
29 112
14 142
67 154
0 65
60 134
5 11
128 127
119 40
121 128
1 85
33 10
139 117
156 81
0 56
28 72
104 1
76 61
4 150
142 23
97 140
53 49
25 24
78 157
21 49
159 3
132 150
60 85
21 102
18 125
135 89
114 61
159 54
73 147
143 57
77 33
15 7
12 7
131 100
17 14
86 11
5 78
13 101
156 2
59 32
159 92
88 89
76 144
131 84
42 120
"""

waters="""
0.08805 0.83579 0.3306
0.11463 0.21625 0.49244
0.93678 0.09296 0.78747
0.47354 0.68367 0.24486
0.30756 0.19685 0.82161
0.94406 0.58829 0.53567
0.28344 0.08658 0.17942
0.45577 0.44008 0.05772
0.22197 0.87894 0.75713
0.23963 0.27519 0.46593
0.17783 0.94124 0.36312
0.0 0.5 0.43495
0.43678 0.40705 0.21253
0.41964 0.82777 0.09163
0.4292 0.63849 0.63887
0.54424 0.55992 0.05772
0.22344 0.7625 0.69426
0.42233 0.52151 0.57426
0.08036 0.32777 0.90837
0.35163 0.64525 0.37451
0.80447 0.34673 0.33641
0.86463 0.26771 0.43136
0.06322 0.90705 0.78747
0.67783 0.55876 0.63688
0.0 0.0 0.68991
0.87647 0.96555 0.58938
0.74959 0.10716 0.12051
0.01038 0.70176 0.5301
0.21509 0.95303 0.00158
0.8867 0.19111 0.17816
0.58239 0.36205 0.00024
0.75162 0.42197 0.97005
0.37353 0.03446 0.66558
0.28385 0.97427 0.24087
0.57914 0.98705 0.82541
0.78344 0.41342 0.82058
0.9292 0.86152 0.36113
0.91964 0.67224 0.90837
0.20928 0.40019 0.50359
0.52647 0.31633 0.24486
0.88538 0.78375 0.49244
0.04864 0.33395 0.05765
0.6133 0.69111 0.82185
0.82798 0.58803 0.11513
0.57767 0.4785 0.57426
0.37379 0.71572 0.11893
0.28491 0.45303 0.99842
0.30447 0.15327 0.66359
0.04864 0.20895 0.11671
0.73963 0.22482 0.53407
0.95136 0.66605 0.05765
0.55594 0.08829 0.46433
0.71616 0.02573 0.24087
0.77656 0.2375 0.69426
0.5 0.5 0.31009
0.93328 0.27422 0.69227
0.13538 0.73229 0.43136
0.87353 0.46555 0.33442
0.5708 0.36152 0.63887
0.42086 0.01295 0.82541
0.02647 0.18367 0.75514
0.5 0.0 0.56505
0.38538 0.71625 0.50756
0.82945 0.82947 0.23706
0.07767 0.02151 0.42574
0.1133 0.8089 0.17816
0.72344 0.7375 0.30575
0.88873 0.38092 0.08676
0.32798 0.91198 0.88487
0.07914 0.51295 0.17459
0.95577 0.05992 0.94228
0.27803 0.37894 0.24288
0.04424 0.94008 0.94228
0.45136 0.70895 0.88329
0.19244 0.69685 0.17839
0.75541 0.53963 0.37252
0.44406 0.91171 0.46433
0.25041 0.89284 0.12051
0.95617 0.54724 0.69603
0.87379 0.78429 0.88107
0.26038 0.77519 0.53407
0.7446 0.03963 0.62748
0.45227 0.13382 0.21199
0.54774 0.86618 0.21199
0.85163 0.85475 0.62549
0.14837 0.14525 0.62549
0.12647 0.53446 0.33442
0.21656 0.58658 0.82058
0.62353 0.46555 0.41062
0.64837 0.35475 0.37451
0.61127 0.88092 0.91324
0.54864 0.16605 0.94236
0.72197 0.62106 0.24288
0.51038 0.79824 0.4699
0.29072 0.90019 0.49641
0.05594 0.41171 0.53567
0.19553 0.65327 0.33641
0.74838 0.92197 0.02995
0.25541 0.96037 0.62748
0.56672 0.77422 0.30773
0.63538 0.76771 0.56864
0.45136 0.83395 0.94236
0.98963 0.29824 0.5301
0.78491 0.04697 0.00158
0.0708 0.13849 0.36113
0.12353 0.03446 0.58938
0.08239 0.13795 0.99976
0.91761 0.86205 0.99976
0.25162 0.07803 0.02995
0.41761 0.63795 0.00024
0.95227 0.36618 0.78801
0.38873 0.11908 0.91324
0.91195 0.16422 0.3306
0.70928 0.09982 0.49641
0.62647 0.96555 0.66558
0.67202 0.08803 0.88487
0.82217 0.05876 0.36312
0.48963 0.20176 0.4699
0.27656 0.2625 0.30575
0.76038 0.72482 0.46593
0.69244 0.80316 0.82161
0.36463 0.23229 0.56864
0.95136 0.79105 0.11671
0.79072 0.59982 0.50359
0.54383 0.04724 0.30397
0.24959 0.39284 0.87949
0.37647 0.53446 0.41062
0.32217 0.44124 0.63688
0.41195 0.33579 0.66941
0.78385 0.52573 0.75914
0.71509 0.54697 0.99842
0.69553 0.84673 0.66359
0.54864 0.29105 0.88329
0.11127 0.61908 0.08676
0.12622 0.21572 0.88107
0.61463 0.28375 0.50756
0.24838 0.57803 0.97005
0.2446 0.46037 0.37252
0.97354 0.81633 0.75514
0.43328 0.22579 0.30773
0.71656 0.91342 0.17942
0.75041 0.60716 0.87949
0.58805 0.66422 0.66941
0.92086 0.48705 0.17459
0.45617 0.95277 0.30397
0.21616 0.47427 0.75914
0.67055 0.32947 0.76294
0.32945 0.67053 0.76294
0.62622 0.28429 0.11893
0.92233 0.9785 0.42574
0.3867 0.3089 0.82185
0.17202 0.41198 0.11513
0.17055 0.17053 0.23706
0.58036 0.17224 0.09163
0.80756 0.30316 0.17839
0.04383 0.45277 0.69603
0.77803 0.12106 0.75713
0.04774 0.63382 0.78801
0.06672 0.72579 0.69227
0.56322 0.59296 0.21253
"""

coord= "relative"

cages="""
12 0.42406 0.36787 0.44698
14 -0.31069 -0.08602 0.42468
14 0.5 0.0 0.064
16 0.0 0.0 0.17225
16 0.5 0.5 -0.17225
15 0.82306 0.23969 -0.05674
14 0.54844 0.16421 -0.29458
15 0.32306 0.26031 0.05674
12 0.92406 0.13213 -0.44698
14 0.0 0.5 -0.064
15 0.17694 0.76031 -0.05674
14 0.31069 0.08602 0.42468
12 0.07594 0.86787 -0.44698
14 0.45156 0.83579 -0.29458
15 -0.32306 -0.26031 0.05674
12 1.17531 0.31106 -0.30253
14 0.18931 0.58602 -0.42468
12 -0.31657 -0.5518 0.1732
14 0.81069 0.41398 -0.42468
14 -0.04844 -0.33579 0.29458
12 -0.67531 -0.18894 0.30253
12 -0.42406 -0.36787 0.44698
12 0.81657 -0.0518 -0.1732
12 -0.17531 0.68894 -0.30253
12 0.31657 0.5518 0.1732
12 0.18343 1.0518 -0.1732
14 0.04844 0.33579 0.29458
12 0.67531 0.18894 0.30253
"""

bondlen = 3

celltype = 'rect'

cell = """
17.918034918814932 25.85585726509846 19.94194341745186
"""

density = 0.51764847234306

