Feature: BDD-Python-Sample

Scenario: First Python scenario
	Given StringHelper sinifindan kopya olusturacagim
	When RemoveDiacritics metoduna parametre olarak "Merhaba Dünya Ben Maraşlı" ve "True" gececegim
	Then Sonuc "merhaba dunya ben marasli" seklinde olmali