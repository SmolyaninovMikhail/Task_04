# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
berr = list(random.randint(1, 501) for _ in range(int(input('Сколько кустов на грядке: '))))
print(berr)
if len(berr) == 1:
    print(berr[0])
elif len(berr) == 2:
    print(berr[0] + berr[1])
else:
    amount = list()
    for i in range(len(berr) - 1):
        amount.append(berr[i - 1] + berr[i] + berr[i + 1])
    amount.append(berr[i - 2] + berr[i - 1] + berr[0])
    print(max(amount))