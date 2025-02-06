# Tapşırıq:
# İstifadəçidən yaşını daxil etməsini istəyin və aşağıdakı qaydalara əsasən ona mesaj verin:

# 0-12 yaş: "Uşaqsan"
# 13-19 yaş: "Gəncsən"
# 20-64 yaş: "Böyüksən"
# 65 və yuxarı: "Yaşlısan"

try:
    yas = int(input("Yasinizi daxil edin: "))

    if yas <=12:
        print("Uşaqsan")
    elif yas >=13 and yas <= 19:
        print("Gəncsən")
    elif yas >=20 and yas <=64: 
        print("Böyüksən")
    elif yas >=65 and yas <=100:
        print("Yaşlısan")
    elif yas >=100:
        print("Allah ömür versin, neçədən sonra saymağın başını buraxacaqsan?")
    else:
        pass
except ValueError:
    print("Reqem daxil edin")