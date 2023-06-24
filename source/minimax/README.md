# Minimax algoritme

## Introductie
Dit is een minimax algoritme met alpha-beta pruning die toegepast kan worden bij zero-sum games met spelstukken die acties kunnen ondernemen zoals Dammen en Schaken.

## Specificaties
Het algoritme is zo geschreven dat het ingevoegd kan worden in een bord- of spelklasse. Het krijgt een integer 'depth' mee dat naar 0 telt om niet oneindig door te lopen. Ook heeft het twee parameters alpha en beta om het efficienter te maken en natuurlijk een boolean 'isMaximizing' om bij te houden wat er gekozen moet worden.

## Implementeren
Allereerst is er een bord- of spelklasse nodig die als overkoepelende klasse werkt om het speelveld op te slaan en alle functies op te roepen. Het algoritme kan op deze manier toegevoegd worden aan de klasse

```
from minimax.algorithm import minimax as algorithm

class Example:
    def __init__(self):
        # doe iets

    # hier wordt de minimax functie aan deze klasse
    # toegevoegd onder de naam 'minimax'
    minimax = algorithm
```
De klasse heeft de volgende functies nodig voor de werking van het minimax algoritme
* estimateScore()
    * Voor het toekennen van een score aan een bordstatus wanneer de zoekdiepte gevonden is
* numPossibleMoves(player: str)
    * Voor het checken van een terminale node
* getPieces(player: str)
    * Voor het verkrijgen van alle coordinaten van de stukken van 1 speler
* getMoves(x :int, y:int, player:str)
    * Voor het verkrijgen van alle coordinate waar een stuk op een gegeven coordinaat naar toe kan gaan
* move(xOld:int, yOld:int, xNew:int, yNew:int)
    * Voor het verzetten van een stuk op het bord

Als deze functies geïmplementeerd zijn kan minimax op de volgende manier aangeroepen worden.

```
def handleMinimaxTurn(self, parameters):
    # bepaal een maximale zoekdiepte
    maxDepth = 4

    # isMaximizing is True als speler wit als volgende
    # aan de beurt is
    isMaximizing = True

    # loop door alle mogelijke zetten, maak die zetten
    # in een kopie van het huidge spelbord en doe het
    # volgende per zet.

    score = boardCopy.minimax(maxDepth, -Inf, Inf, isMaximizing)

    # bepaal dmv de score welke zet er gemaakt moet
    # worden.
```