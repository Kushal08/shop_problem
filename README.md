csv package is used to read csv files
### How to run the program.

Sample Data File data.csv
```
1, 4.00, teddy_bear
1, 8.00, baby_powder
2, 5.00, teddy_bear
2, 6.50, baby_powder
3, 4.00, pampers_diapers
3, 8.00, johnson_wipes
4, 5.00, johnson_wipes
4, 2.50, cotton_buds
5, 4.00, bath_towel
5, 8.00, scissor
6, 5.00, scissor
6, 6.00, bath_towel, cotton_balls, powder_puff
```

Some examples

1) Program Input:
```
$>python shopper.py data.csv teddy_bear baby_powder
```
Expected Output:
```
=> 2, 11.5
```

2) Program Input:
```
$>python shopper.py data.csv pampers_diapers baby_soap
```
Expected Output:
```
=> none
```

3) Program Input:
```
$>python shopper.py data.csv scissor bath_towel
```
Expected Output:
```
=> 6, 11.0
```
