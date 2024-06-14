Проведено дослыдження двох алгоритмів:
* жадібний алгоритм (find_coins_greedy)
* динамічне програграмування (find_min_coins)

Результати дослідження:  
```
***** find_coins_greedy *****
case for cash:  113
Result:  {50: 2, 10: 1, 2: 1, 1: 1}
Time taken: 0.008570028003305197
case for cash:  137
Result:  {50: 2, 25: 1, 10: 1, 2: 1}
Time taken: 0.007605836988659576
case for cash:  75
Result:  {50: 1, 25: 1}
Time taken: 0.0041089929873123765
case for cash:  38
Result:  {25: 1, 10: 1, 2: 1, 1: 1}
Time taken: 0.0074957179895136505
case for cash:  12
Result:  {10: 1, 2: 1}
Time taken: 0.0054430180171038955
case for cash:  65345
Result:  {50: 1306, 25: 1, 10: 2}
Time taken: 0.00583662700955756
case for cash:  543210
Result:  {50: 10864, 10: 1}
Time taken: 0.004716766008641571

***** find_min_coins *****
case for cash:  113
Result:  {50: 2, 10: 1, 2: 1, 1: 1}
Time taken: 0.4022088109923061
case for cash:  137
Result:  {50: 2, 25: 1, 10: 1, 2: 1}
Time taken: 0.5081989769823849
case for cash:  75
Result:  {50: 1, 25: 1}
Time taken: 0.26323807999142446
case for cash:  38
Result:  {25: 1, 10: 1, 2: 1, 1: 1}
Time taken: 0.1275053930003196
case for cash:  12
Result:  {10: 1, 2: 1}
Time taken: 0.0438014269748237
case for cash:  65345
Result:  {50: 1306, 25: 1, 10: 2}
Time taken: 410.7702622450015
case for cash:  543210
undefined
```

Як ми бачимо жадібний алгоритм працює приблизно однаково швидко з ростом вхідних даних. 
Динамічне програмування стабільно працює на невеликих даних: але коли данні стають завеликі то такий алгоритм перестає 
ефективно виконуватись за розумний час.
