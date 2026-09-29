# 1 Diskutera i grupp
Denna gången är det en fördel att diskutera de flesta uppgifterna.
Planera din tid, så att du hinner arbeta med övningar från alla kapitel. Du behöver alltså inte göra "färdigt" alla tidigare övningar innan du går vidare på nästa.

### 1a. Vilka strängar matchas av det reguljära uttrycket: "ab" ?

Rätt svar: "sabotör"

### 1b. Betrakta uttrycket "nisse". Vad skriver jag för att matcha både "Nisse", "NISSE" och "nisse"?

Rätt svar: Man kan skriva ``re.compile("Agile Helper", re.IGNORECASE)``
IGNORECASE säger då att ignorerar upper och lowercase med andra oj inte case sensetive.

### 1d.  Vilka strängar matchas av "[ae]n" ?

Rätt svar: "en" i "inconsequential" eftersom [ae]n betyder a och n eller e och n.

### 1e. Vilka strängar matchas av "je.+e"?

Rätt svar: jeppe och je je, anledningen till detta är för att je.+e betyder att je måste vara med "." betyder att vad som helst kan vara här men de måster vara något innan nästa e kommer.

### 1f. Vilka strängar matchas av "\san?\s"

Rätt svar: "an na an" och "be a darling" eftersom "an" är ett eget ord i sin sträng och "a" är ett eget ord i "be a darling".

### 1e. Skriv ner med egna ord, vad följande uttryck matchar. "Strängar som innehåller…"

1."lines?" Strängar som innehåller "lines" och "line"

2."^a*ö$" stängar som bara är "a*ö"

3."[aeiouyåäö]+" alla strängar som innehåller bokstäverna på rad eller ensamma ex åäö eller ou

4."[123456789]\d*" strängar där första siffran måste vara nån av 1-9

5."\d{4}-\d{2}-\d{2}" strängar som matchar siffer mönstret, ex 3453-23-23

---
### 2a. Betrakta https://lejonmanen.github.io/agile-helper/ . Skriv en user story som beskriver att användaren ska kunna läsa hur man gör en "sprint retrospective".

- Som användare vill jag kunna läsa om "Sprint retrospective" på hemsidan.
- Så att jag kan lära mig mer och förstå mer om ämnet.
---

### 2b Skriv ner ett testscenario för user storyn. Använd en punktlista. Fundera särskilt på vad som ska testas implicit och explicit.
Implicit = underförstått, testas indirekt
Explicit = uttryckligen, testas direkt

- öppna hemsidan
- tryck på "sista"
- tryck på knappen som innehåller ordet "Sprint retrospective"
- Observera texten om retrospective

Vad som testas implicit är: - kan öppna sidan, - kan hitta "sista", - kan klicka på "sista", kan hitta och klicka på "Sprint retrospective"

Vad som explicit testas: - "Sprint retrospective" leder till rätt innehåll, att texten om sprint retrospective faktiskt finns.

---

### 3. Titta på kodexemplet från lektionen. Skriv upp allt du är osäker på och diskutera i grupp, eller fråga om på nästa lektion.

````python
def test_view_sprint_planning(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button") # Först deklarerar vi en variabel som är en button och kallar den locator
    first_button = locator.get_by_text("First") # Nu deklarerar vi att knappen skall leta efter "first" och sen ger vi den namnet first_button
    first_button.click(timeout=100) # vi tar den deklarerade knappen och lägger till .click med en timeout på 100ms

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning")) # Här gör vi samma sak, deklarer ett namnpå en knapp, att den ska leta efter "Sprint restrospective" 
    expect(sp_button).to_be_visible() # Här testar vi att knappen sen är synlig först.
    
    # Klicka på den
    sp_button.click(timeout=100) # Vi klickar på knappen med samma timeout 100ms

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning") # Vi deklarerar en variabel som letar efter rollen heading och att den ska innehålla "Sprint planning"
    expect(sp_heading).to_be_visible() # Här testar vi sedan att texten faktiskt är synlig.
````

---

## 2 Öva på regex
 1a. Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter: "Fiskarna som jag fångade var 55 cm långa."

 1b. Denna gången vill vi veta om det finns två längder.

 1c. Längderna ska vara samma enhet. "Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."


2. Skriv ett regex som matchar ett svenskt postnummer. Postnummer består av fem siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45" Om du vill övertänka fördjupa dig mera: https://sv.wikipedia.org/wiki/Postnummer_i_Sverige 

3. Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601, alltså 10 tecken med bindestreck mellan avdelningarna. Exempel: 2025-03-10.


4. Skriv ett regex som matchar ett pengavärde i siffror. Exempel på värden som ska matchas: 200 kr 12,50 kr 0,35 kr


5a. Skriv ett regex som matchar en e-postadress (användarnamn@server.domän) enligt följande icke kompletta regler.
användarnamn kan innehålla bokstäver, siffror och specialtecknen som punkt och bindestreck
server kan innehålla samma sorts tecken
domän kan innehålla bokstäver och siffror

5b. Gör ett regex som matchar en komplett e-postadress enligt specifikationen i artikeln här:
What is a valid email address format 



