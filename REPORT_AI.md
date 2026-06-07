# Sprawozdanie — wykorzystanie AI przy realizacji zadania

## 1. Do czego używałem AI

AI wykorzystałem w trakcie tworzenia rozwiązania.

Pomagało mi m.in. w:

- znalezieniu błędów w workflow n8n (np. brak parsowania odpowiedzi, złe połączenia node’ów)
- zaproponowaniu struktury promptu
- napisaniu parsera JSON i jego zabezpieczenia na błędy
- przygotowaniu skryptu w Pythonie do generowania raportu
- ogarnięciu całej struktury projektu (co gdzie zapisać i jak połączyć)

Nie traktowałem AI jako czegoś, co „robi projekt za mnie”, tylko bardziej jako narzędzie do przyspieszenia pracy i podpowiedzi.

---

## 2. Gdzie musiałem sam podjąć decyzje

Mimo użycia AI, sporo rzeczy musiałem ogarnąć sam:

- jak ma wyglądać cały flow (kolejność node’ów w n8n)
- jak obsłużyć błędy (np. gdy API zwraca 429 albo 503)
- jak zapisywać dane (format JSONL zamiast zwykłego JSON)
- jak połączyć wszystko w jeden pipeline (input → AI → zapis → raport)

Musiałem też sprawdzać, czy to co zwraca AI ma sens — bo model czasami się myli albo zwraca niepoprawny format.

---

## 3. Wnioski

AI bardzo przyspiesza pracę, szczególnie przy:

- analizie tekstu
- generowaniu kodu startowego
- debugowaniu

Ale nie można mu ufać w 100%. Trzeba:

- sprawdzać output
- zabezpieczać się na błędy
- rozumieć co się dzieje w kodzie

W tym projekcie AI pomogło mi zrobić system szybciej i lepiej, ale finalnie to ja odpowiadam za to, że wszystko działa poprawnie.
