# Vokabellisten-Generator_Latein

Ein Python-Projekt, das Daten aus einem öffentlich zugänglichen Wörterbuch (via API) interpretiert und in eine Vokabelliste exportiert. Es wird ein Algorithmus verwendet, um relevante Daten zu extrahieren, zu verarbeiten und in einem benutzerfreundlichen Format (z. B. Excel) bereitzustellen.

## Überblick

Dieses Projekt nutzt eine externe API, um Wörter und deren Definitionen aus einem Wörterbuch abzurufen. Diese Daten werden durch einen Algorithmus interpretiert und in einer Vokabelliste exportiert. Die Vokabelliste kann als Grundlage für Sprachübungen, Lernmaterialien oder andere Anwendungen dienen.

## Installation

### Voraussetzungen

- Python 3.x
- Notwendige Python-Bibliotheken aus "requirements.txt"

### Projekt klonen

1. Das Repository klonen:

```bash
https://github.com/BenniBoy602/Vokabellisten-Generator_Latein.git
cd Vokabellisten-Generator_Latein
```

2. Alle Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

## Nutzung

### 1. Projekt ausführen

Das Hauptskript des Projekts heißt `app.py`. Du kannst es direkt mit der `py`-App ausführen, um die Vokabelliste zu generieren.

```bash
py app.py
```

Wenn `py` korrekt installiert ist, wird das Skript gestartet und due kannst es benutzerfreundlich im Browser über Gradio nutzen.

### 2. Vokabelliste nutzen
#### Standart-Funktion
In dem Gradio Interface kannst du einfach den text einfügen und auf Absenden klicken.
Rechts findest du dann deine Datei als Download.

Optional:
- Export nach Brainyoo(Lernsoftware für Vokabeln): muss im Desktop Browser als Datei importiert werden.
- Einstellungen der Anzahl an Therads (nur für fortgeschrittene User), kann bei der Geschwindigkeit einen gravierenden Unterschied machen.
Vorschau:
![alt text](https://github.com/BenniBoy602/Vokabellisten-Generator_Latein/blob/main/images/Interface.png "Interface Vorschau")

#### Alternativ
Wenn man oben neben "Texteingabe" zum Reiter "Datei-Upload (.docx) wechselt, kann man eine Word-Datei hochladen. Hierbei ist wichtig, dass die erwünschten Vokabeln entweder mit einem beliebigen Textmarker markiert sind oder eine rote Textfarbe haben. Beim Textmarker ist zu beachten, dass die Markierung nur funktioniert wenn es in einer aktuellen Version des originalen Word erstellt wird, alternative Programme wie LibreOffice funktionieren nicht. Daher empfehle ich die Nutzung der roten Textfarbe.

## Lizenz

Die Daten, die in diesem Projekt verwendet werden, stammen von "https://www.navigium.de/suchfunktion/_search?q={}". Das Projekt verwendet die Daten zu nicht-kommerziellen Zwecken und die Verantwortung für die Richtigkeit und Verfügbarkeit der Daten liegt beim Anbieter.

- Die Nutzung der Daten unterliegt den allgemeinen rechtlichen Bestimmungen des Anbieters. Weitere Informationen findest du im Impressum des Anbieters.
- Das Projekt selbst ist unter der [MIT-Lizenz](https://opensource.org/licenses/MIT) lizenziert.

## Haftungsausschluss

Dieses Projekt nutzt öffentlich zugängliche Daten von "https://www.navigium.de/suchfunktion/_search?q={}" für nicht-kommerzielle Zwecke. Die Daten werden lediglich interpretiert und weiterverarbeitet. Der Autor übernimmt keine Haftung für die Nutzung durch Dritte oder die Richtigkeit der Quelldaten.


Falls du noch weitere Anpassungen oder zusätzliche Erklärungen benötigst, lass es mich wissen! 😊
