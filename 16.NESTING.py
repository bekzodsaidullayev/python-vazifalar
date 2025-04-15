#NESTING

buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
            'tyil':810,
            'vyil':870,
            'tjoy':'Buxoro'
            }
jaskson = {'ism':'Michael Jackson',
            'tyil':1958,
            'vyil':2009,
            'tjoy':"Amerika"
            }
navoiy = {'ism':'Alisher Navoiy',
          'tyil':1441,
          'vyil':1501,
          'tjoy':"Xirot"
          }
toti = {'ism':'Toti Yusupova',
        'tyil':1936,
        'vyil':2022,
        'tjoy':"Samarqand"
        }
insonlar = ['buxoriy','jaskson','navoiy','toti']
for inson in insonlar:
    ism = inson['ism']
    tyil = inson['tyil']
    tjoy = inson['tjoy']
    print(f"{ism} {tyil}-da {tjoy}da tug'ilganlar.")

insonlar = ['buxoriy','jaskson','navoiy','toti']
for inson in insonlar:
    print(f"{inson['ism']} ning tavallud ayyomlari {inson[tyil]}")



buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
            'tyil':810,
            'vyil':870,
            'tjoy':'Buxoro',
            'asarlari':['Adab durdonalari','Ishonchli hadislar to\'plami']
            }
jaskson = {'ism':'Michael Jackson',
            'tyil':1958,
            'vyil':2009,
            'tjoy':"Amerika",
            'asarlari':['25 Miles','Invincible','Thriller']
            }
navoiy = {'ism':'Alisher Navoiy',
          'tyil':1441,
          'vyil':1501,
          'tjoy':"Xirot",
          'asarlari':['Xamsa','Devoni Foniy']
          }
toti = {'ism':'Toti Yusupova',
        'tyil':1936,
        'vyil':2022,
        'tjoy':"Samarqand",
        'asarlari':['Nazira','Dilxiroj','Yangi boy']
        }

insonlar = ['buxoriy','jaskson','navoiy','toti']
for inson in insonlar:
    print(f"{inson['ism']} ning tavallud ayyomlari {inson['tyil']}")
    for asar in inson['asarlar']:
        print(f"{asar}")


davlatlar = {"O'zbekiston":{'millati':"o'zbek",
                            'maydoni':'448978 km2',
                            'axoli_s':'37.543 mln'
                            },
              "Qozog'iston":{'millati':"qozoq",
                            'maydoni':'2742902 km2',
                            'axoli_s':'19.967 mln'
                            },
              "Turkmaniston":{'millati':"o'zbek",
                            'maydoni':'448.1 km2',
                            'axoli_s':'7 mln'
                            }
              }

for k, q in davlatlar.items():
    print(f"{k} ning millati {q['millati']}. Aholi soni {q['axoli_s']} ga teng. Maydoni {q['maydoni']}." )


davlatlar = {"O'zbekiston":{'millati':"o'zbek",
                            'maydoni':'448978 km2',
                            'axoli_s':'37.543 mln'
                            },
              "Qozog'iston":{'millati':"qozoq",
                            'maydoni':'2742902 km2',
                            'axoli_s':'19.967 mln'
                            },
              "Turkmaniston":{'millati':"o'zbek",
                            'maydoni':'448.1 km2',
                            'axoli_s':'7 mln'
                            }
              }
davlat = input("Istalgan davlatingizni kiriting: ")
if davlat in davlatlar:
    info=davlatlar[davlat]
    print(f"{davlat.title()}ning maydoni {info['maydoni']}")
else:
    print("Bizda bunday davlat haqida ma'lumot yo'q.")