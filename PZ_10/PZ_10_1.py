#В магазинах имеются следующие товары. Магнит - молоко, соль, сахар.
#Пятерочка - мясо, молоко, сыр. Перекресток - молоко, творог, сыр, сахар. Определить:
#1. Полный список товаров.
#2. В каких магазинах можно приобрести одновременно молоко сыр.
#3. В каких магазинах можно приобрести сахар.
magnit = { 'молоко', 'соль', 'сахар' }
pyterochka = {'мясо', 'молоко', 'сыр'}
perekrectok = {'молоко', 'творог', 'сыр', 'сахар'}
print('продукты :', magnit|pyterochka|perekrectok)
def allproduckt():
    print('продукты :', magnit | pyterochka | perekrectok)

def molokocheese():
    moloko = "молоко"
    cheese = "сыр"

    if moloko and cheese in magnit&pyterochka&perekrectok:
        print("можно купить в магните, пятёрочке, перекрёстке")
    else:
        print("Нельзя купить одновременно в трёх магазинах")

    if moloko and cheese in magnit&pyterochka:
        print("можно купить в магните, пятёрочке, перекрёстке")
    else:
        print("Нельзя купить одновременно в магните, пятёрочке")

    if moloko and cheese in magnit&perekrectok:
        print("можно купить в магните, перекрёстке")
    else:
        print("Нельзя купить одновременно в магните, перекрёстке")

    if moloko and cheese in pyterochka&perekrectok:
        print("можно купить в пятёрочке, перекрёстке")
    else:
        print("Нельзя купить одновременно в пятёрочке, перекрёстке")
print(molokocheese())

def solt():
    solt = "соль"

    if solt in magnit:
        print("соль можно купить в магните")
    else:
        print("нельзя купить соль в магните")

    if solt in pyterochka:
        print("соль можно купить в пятёрочке")
    else:
        print("нельзя купить соль в пятёрочке")

    if solt in perekrectok:
        print("соль можно купить в перекрёстке")
    else:
        print("нельзя купить соль в перекрёстке")
print(solt())

