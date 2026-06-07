# AI Ticket Triage — przykładowy raport

**Liczba zgłoszeń:** 10  
**Błędy analizy AI:** 0

## Podsumowanie

### Kategorie

| Kategoria | Liczba |
|-----------|--------|
| Recruitment | 2 |
| Support | 3 |
| Sales | 2 |
| Other | 3 |

### Sentyment

| Sentyment | Liczba |
|-----------|--------|
| Positive | 2 |
| Neutral | 5 |
| Negative | 3 |

### Priorytet

| Priorytet | Liczba |
|-----------|--------|
| High | 2 |
| Medium | 2 |
| Low | 6 |

## Zgłoszenia

| # | Imię i nazwisko | Email | Kategoria | Sentyment | Priorytet | Fragment wiadomości |
|---|-----------------|-------|-----------|-----------|-----------|---------------------|
| 1 | Anna Nowak | anna.nowak@example.com | Sales | Positive | Medium | Dzień dobry, chciałabym zapytać o możliwość współpracy i zakup Państwa usług ... |
| 2 | Tomasz Kowalczyk | t.kowalczyk@example.com | Support | Negative | High | System nie działa od rana, tracę klientów, proszę o natychmiastową pomoc!!! T... |
| 3 | Kasia Wiśniewska | kasia.w@example.com | Recruitment | Neutral | Low | Chciałabym aplikować na stanowisko junior developer, czy rekrutacja jest nada... |
| 4 | Marek Lewandowski | marek.l@example.com | Other | Positive | Low | Dziękuję za szybką realizację zamówienia, wszystko działa bez zarzutu. Poleca... |
| 5 | Joanna Zielińska | j.zielinska@example.com | Other | Neutral | Low | Nie mogę zalogować się do panelu od dwóch godzin, reset hasła też nie działa.... |
| 6 | Piotr Dąbrowski | p.dabrowski@example.com | Other | Neutral | Low | Interesuje mnie oferta na pakiet premium dla zespołu 20 osób. Proszę o wycenę... |
| 7 | Aleksandra Wójcik | a.wojcik@example.com | Recruitment | Neutral | Low | Czy prowadzicie rekrutację na stanowisko senior Golang developer? Mam 8 lat d... |
| 8 | Krzysztof Kamiński | k.kaminski@example.com | Support | Negative | Medium | Mam pytanie odnośnie faktury numer FV/2026/04/123 - kwota wydaje się niezgodn... |
| 9 | Magdalena Szymańska | m.szymanska@example.com | Support | Negative | High | PROSZĘ O PILNĄ POMOC! Dane klientów są widoczne publicznie po ostatniej aktua... |
| 10 | Rafał Mazur | r.mazur@example.com | Sales | Neutral | Low | Dzień dobry, chciałbym się dowiedzieć jakie są godziny waszej pracy i czy moż... |

## Zgłoszenia HIGH (wymagają natychmiastowej reakcji)

###  Tomasz Kowalczyk — Support

- **Email:** t.kowalczyk@example.com
- **Sentyment:** Negative
- **Uzasadnienie AI:** Wiadomość dotyczy awarii systemu i utraty klientów, co kwalifikuje ją jako zgłoszenie wsparcia o wysokim priorytecie z negatywnym sentymentem.

**Treść:**

> System nie działa od rana, tracę klientów, proszę o natychmiastową pomoc!!! To nie do pomyślenia.

###  Magdalena Szymańska — Support

- **Email:** m.szymanska@example.com
- **Sentyment:** Negative
- **Uzasadnienie AI:** Wiadomość dotyczy incydentu bezpieczeństwa i naruszenia RODO, gdzie dane klientów są publicznie widoczne, co wymaga pilnej interwencji.

**Treść:**

> PROSZĘ O PILNĄ POMOC! Dane klientów są widoczne publicznie po ostatniej aktualizacji, to katastrofa RODO!
