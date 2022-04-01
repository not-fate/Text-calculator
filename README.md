# Text-calculator
Реализация строкового текстового калькулятора, работающего с числами в диапазоне [-99, 99]. Программа может работать с приоритетом операций (включая скобки).  Использованы методы польской нотации. 

Задача для второго задания Практикума по программированию. Общая тема задания «текстовый калькулятор».

Базовая часть:
Написать калькулятор для строковых выражений вида '<число> <операция> <число>', где <число> - не отрицательное целое число меньшее 100, записанное словами, например "тридцать четыре", <арифмитическая операция> - одна из операций "плюс", "минус", "умножить". Результат выполнения операции вернуть в виде текстового представления числа. Пример calc("двадцать пять плюс тринадцать") -> "тридцать восемь"
Оформить калькулятор в виде функции, которая принимает на вход строку и возвращает строку.

Реализованы следующие подзадачи:
    3) Реализовать текстовый калькулятор для выражения из произвольного количества операций с учетом приоритета операций. Пример: calc("пять плюс два умножить на три минус один") -> "десять". (Для реализации рекомендуется использовать алгоритмы основанные на польской инверсной записи см. например, https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D1%8C ). Сложность 3
    4) Расширение задания 3. Добавить поддержку приоритета операций с помощью скобок. Пример: calc("скобка открывается пять плюс два скобка закрывается умножить на три минус один") -> "двадцать". Сложность 3
    5) Добавить возможность использования отрицательных чисел. Пример: calc("пять минус минус один") -> "шесть". Сложность 1