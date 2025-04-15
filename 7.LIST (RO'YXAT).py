# LIST (RO'YXAT)
ismlar = []
ismlar.append("Asqar")
ismlar.append("Akmal")
ismlar.append("Behruz")
print(ismlar)

ismlar = ["Akmal","Alisher","Anvar"]
print("Salom ",ismlar[0],", yaxshimisan?")
print("Yaxshi yuribsanmi ",ismlar[1],", nima gap?")
print(ismlar[2],", bugun yig'ilish bormi?.")

sonlaer = [1,2,-3,5.61]

sonlar = [1,2,-3,5.61]
sonlar[0]=5
sonlar[1]=sonlar[0]+5
sonlar[-1]=sum(sonlar[0:3])
print(sonlar)

t_shaxs = ['Bobur','Alisher Navoiy','Amir Temur']
z_shaxs = ['Murod Nazarov','Anvar Nazriddinov']

t_shaxs = ['Bobur','Alisher Navoiy','Amir Temur']
z_shaxs = ['Murod Nazarov','Anvar Nazrullayev']
t_sh = t_shaxs.pop(2)
z_sh = z_shaxs.pop(1)
print('Men tarixiy shaxslardan '+ t_sh + 'ni xurmat qilaman. Ular kuchli sarkarda bo\'lganlar.')
print("Men zamonaviy shaxslardan "+ z_sh + "ni xurmat qilaman. Chunki ular sababli ko'pgina yoshlar bilimga ega bo'lmoqda.")

friends = []
friends.append("Asqar")
friends.append("Behruz")
friends.append("Akmal")
friends.append("Saidakmal")
friends.append("Mo'minaka")

friends = ['Asqar','Behruz','Akmal','Saidakmal','Mo\'minaka']
friends.remove('Saidakmal')
friends.remove('Behruz')
print(friends)

friends = ['Asqar','Behruz','Akmal','Saidakmal','Mo\'minaka']
friends.insert(0, 'Alisher')
friends.insert(-1, 'Solih')
friends.insert(3, 'Bahtiyoraka')
print(friends)

friends = ['Asqar','Behruz','Akmal','Saidakmal','Mo\'minaka']
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
print("Mening uyimga kelgan mehmonlarim: ", mehmonlar)
print("Mening uyimga kela olmagan do'stlarim': ",friends)