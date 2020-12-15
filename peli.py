from sys import exit
import random

pisteet = 0 
aikaaJaljella = 0
vaikeustaso = 0
aamutakki = True
hoonVaatteet = False
reppuMukana = False
repunSisältö = []
maski = False

#alkutilanne
def pistetilanne(muutos):
    global pisteet
    pisteet += muutos
    print(f"pisteesi on nyt {pisteet}.")
    return pisteet

def lisaaAikaa(minuuttia):
    kello = minuuttia
    print(f"Olen LisaaAikaaKello ja arvoni on {kello}")
    return kello

def aika(kello):
    global aikaaJaljella
    aikaaJaljella += kello
    onkoAikaTaysi = aikaaJaljella
    print(f"Aikaa kerhon alkuun on {aikaaJaljella} minuuttia.")
    
    if onkoAikaTaysi <= 0:
        print("Aika loppui. Kerho jäi. Lapsi itkee, well done.")
        print(f"Loppupisteesi on {pisteet}")
        exit(0)
    elif aikaaJaljella <= 60:
        print("Kiire tulee...")

    return aikaaJaljella

def valinta():
    kanasteltu = False
    while True:
        print("Tekeekö mielesi kölliä, paina 1, jos taas haluat vielä kainalokanastella, paina 2. Ei armoa, ylös, paina 3")

#        print(f"kana-arvo: {kanasteltu}")
        aamuvirkku = input("> ")
                
        if aamuvirkku == '1':
            print("Ihanaa, vielä viisi minuuttia äiti...")
            pistetilanne(1)
            aika(-5)
        elif aamuvirkku == '2':
            print('"Tuletko kulta kainalokanaseksi vielä hetkiseksi?"')
            if int(vaikeustaso) == 1 and not kanasteltu:
                print('"Juu tulen mielelläni."\n Höpöliini kömpii viereen ja aamu muuttuu vain paremmaksi')
                pistetilanne(10)
                aika(-15)
                kanasteltu = True
 #               print(f"kana-arvo: {kanasteltu}")
                input('Paina mitä tahansa jatkaaksesi.')
            elif int(vaikeustaso) == 1 and kanasteltu:    
                print('"EIEIEIEIEIEIIIII!"\n "Hyvä on noustaan ylös"\n Menette aamutoimiin')
                input('Paina mitä tahansa jatkaaksesi.')
                vessa()     
            elif int(vaikeustaso) == 2:
                print('"En tule."\n "Entä jos-"\n "EIEIEIEIEI..."\n "No mennään sitten aamutoimiin"\n "... Ja katsotaan Ryhmä Hauta"\n "Huoh, joo..."')
                pistetilanne(0)
                aika(-5)
                input('Paina mitä tahansa jatkaaksesi.')
                vessa()
            else:
                print('"EEEIEIEIEIIEIEIEIEI!!!!"\n "Ei sit-"\n "EIEIEIEIEIEIIII!!!"\n "Älä huuda! Mennään sitten aamutoimiin"\n "Eikä mennää!!!!!..."')
                print("ahhh, tästä se lähtee")
                pistetilanne(-10)
                aika(-15)
                input('Paina mitä tahansa jatkaaksesi.')
                vessa()    
        elif aamuvirkku == '3':
            if int(vaikeustaso) < 3:
                print('"Nyt noustaan"\n "Niin noustaan, aikainen lintu kerhoon löytää"\n Marssitte yhdessä kylppäriin hissun kissun.')
                pistetilanne(1)
                aika(-1)
                input('Paina mitä tahansa jatkaaksesi.')
                vessa()
            else:
                print('"Nyt noustaan"\n "Ei nousta eieieieieii"\n "Noustaan niin saat katsoa Ryhmä Hauta"\n "Haluan Pipsa Possua yääääähhh!!!!"')
                print('"Ai että", ajattelet kun hyssyttelyn ja maanittelun jälkeen saat kannettua rimpuilevan rakkaasi vessaan.')
                pistetilanne(3)
                aika(-10)
                input('Paina mitä tahansa jatkaaksesi.')
                vessa()   
        else:
            print('Valitse numero väliltä 1-3.')         

def vessa():
    global aamutakki
    global hoonVaatteet
    global vaikeustaso

    print('Olette päässeet pitkälle; Viereiseen kylpyhuoneeseen.')
    while True:
        print('Valintojen aika, mitä teet?')
        print('Jos haluat pestä Havinan suihkussa, paina 1.')
        print('Jos haluat pestä Havinan hampaat, paina 2.')
        print('Jos haluat mennä itse suihkuun, paina 3.')
        print('Jos haluat pestä Havinan pepun, paina 4.')
        print('Jos haluat pestä omat hampaat, paina 5.')
        print('Jos haluat vaihtaa itseltäsi aamutakin päivävaatteisiin, paina 6.')
        print('Jos haluat Havinan menevän potalle, paina 7.')
        print('Jos haluat vaihtaa Havinan yövaatteet päivävaatteisiin, paina 8.')
        print('Jos täällä ei ole enempää tehtävää, paina 9, ja lähdette alakertaan.')

#        print(vaikeustaso)
        vessaValinta = input('> ')
        if vessaValinta == '9':
            if hoonVaatteet == True:
                print('"Move on, kyllä tämä tästä", päätät ja lähdette laskeutumaan alakertaan ja kohti aamupalaa.')
                input('Paina mitä tahansa jatkaaksesi.')
                break
            else:
                print('Ehditte alakertaan ja mietit miten Havina on jotenkin eri näköinen kuin normaalisti. Silloin huomaat, että pukeminen jäi tekemättä. palaatte yläkertaan')
                pistetilanne(-5)
                aika(-3)
                input('Paina mitä tahansa jatkaaksesi.')
                continue
        if vessaValinta == '1':
            if vaikeustaso == 1:
                print('Aikaa kuluu suihkussa, mutta Havina nauttii. Annat hänen kokeilla suihkutella itsensä ja hän osaa jopa itse suihkutella itsensä puhtaaksi')
                pistetilanne(10)
                aika(-20)
                input('Paina mitä tahansa jatkaaksesi.')
            elif vaikeustaso < 1:
                print('Hetkellinen tappelu siitä halutaanko suihkuun päättyy Havinan murinaan ja ikuiseen juuri oikeanlämpöisen veden säätämiseen.')
                print('Lopputulos: lapsi itkee, sinun aamutakkisi on täysin märkä ja silti kukaan ei kostunut tästä mitään.')
                pistetilanne(2)
                aika(-20)
                input('Paina mitä tahansa jatkaaksesi.')
        elif vessaValinta == '2':
            while True:
                print('"Haluan katsoa Ryhmä Hauta!"')
                print('Kaivatko Yle Areenan puhelimesta?')
                hau = (input('Joo vai Ei? > ')).lower()
#                print(hau)
                if hau == 'joo' and vaikeustaso == 1:
                    print('"...jälleen vauhti päällä." 2 minuuttia menevät lennokkaasti Vainun ja kumppaneiden seurassa ja hampaat ovat puhtaat. Kuka olisi uskonut, että Samppa kaatuu?')
                    aika(-3)
                    pistetilanne(15)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                elif hau == 'joo':
                    print('Äst. Olet jättänyt puhelimen alakertaan. Mitäs nyt?')
                    if vaikeustaso == 2:
                        print('Saat Havinan pesemään hampaat, kun lupaat, että alakerrassa hän saa katsoa kokonaisen jakson. Hampaat puhtaat ja mieli odottava!')
                        aika(-4)
                        pistetilanne(15)
                        input('Paina mitä tahansa jatkaaksesi.')
                        break
                    else:
                        print('Yrität ehdottaa, että hän Havina saisi katsoa jakson alakerrassa, mutta mikään ei auta, kuppi on nurin ja suu pysyy kiinni. Hampaat jäävät pesemättä.')
                        aika(-5)
                        pistetilanne(-15)
                        input('Paina mitä tahansa jatkaaksesi.')
                        break
                elif hau == 'ei':
                    print('"Nyt pestään hampaat, eikä katsota." Se on viimeinen virhe. Alkaa sen päiväinen huuto, mutta kuitenkin suu kiinni, ettei harjaa vahingossakaan saa koskettamaan hampaita.')
                    aika(-5)
                    pistetilanne(-15)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                else:
                    print('kirjoita "joo" tai "ei".')
        elif vessaValinta == '3':
            print('Tässä vaiheessa, koet tosissasi olevasi suihkun tarpeessa. Annat Havinan katsoa Ryhmä Hauta sillä aikaa kun itse sutaiset itsesi puhtaaksi äkkisuihkulla.')
            aika(-7)
            pistetilanne(1)
            input('Paina mitä tahansa jatkaaksesi.')
        elif vessaValinta == '4':
            print('Otat Havinan vaipan pois ja nappaat Havinan hanan alle peppupesulle.')
            aika(-4)
            pistetilanne(10)
            input('Paina mitä tahansa jatkaaksesi.')
        elif vessaValinta == '5':
            print('Tartut harjaasi ja peset hampaasi. Se vie kaksi minuuttia arvokasta aikaasi, mutta olo on kuin uudestisyntynyt.')
            aika(-2)
            pistetilanne(20)
            input('Paina mitä tahansa jatkaaksesi.')
        elif vessaValinta == '6':
            print('Päätät vaihtaa aamutakin pois ja säälliset vaatteet tilalle. Hyviä päätöksiä.')
            aika(-3)
            pistetilanne(5)
            aamutakki = False
            input('Paina mitä tahansa jatkaaksesi.')
        elif vessaValinta == '7':
            if int(vaikeustaso) == 1:
                print('"Menisitkö potalle Höppänä?", kysyt ja H vastaa myöntävästi. Pikku hetken kuluttua pissa on valmis ja aamu voi jatkua.')
                aika(-2)
                pistetilanne(15)
                input('Paina mitä tahansa jatkaaksesi.')
            else:
                print('"Haluan lukea kirjaa"')
                kirja = input('Annatko kirjan, joo vai ei? > ')
                if kirja.lower() == "joo":
                    if int(vaikeustaso) == 2:
                        print('Aikaa kuluu, mutta valmista tulee, saatte pissan aikaiseksi muutamassa minuutissa, kun kirja on luettu kerran ja kuvat katsottu neljä kertaa.')
                        aika(-7)
                        pistetilanne(15)
                        input('Paina mitä tahansa jatkaaksesi.')
                    elif int(vaikeustaso) == 3:
                        print('Kirja imee mukaansa ja joudutte ikuiseen kirjalimboon. Sieltä ei ole ulospääsyä. Vain kirjoja kirjojen perään. Aikanne loppuu "Uskomaton Olof" -kirjan kohdalla.')
                        aika(-200)
                        input('Paina mitä tahansa jatkaaksesi.')
                elif kirja.lower() == "ei":
                    print('"Nyt ei lueta kirjaa."')
                    print('"Minä haluan, ääh yääh eieieieieieIEEIEIEieieiie!!!')
                    print('Ei pissaa, mutta paha mieli. Kiitoss.')
                    aika(-3)
                    pistetilanne(-15)
                    input('Paina mitä tahansa jatkaaksesi.')
                else:
                    print('En ymmärrä vastaustasi. Ei pissata.')
        elif vessaValinta == '8':
            if hoonVaatteet == True:
                print("Vaatteet on jo vaihdettu. Älä sekoile.")
                input('Paina mitä tahansa jatkaaksesi.')
            elif vaikeustaso == 1:
                print('Eiliset lempivaatteet, Kaja-sukat, Vainu-paita ja yksisarvishousut, vaihtuvat päälle vikkelästi ja iloinen värien sateenkaari on valmis lähtemään kerhoon.')
                pistetilanne(15)
                aika(-2)
                hoonVaatteet = True
                input('Paina mitä tahansa jatkaaksesi.')
                continue
            else:
                print('Eilispäivän vaatteet ovat likaiset. Täytyy hakea uudet. Valitsetko vaatteet?')
                vaateparsi = input('joo vai ei?' )
                if vaateparsi.lower() == 'joo' and int(vaikeustaso) == 2:
                    print('Valitsemasi vaatteet ovat lähestulkoon Havinalle mieleen, ja vain pari kierrosta housuja vaihdetaan, ennenkuin oikeat löytyvät.')
                    pistetilanne(15)
                    aika(-5)
                    hoonVaatteet = True
                    input('Paina mitä tahansa jatkaaksesi.')
                    continue
                elif vaateparsi.lower() == 'joo' and int(vaikeustaso) == 3:
                    print('Mikään ei kelpaa. Yrität yhä uutta vaatetta, mutta kaikki on menetetty. Lopulta vaatteeksi kelpaavat pyykkikorista löytyvä tahroja täynnäoleva Vainu-paita')
                    pistetilanne(3)
                    aika(-10)
                    hoonVaatteet = True
                    input('Paina mitä tahansa jatkaaksesi.')
                    continue
                else:
                    print("Päätät antaa Havinan valita itse vaatteet silläkin uhalla, että siihen tuhlaantuu kalliita minuutteja.")
                    print("Lopputulos: Havina löytää etsimänsä äkkiä ja pukeutuminen sujuu vauhdikkaasti. Jes")
                    pistetilanne(20)
                    aika(-3)
                    hoonVaatteet = True 
                    input('Paina mitä tahansa jatkaaksesi.')
                    continue        
        else:
            print('Tuo ei ollut sopiva numero. Kokeilehan uudelleen.')       
    aamupala()

def aamupala():
    print("Pääsit aamupalalle asti. Well done.")
    hooHaluaa = random.choice(['muroja', 'mysliä', 'muroja ja jogurttia', 'muroja ja jogurttia erikseen', 'jogurttia', 'leipää', 'klementiiniä', 'ei mitään', 'puuroa'])
    print('Aamupalan vuoro. Mitäs laitetaan?')
    print('Kysytkö Havinalta vai laitatko vain jotain?')
    palanKysyminen = (input("Kysyn/En \n> ")).lower()
    if palanKysyminen == 'kysyn':
        print(f"Viisas valinta. Havina kertoo haluavansa {hooHaluaa}.")
        pistetilanne(10)
    elif palanKysyminen == 'en':
        print("Nonni. Yritä sitten arvata...")
    else:
        print('En ymmärrä. Mennään arvaamalla...')

    print("Mitäs laitetaan? Normaalisti tarjolla on jotain näistä: muroja, mysliä, muroja ja jogurttia, muroja ja jogurttia erikseen, jogurttia, leipää, klementiiniä tai puuroa.")
    yritykset = 0
    while True:
        pöytään = (input('> ')).lower()
        if pöytään == hooHaluaa and hooHaluaa != 'ei mitään':
            print("Oikea vastaus, Havina hyökkää pöytään innolla ja syö kauniisti koko lautasellisen.")
            pistetilanne(15)
            aika(-10)
            input('Paina mitä tahansa jatkaaksesi.')
            lähdössä()
        elif pöytään == hooHaluaa and hooHaluaa == 'ei mitään':
            print("Kuulet mitä Havina sanoo ja artikuloit hänelle selvin sanakääntein, että aamupala on päivän tärkein ateria, ja että Oliverkin syö aamupalan aina.")
            print('"Hyvä on", Havina sanoo ja syö mitä tarjotaan, onneksi.')
            pistetilanne(10)
            aika(-15)
            input('Paina mitä tahansa jatkaaksesi.')
            lähdössä()
        else:
            print('No nyt ei osunut aivan oikein, yritäs uudelleen.')
            aika(-3)
            yritykset = yritykset + 1
            if yritykset == 5:
                print("Ei tästä nyt tule yhtään mitään. Täytyy lähteä kerhoon tyhjin vatsoin.")
                pistetilanne(-30)
                input('Paina mitä tahansa jatkaaksesi.')
                lähdössä()


def lähdössä():
    global reppuMukana
    global repunSisältö
    global maski
    tietoKoronasta = False
    
    print("Melkein kerhossa, hyvin menee. Nyt on syöty ja pitäisi varmaan valmistautua jotenkin. Mitä teet?")
    try:    
        while True:
        
            print("Jos haluat leikkiä, paina 1.")
            print("Jos pitäisi ottaa Havinan reppu, paina 2.")
            print("Jos haluat lukea lehden, paina 3.")
            print("Jos haluat nyt vaan lähdetään sinne kerhoon, paina 4.")
            
            
            if reppuMukana == True:
                print("Jos haluat pakata repun, paina 5.")
            if tietoKoronasta == True:
                print("Jos haluat napata maskin taskuun, paina 6.")
            lähtöValinta = int(input("> "))
            if lähtöValinta == 4:
                print('"Eiku nyt vaan tehään tää", huokaat ja puet Havinalle takin päälle')
                if reppuMukana == True:
                    print("Muistat vielä Havinan repunkin ja jopa omat avaimesi, joten olette valmiita.")
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                else:
                    print("Kaikki ei taida olla muuten mukana... Mennääs miettimään.")
                    continue
            if lähtöValinta == 1:
                print("Leikitte hetken Ryhmä Hau hahmoilla. Sinä saat olla Rolle ja Havina on Vainu. Paitsi jos haluat olla Rolle niin silloin saat olla Vainu.")
                aika(-15)
                pistetilanne(15)
                input('Paina mitä tahansa jatkaaksesi.')
                continue
            elif lähtöValinta == 2:
                print("Hyvä idea ottaa Havinan reppu. Sitä tarvitaankin kerhossa.")
                reppuMukana = True
                pistetilanne(10)
                aika(-2)
                input('Paina mitä tahansa jatkaaksesi.')
                continue
            elif lähtöValinta == 3:
                print("Päätät lukea Kirkkonummen Sanomia ja teeskennellä kuinka mukavan rauhallinen aamu teillä on.") 
                print("Lehdessä kerrotaan uusista Koronarajoitteista ja vedotaan ihmisiä käyttämään maskia kaikissa julkisissa tiloissa, kuten kouluissa, päiväkodeissa yms.")
                print("Hmm...")
                aika(-10)
                tietoKoronasta = True
                input('Paina mitä tahansa jatkaaksesi.')
                continue

            elif lähtöValinta == 5:
                if reppuMukana == True:
                    print('Haluat pakata repun. Mitä otetaan mukaan? Kirjoita asioita yksi kerrallaan allaolevaan nuoleen ja paina enter. Kun olet valmis, kirjoita "valmis"')
                    while True:
                        print(*repunSisältö, sep='\n')
                        tavara = input('> ')
                        if tavara == 'valmis':
                            print('Noin, ei uskoisi, että Kånkeniin mahtuu noin paljon tavaraa.')
                            break
                        else:
                            repunSisältö.append(tavara)
                else:
                    print("Kuka sinulle on kertonut tästä valinnasta. Mene pois ja pelaa sääntöjen mukaan. Ei voi pakata reppua, jos sitä ei ole.")
                    continue

            elif lähtöValinta == 6 and maski == False:
                if tietoKoronasta == True:
                    print("Mikä Kirkkiksen Sanomissa lukee, se on uskottava. Nappaat maskin mukaan, hyvä hyvä.")
                    pistetilanne(10)
                    maski = True
                    input('Paina mitä tahansa jatkaaksesi.')
                    continue
                else:
                    print("Ilmeisesti sinulla on tietoa koronasta ilman lehteäkin. Tietäjät tietää. Maskin mukaanottaminen on kuitenkin hyvä juttu.")
                    pistetilanne(10)
                    maski = True
                    input('Paina mitä tahansa jatkaaksesi.')
                    continue
            elif lähtöValinta == 6 and maski == True:
                print('Kuinka monta naamaa sinulla on? Yksi maski riittää.')
                input('Paina mitä tahansa jatkaaksesi.')
                continue
    except:
        print('Tuo ei ollut numero, yritähän vielä.')
        lähdössä()
    finally:
        matkalle()
        


def matkalle():
    global vaikeustaso
    
    while True:
        print("No nyt ollaan jo tosi lähellä. Milläs mennään?")
        print('Jos haluat, että kävelette yhdessä, paina 1.')
        print('Jos haluat, että Havinalle otetaan potkupyörä, paina 2.') 
        print('Jos haluat, että menette autolla, paina 3.')
        print('Jos kannat Havinan perille asti, paina 4.')
        try:
            matkustusTapa = int(input('> '))
            if matkustusTapa == 1:
                if int(vaikeustaso) == 1:
                    print('Kävelette lintujen laulaessa kauniisti käsi kädessä kerhoon.') 
                    print('Matka menee niin mukavasti, että ehditte pysähtyä katsomaan jopa pientä hiirulaista, joka vie istuttamiasi kukkasipuleita kukkapenkistä parempaan talteen.')
                    print('Saavutte päiväkodin portille.')
                    aika(-10)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                elif int(vaikeustaso) == 2:
                    print('Käveleminen on suhteellinen käsite, kun Havina keksii leikkiä taikinaa. Lopulta saat lapsesi motivoitumaan keksimällä improvisoidun tanssin. Naapurit tykkää ja aikaa kuluu')
                    print('Saavutte päiväkodin portille.')
                    aika (-20)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                else:
                    print('"Lajin helppous viehättää", ajattelet, kun parkkipaikalle rynnännyt lapsesi meinaa jäädä 100 metrin matkalla jo toistamiseen auton alle. Juuri kun portit häämöttävät edessä,')
                    print('päättää Havina lähteä juoksemaan takaisin kohti kotia. Matkalla hän polkaisee jalkansa Kirkkonummen erikoiseen, eli aitoon höyryävään rottweilerin köntsään niin, että ainut vaihtoehto')
                    print('käydä vaihtamassa kengät ja jättää haiseva palkinto tuulikaappiin odottamaan jatkotoimenpiteitä. Kuin ihmeen kaupalla uudet kengät vievät Havinan kommelluksitta päiväkodille.')
                    print('Saavutte päiväkodin portille.')
                    aika(-20)
                    pistetilanne(-10)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
            elif matkustusTapa == 2:
                if int(vaikeustaso) == 1:
                    print('Kypärä kiinni ja menoksi. Vauhdin hurmaa, pääsette juoksuvauhtia alamäkeen, koska Havinasta on vuoden aikana tullut aika peto potkupyöräilyssä.')
                    print('Havina taluttaa pyörän suojatien yli ja saa Oliverin kiinni, kun hän on Samin kanssa myös menossa samaan suuntaan. Pikku hipat vielä ennen portteja. Kaikki nauravat.')
                    print('Saavutte päiväkodin portille.')
                    aika(-5)
                    pistetilanne(10)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                elif int(vaikeustaso) == 2:
                    print('Potkupyöräily sujuu mallikkaasti, kunnes Havina kääntyy katsomaan lentävää korppia ja menettää tasapainonsa. Havina kaatuu ja polveen sattuu. Puhallus auttaa mutta lohduttaessa menee aikaa.')
                    print('Saavutte päiväkodin portille.')
                    aika(-15)
                    pistetilanne(-5)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                else:
                    print('Kun saat oven auki, ajattelet että hurraa! Näet edessäsi Oliverin matkalla päiväkotiin hienolla polkupyörällä. Yhtäkkiä potkupyöräily menettää hohtonsa Havinan silmissä ja hänen on aivan pakko')
                    print('saada ajaa Oliverin polkupyörällä. Tätä pakkoa ei poista lukuisat yritykset selittää, ettei Havinan jalat edes yllä polkimille, saati että hän osaisi ajaa polkupyörää.') 
                    print('Oliver ja Sami joutuvat menemään edeltä ja jättävät sinut täydellisen murtumisen kokeneen kaksivuotiaan kanssa kaksin. Sylittely ja halaukset eivät auta vaan lopulta kannat itkevän lapsen ja')
                    print('potkupyörän kerholle.')
                    print('Saavutte päiväkodin portille.')
                    aika(-20)
                    pistetilanne(-5)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
            elif matkustusTapa == 3:
                print('Ai autolla? Ai päiväkodille? Ai siis naapuriin? Ookoo.')
                print('Auto on jäässä ja nauttii suunnattomasti, kun ajat sillä minuutin matkan, kun olet ensin skrabannut laseja 19 minuuttia.')
                print('Saavutte päiväkodin portille.')
                aika(-20)
                pistetilanne(-10)
                input('Paina mitä tahansa jatkaaksesi.')
                break
            elif matkustusTapa == 4:
                print('Nopein tapa saada asiat liikkeelle on juosta lapsi sylissä. Ei eleganttia, mutta niistää minuutteja. Go Usain Bolt!')
                print('Saavutte päiväkodin portille.')
                pistetilanne(-5)
                aika(-5)
                input('Paina mitä tahansa jatkaaksesi.')
                break
            else:
                print('******************')
        except:
            print('Väärä nappi, kokeile uudelleen.')
            matkalle()
        finally:
            break
    portilla()


def portilla():
    global reppuMukana
    global repunSisältö
    global aamutakki
    global maski
    global pisteet
    global aikaaJaljella
    print('Noniin, vihdoin portilla. Mari jo vilkutteleekin pihalta.')
    if maski == True:
        print('Laitat maskin päällesi ja tunnet olevasi vastuuntuntoinen kansalainen.')
        pistetilanne(10)
        input('Paina mitä tahansa jatkaaksesi.')
    else:
        print('Tajuat, että sinulla ei ole maskia mukana, joten joudut häpeään ja ihmiset katsovat sinua pahasti. Nolona yrität hengittää vain tarvittaessa.')
        pistetilanne(-15)
        input('Paina mitä tahansa jatkaaksesi.')

    if aamutakki == True:
        print('Mari katsoo sinua kummissaan, ja huomaat vasta nyt, että omat vaatteesi ovat vaihtamatta ja että olet saapunut paikalle aamutakki lepattaen. Kiusallista.')
        pistetilanne(-10)
        input('Paina mitä tahansa jatkaaksesi.')
    
    if reppuMukana == False:
        print('Ai perhana nyt muistat, että reppuhan pitää olla mukana. Ei muuta kuin lapsi kainaloon ja pikapikaa takaisin kotiin hakemaan reppua.')
        aika(-5)
        input('Paina mitä tahansa jatkaaksesi.')
        lähdössä()
    print('Pussaat Havinaa ja toivotat hänelle mukavaa kerhopäivää. Havina juoksee Hemmon ja Edvinin luo leikkimään. Huokaiset helpotuksesta ja hyväntahtoinen Mari katsoo sinua.') 
    print('Kenties tuntee jonkinlaista myötätuntoakin sinua kohtaan.')
    input('Paina mitä tahansa jatkaaksesi.')
    input('\n \n \n \n \n')
    print('Noniin tehtävä suoritettu, aika laskea pisteet.')
    print(f'sait aamun toiminnastasi {pisteet} pistettä. Ei siinä vielä kaikki')
    print('Mitäs repussa on?')
    summa = 0
    for i in repunSisältö:
        if i == 'eväät':
            print('Eväistä sai viisitoista pistettä.')
            pistetilanne(15)
            summa = summa + 1
        elif i == 'vaippa':
            print('Vaipasta saa kymmenen pistettä.')
            pistetilanne(10)
            summa = summa + 1
        elif i == 'varavaatteet':
            print('Varavaatteista saa kymmenen pistettä.')
            pistetilanne(10) 
            summa = summa + 1
        elif i == 'vaihtovaatteet':
            print('Vaihtovaatteista saa kymmenen pistettä')
            pistetilanne(10)
            summa = summa + 1      
        else:
            print(f'Repusta löytyi {i}. Siitä ei saa pisteitä.')
            pistetilanne(0)
    if summa == 0:
        print('Repussa ei ollut mitään hyödyllistä. Pakkasitko sitä edes?')
    if summa > 0:
        print(f'Repussa oli {summa} hyödyllistä asiaa.')
    print('\n'*6)
    print('***********************************TULOS*******************************')
    print(f'                      Sait aamusta pisteitä {pisteet}')
    print(f'           Sehän meni ihan kivasti. Aikaa jäi {aikaaJaljella} minuuttia')
    print('***********************************************************************')
    exit(0)                      

def start():
    global vaikeustaso
    print('\n\n')
    print('KKKKKKKKK    KKKKKKKEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   HHHHHHHHH     HHHHHHHHH     OOOOOOOOO                    AAA                              AAA               MMMMMMMM               MMMMMMMMUUUUUUUU     UUUUUUUU')
    print('K:::::::K    K:::::KE::::::::::::::::::::ER::::::::::::::::R  H:::::::H     H:::::::H   OO:::::::::OO                 A:::A                            A:::A              M:::::::M             M:::::::MU::::::U     U::::::U')
    print('K:::::::K    K:::::KE::::::::::::::::::::ER::::::RRRRRR:::::R H:::::::H     H:::::::H OO:::::::::::::OO              A:::::A                          A:::::A             M::::::::M           M::::::::MU::::::U     U::::::U')
    print('K:::::::K   K::::::KEE::::::EEEEEEEEE::::ERR:::::R     R:::::RHH::::::H     H::::::HHO:::::::OOO:::::::O            A:::::::A                        A:::::::A            M:::::::::M         M:::::::::MUU:::::U     U:::::UU')
    print('KK::::::K  K:::::KKK  E:::::E       EEEEEE  R::::R     R:::::R  H:::::H     H:::::H  O::::::O   O::::::O           A:::::::::A                      A:::::::::A           M::::::::::M       M::::::::::M U:::::U     U:::::U ')
    print('  K:::::K K:::::K     E:::::E               R::::R     R:::::R  H:::::H     H:::::H  O:::::O     O:::::O          A:::::A:::::A                    A:::::A:::::A          M:::::::::::M     M:::::::::::M U:::::D     D:::::U ')
    print('  K::::::K:::::K      E::::::EEEEEEEEEE     R::::RRRRRR:::::R   H::::::HHHHH::::::H  O:::::O     O:::::O         A:::::A A:::::A                  A:::::A A:::::A         M:::::::M::::M   M::::M:::::::M U:::::D     D:::::U ')
    print('  K:::::::::::K       E:::::::::::::::E     R:::::::::::::RR    H:::::::::::::::::H  O:::::O     O:::::O        A:::::A   A:::::A                A:::::A   A:::::A        M::::::M M::::M M::::M M::::::M U:::::D     D:::::U ')
    print('  K:::::::::::K       E:::::::::::::::E     R::::RRRRRR:::::R   H:::::::::::::::::H  O:::::O     O:::::O       A:::::A     A:::::A              A:::::A     A:::::A       M::::::M  M::::M::::M  M::::::M U:::::D     D:::::U ')
    print('  K::::::K:::::K      E::::::EEEEEEEEEE     R::::R     R:::::R  H::::::HHHHH::::::H  O:::::O     O:::::O      A:::::AAAAAAAAA:::::A            A:::::AAAAAAAAA:::::A      M::::::M   M:::::::M   M::::::M U:::::D     D:::::U ')
    print('  K:::::K K:::::K     E:::::E               R::::R     R:::::R  H:::::H     H:::::H  O:::::O     O:::::O     A:::::::::::::::::::::A          A:::::::::::::::::::::A     M::::::M    M:::::M    M::::::M U:::::D     D:::::U ')
    print('KK::::::K  K:::::KKK  E:::::E       EEEEEE  R::::R     R:::::R  H:::::H     H:::::H  O::::::O   O::::::O    A:::::AAAAAAAAAAAAA:::::A        A:::::AAAAAAAAAAAAA:::::A    M::::::M     MMMMM     M::::::M U::::::U   U::::::U ')
    print('K:::::::K   K::::::KEE::::::EEEEEEEE:::::ERR:::::R     R:::::RHH::::::H     H::::::HHO:::::::OOO:::::::O   A:::::A             A:::::A      A:::::A             A:::::A   M::::::M               M::::::M U:::::::UUU:::::::U ')
    print('K:::::::K    K:::::KE::::::::::::::::::::ER::::::R     R:::::RH:::::::H     H:::::::H OO:::::::::::::OO   A:::::A               A:::::A    A:::::A               A:::::A  M::::::M               M::::::M  UU:::::::::::::UU  ')
    print('K:::::::K    K:::::KE::::::::::::::::::::ER::::::R     R:::::RH:::::::H     H:::::::H   OO:::::::::OO    A:::::A                 A:::::A  A:::::A                 A:::::A M::::::M               M::::::M    UU:::::::::UU    ')
    print('KKKKKKKKK    KKKKKKKEEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRRHHHHHHHHH     HHHHHHHHH     OOOOOOOOO     AAAAAAA                   AAAAAAAAAAAAAA                   AAAAAAAMMMMMMMM               MMMMMMMM      UUUUUUUUU      ')

    print('\n\n')
    print("Tervetuloa pelaamaan 'Kerhoaamu' -peliä. Ensimmäisenä valitaan int(vaikeustaso).")
    print("Millainen aamu tänään on?")
    def ekavalinta():
        global vaikeustaso
        while True:
            print('Jos aamu on hyvä, valitse 1 | Jos aamu on nääh, valitse 2 | Jos aamu on suoraan helvetistä, valitse 3: ')
            syote = input("> ")
            if syote == '1' or syote == '2' or syote == '3':
                vaikeustaso = int(syote)
                if vaikeustaso == 1:
                    print("Linnut laulavat ja herättävät teidät lattialta.")
                    print('Havina kääntyy hymyillen puoleesi ja sanoo: "Hyvää huomenta kultarakas. Herätäänkö?"')
                    print('Olet mennyt aikaisin nukkumaan, joten olet valmis päivään. Mitä teet?')
                    aika(120)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                elif vaikeustaso == 2:
                    kello = 90
                    print("Olisitpa uskonut, kun sinulle sanottiin, että mene nukkumaan. Väsyttää.")
                    print("Ei se mitään. Havina on herännyt ja pomppii päälläsi.")
                    print("Mitä teet?")
                    aika(kello)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
                elif vaikeustaso == 3:
                    kello = 45
                    print("Heräät karmivaan kirkunaan! Nielet sydäntäsi suustasi samalla kun yrität rauhoittaa sekä lastasi, että itseäsi.")
                    print('"What a day", ajattelet kun verta viimein riittää aivoihisi. Katsot kelloa ja mietit miksi sydämesi syke kiihtyy jälleen.')
                    print('Ymmärrys hiipii sinuun moukarin lailla: Aikaa kerhon alkuun on kolme varttia!')
                    aika(kello)
                    input('Paina mitä tahansa jatkaaksesi.')
                    break
            else:
                print("kirjoita numero 1-3.")
        
    ekavalinta()
#    print(vaikeustaso)
    valinta()

start()    
exit(0)