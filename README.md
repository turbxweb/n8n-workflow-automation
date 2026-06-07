# AI Ticket Triage — Case Study

Prototyp inteligentnego systemu segregacji zgłoszeń. Odbiera dane z formularza kontaktowego, klasyfikuje je z użyciem Google Gemini 2.5 Flash (kategoria / sentyment / priorytet), zapisuje pełny rekord do lokalnego magazynu JSONL, a dla zgłoszeń o wysokim priorytecie wysyła pilny e-mail.

## Zawartość

```
.
├── workflow.json              # Eksport workflow n8n (import + użycie)
├── scripts/
│   ├── generate_report.py     # Generator raportu Markdown z JSONL
├── workflow_output/
│   ├── tickets.jsonl          # Przykładowy output z flow (wygenerowany deterministycznie)
├── reports/
│   └── report.md              # Przykładowy raport oparty o powyższy JSONL
├── README.md                  # Ten plik
└── REPORT_AI.md               # Sprawozdanie: jak wykorzystałem AI przy realizacji zadania
```

## Architektura workflow

```
Manual Trigger
  → Load Test Tickets (Code: JS) (wybrany język JS z powodu problemów z python-runnerem) dane wejściowe są zawarte w tym Node ze względu wyboru rozwiązania manual trigger
  → Process One By One (Split In Batches, batchSize=1)
  → Wait Node
    → Gemini Classify (HTTP Request, auth via Header Auth credential)
    → Parse & Merge (Code: JS — defensywny parser + walidacja enumów)
    → To JSONL Line (Code: JS — serializacja do binary)
    → Append to JSONL (Read/Write Files, append=true)
    → IF priority == "High"
        ├── true  → Send Urgent Email (SMTP)
        └── false → NoOp
    ↺ (loop back do Process One By One)
```

## Wymagania

- **n8n** ≥ 1.0 (testowane w 1.70; działa w n8n Desktop oraz self-hosted)
- **Klucz API Google Gemini**
- **Konto SMTP** — dowolne (Gmail z App Password, Mailtrap, własny serwer). Wymagane tylko w przypadku wysyłki maili dla priorytetu High; w przeciwnym razie pętla `NoOp` załatwi sprawę.
- **Zmienne środowiskowe** - opisane poniżej w kroku nr 4.

## Setup

### 1. Import workflow

W n8n: **Workflows → Import from File → `workflow.json`**.

### 2. Credential: Gemini API Key (Header Auth)

W n8n: **Credentials → New → Header Auth**. Ustaw:

- **Name:** `Gemini API Key (header: x-goog-api-key)`
- **Header Name:** `x-goog-api-key`
- **Header Value:** `<klucz z Google AI Studio>`

Następnie w node **Gemini Classify** należy wybrać tę credential z dropdownu. (W eksportowanym pliku jest placeholder `REPLACE_WITH_YOUR_CREDENTIAL_ID` — n8n poprosi o wybór credential przy pierwszym otwarciu.)

> **Uwaga bezpieczeństwa:** klucz API NIE jest przechowywany w URL ani w body node'a HTTP Request. Idzie wyłącznie przez credential n8n w headerze `x-goog-api-key`, który jest oficjalnym sposobem uwierzytelnienia Gemini API.

### 3. Credential: SMTP (opcjonalnie, tylko dla maili High)

W n8n: **Credentials → New → SMTP**. Należy wypełnić dane swojego serwera. Następnie w node **Send Urgent Email** podmienić credential.

### 4. Zmienne środowiskowe

Workflow czyta następujące zmienne (wszystkie mają fallbacki, więc działa out-of-the-box):

| Zmienna               | Domyślna wartość      | Opis                                |
| --------------------- | --------------------- | ----------------------------------- |
| `TICKETS_OUTPUT_PATH` | `/tmp/tickets.jsonl`  | Ścieżka pliku JSONL (w append mode) |
| `ALERT_FROM_EMAIL`    | `noreply@example.com` | Adres nadawcy pilnych powiadomień   |
| `ALERT_TO_EMAIL`      | `ops@example.com`     | Adres odbiorcy pilnych powiadomień  |

**Windows:** ustaw `TICKETS_OUTPUT_PATH` na coś w rodzaju `C:\<nazwa_folderu_roboczego>\tickets.jsonl`. Należy upewnić się że folder istnieje — node Read/Write Files nie tworzy katalogów sam.

**n8n Desktop:** zmienne środowiskowe ustawia się przez plik `.env` lub systemowo przed startem aplikacji.

## Uruchomienie

### A. Workflow

1. Otwórz workflow w n8n.
2. Kliknij **Execute workflow**.
3. Po zakończeniu w konsoli/loggerze powinno pojawić się 10 iteracji Gemini Classify; plik pod `$TICKETS_OUTPUT_PATH` będzie zawierał 10 linii JSONL; a 2 maile (Kowalczyk + Szymańska) powędrują na `$ALERT_TO_EMAIL`.

### B. Generowanie raportu

Przykładowe wywołanie skryptu do generowania raportu

```bash
python3 ./scripts/generate_report.py ./workflow_output/tickets.jsonl ./reports/report.md
```

Komenda zawiera ścieżkę do skryptu oraz dwa argumenty - ścieżka do pliku z outputem z workflow oraz ścieżka i nazwa pliku do zapisu raportu.

Skrypt nie ma żadnych zależności poza stdlib Pythona 3.9+.

## Potencjalne problemy

**`$env` wewnątrz wyrażeń n8n.** Dostęp do zmiennych środowiskowych w n8n Desktop wymaga włączonej opcji `N8N_SECURE_COOKIE=false` lub uruchomienia z odpowiednią flagą.
