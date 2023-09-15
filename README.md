# OSARegistry
Diplomprojekt mit co contributor Dominik Nowak

## Aufgabenstellung: ## 
Im Gegensatz zu anderen europäischen Ländern werden in Österreich bislang die unter Beatmungstherapie gestellten Patienten mit obstruktiver Schlafapnoe aus medizinischer Sicht nicht einheitlich erfasst. Durch den Aufbau einer sachgemäßen Datenbank, die von verschiedenen medizinischen Einrichtungen verwendet werden sollen, erhält man einen Überblick über die verwendeten Geräte und Beatmungsformen.
Eine Webapplikation, die es Ärzten ermöglicht, Patientendaten aus Schlaflaboren schnell und sicher in eine Datenbank zu speichern. Außerdem soll es möglich sein, diese Daten jederzeit und übersichtlich darzustellen.

Es wurde eine Webapplikation mit Django als Servertechnologie und HTML/CSS als Front-End realisiert.

## System Architektur ##

![image](https://github.com/Nour-hash/OSARegistry/assets/113339425/b3350f90-2ef3-4081-9e08-30b39cfc7c79)


Über ein Login-Fenster kann man auf das System zugreifen.
Es wird 4 Arten von Usern geben. Alle 4 Benutzer unterscheiden sich in der Verteilung der Rechte.
 
Die erste Art von Benutzer ist der Admin, dieser hat den vollen Zugriff aufs System, so kann dieser zum Beispiel neue Benutzer definieren und die Rechte von existierenden Benutzern bearbeiten oder Veränderungen am Datenbankmodell durchführen. 
Die zweite Gruppe von Benutzern sind die Schlaflabore. 
Diese können neue Datensätze erstellen, die genau vom Admin definiert sind und diese natürlich dann auch löschen oder verändern. Außerdem kann er auch Patient bezogene Daten ansehen. 
Der Arzt kann nur Patient bezogene Daten bearbeiten und lesen. 
Als letztens sind die Firmen, diese können nur bestimmte Daten hinzufügen und lesen.


## How to start: ##
install needed libaries

run localhost for the database

create the database

python OSA_Registry\manage.py makemigrations
python OSA_Registry\manage.py migrate
python OSA_Registry\manage.py runserver
