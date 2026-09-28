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
