# corrected-evolutionary-dating
Script for correcting evolutionary time



## Example

A specific example is used to implement the correction process of ***Jasminum sambaca*** to obtain the correction coefficients for each step

~~~bash
python correct_time_coefficient.py Oleaceae-demo.csv
~~~

**Enter the parameters：**

~~~bash
# First correction
# For the slowest evolving V. vinifera in the ECH event, the Ks between homologous genes generated by the ECH event within the Oleaceae genome had the same value as the slowest evolving V. vinifera

Please enter the species with the lowest Ks value:[spec/end]Vvi
Please enter the lowest Ks value[ks_value/no]:no

# Second Correction
# Correction of the divergence of V. vinifera from C. humblotiana and Oleaceae plants genome

Please enter the species with the lowest Ks value:[spec/end]Vvi_
Please enter the lowest Ks value[ks_value/no]:no

# Third Correction
# Correction of the divergence of C. humblotiana from Oleaceae plants genome

Please enter the species with the lowest Ks value:[spec/end]Chu_
Please enter the lowest Ks value[ks_value/no]:no

# Fourth correction
# Correction OCH event within the of Oleaceae genome  had the same value as the slowest evolving F. pennsylvanica

Please enter the species with the lowest Ks value:[spec/end]Fpe
Please enter the lowest Ks value[ks_value/no]:no

~~~

### Result

~~~bash
spec/div        after_ks
Fpe     [0.1662402641603776]
Oeu     [0.22972898422449428]
Sob     [0.19825451545172237]
Jsa_Sob 0.2763209588082471
Jsa_Fpe 0.2646748225824783
Jsa_Oeu 0.2679213639411253
Sob_Fpe 0.15874294636269265
Sob_Oeu 0.18281014248626107
Fpe_Oeu 0.15653694619870306
spec/div        coefficient
Vvi     [1.0, 1]
Chu     [0.8179723502304147, 0.8519505821652364, 1]
Jsa     [0.7853982300884955, 0.8633307001433699, 0.996697027460012, 0.8054089010114501]
Fpe     [0.7128514056224899, 0.9802633554383491, 1.0, 1.0]
Oeu     [0.9033078880407124, 1.0, 0.9491614998837723, 0.9284179936451389]
Sob     [0.8499600957701516, 0.8898584255282542, 0.9948782182161946, 0.9964884300341601]
Vvi_Jsa [0.8926991150442478, 0.9316653500716849]
Vvi_Chu [0.9089861751152073, 0.9259752910826182]
Vvi_Sob [0.9249800478850758, 0.9449292127641271]
Vvi_Fpe [0.856425702811245, 0.9901316777191745]
Vvi_Oeu [0.9516539440203562, 1.0]
Chu_Jsa [0.8016852901594551, 0.8576406411543032, 0.998348513730006]
Chu_Sob [0.8339662230002831, 0.8709045038467453, 0.9974391091080973]
Chu_Fpe [0.7654118779264523, 0.9161069688017928, 1.0]
Chu_Oeu [0.8606401191355635, 0.9259752910826182, 0.9745807499418861]
Jsa_Sob [0.8176791629293236, 0.876594562835812, 0.9957876228381033, 0.9009486655228052]
Jsa_Fpe [0.7491248178554928, 0.9217970277908595, 0.998348513730006, 0.9027044505057251]
Jsa_Oeu [0.844353059064604, 0.9316653500716849, 0.9729292636718921, 0.8669134473282945]
Sob_Fpe [0.7814057506963208, 0.9350608904833017, 0.9974391091080973, 0.99824421501708]
Sob_Oeu [0.876633991905432, 0.9449292127641271, 0.9720198590499834, 0.9624532118396495]
Fpe_Oeu [0.8080796468316012, 0.9901316777191745, 0.9745807499418861, 0.9642089968225694]

# Jasminum sambac Correction coefficients after four corrections

Jsa     [0.7853982300884955, 0.8633307001433699, 0.996697027460012, 0.8054089010114501]

# The cumulative correction factor for each event
ECH:  0.7853982300884955
OCH:  0.7853982300884955*0.8633307001433699*0.996697027460012*0.8054089010114501
~~~

