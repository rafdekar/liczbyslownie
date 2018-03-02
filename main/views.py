from django.shortcuts import render, redirect

def index(request):
    if request.method == "POST":
        return redirect('main:result', number=request.POST['number'])
    else:
        return render(request, 'main/index.html')

def result(request, number):
    return render(request, 'main/result.html', { 'number_str': getNumberInWords(int(number)), })

def getNumberInWords(liczba): 
    jednosci = ["", " jeden", " dwa", " trzy", " cztery", " pięć", " sześć", " siedem", " osiem", " dziewięć"]
    nastki = ["", " jedenaście", " dwanaście", " trzynaście", " czternaście", " piętnaście", " szesnaście", " siedemnaście", " osiemnaście", " dziewiętnaście"]
    dziesiatki = ["", "dziesięć", " dwadzieścia", " trzydzieści", " czterdzieści", " pięćdziesiąt", " sześćdziesiąt", " siedemdziesiąt", " osiemdziesiąt", " dziewięćdziesiąt"]
    setki = ["", " sto", " dwieście", " trzysta", " czterysta", " pięćset", " sześćset", " siedemset", " osiemset", " dziewięćset"]
    grupy = [
        ["", "", ""],
        [" tysiąc", " tysiące", " tysięcy"],
        [" milion", " miliony", " milionów"],
        [" miliard", " miliardy", " miliardów"],
        [" bilion", " biliony", " bilionów"],
    ]

    g = 0 #rzad wielkosci
    znak = ''
    wynik = ''

    if liczba == 0:
        return 'zero'
    elif liczba < 0:
        znak = "minus"
        liczba = -liczba

    while liczba > 0:
        liczba_setek = liczba % 1000 // 100
        liczba_dziesiatek = liczba % 100 // 10
        liczba_nastek = 0
        liczba_jednosci = liczba % 10

        k = 0 #forma gramatyczna

        if liczba_dziesiatek == 1 and liczba_jednosci > 0:
            liczba_nastek = liczba_jednosci
            liczba_dziesiatek = 0
            liczba_jednosci = 0
        if liczba_jednosci == 1 and liczba_setek + liczba_dziesiatek + liczba_nastek == 0:
            k = 0
        elif liczba_jednosci == 2 or liczba_jednosci == 3 or liczba_jednosci == 4:
            k = 1
        else:
            k = 2

        wynik = setki[liczba_setek] + dziesiatki[liczba_dziesiatek] + nastki[liczba_nastek] + jednosci[liczba_jednosci] + grupy[g][k] + wynik

        g += 1

        liczba = liczba // 1000
            
    wynik = znak + wynik
    return wynik