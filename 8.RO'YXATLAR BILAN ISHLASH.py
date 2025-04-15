# RO'YXATLAR BILAN ISHLASH

davlatlar = ['O\'zbekiston','Germaniya','Kanada','Turkiya']
print(davlatlar)

davlatlar = ['O\'zbekiston','Germaniya','Kanada','Turkiya']
print(len(davlatlar))

davlatlar = ['O\'zbekiston','Germaniya','Kanada','Turkiya']
print("Tartiblangan ro'yhat: ",sorted(davlatlar))
print("Asl ro'yhat: ",davlatlar)

davlatlar = ['O\'zbekiston','Germaniya','Kanada','Turkiya']
print("Tartiblangan va aylantirilgan ro'yhat: ",sorted(davlatlar, reverse=True))
print("Asl ro'yhat: ",davlatlar)

davlatlar = ['O\'zbekiston','Germaniya','Kanada','Turkiya']
davlatlar.reverse()
print(davlatlar)

davlatlar = ['O\'zbekiston','Germaniya','Kanada','Turkiya']
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

sonlar = list(range(120,1200,2))
print(sonlar)

sonlar = list(range(120,1200,2))
print(sum(sonlar))

sonlar = list(range(120,1200))
print(max(sonlar)-min(sonlar))

sonlar = list(range(120,1200))
print(len(sonlar))

sonlar = list(range(120,1200))
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

taomlar = []
taomlar.append('norin')
taomlar.append('somsa')
taomlar.append('manti')
taomlar.append('osh')
taomlar.append('dimlama')
nonushta = taomlar[:]
print(taomlar)
print(nonushta)

nonushta = ['norin','somsa','manti','osh','dimlama']
nonushta.remove('osh')
nonushta.remove('manti')
nonushta.append('qaymoq')
nonushta.append('tuxum')
print(nonushta)

taomlar = []
taomlar.append('norin')
taomlar.append('somsa')
taomlar.append('manti')
taomlar.append('osh')
taomlar.append('dimlama')
print(taomlar)
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove('manti')
nonushta.append('qaymoq')
nonushta.append('tuxum')
print(nonushta)

taomlar = []
taomlar.append('norin')
taomlar.append('somsa')
taomlar.append('manti')
taomlar.append('osh')
taomlar.append('dimlama')
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove('manti')
nonushta.append('qaymoq')
nonushta.append('tuxum')
nonushta=tuple(nonushta)
nonushta[0]="qaymoq va non"