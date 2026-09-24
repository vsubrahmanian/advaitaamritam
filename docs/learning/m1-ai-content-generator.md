Great. That means **M0 → M1 is a real transition**, not just a roadmap change.

## M1 — AI Content Generator

The goal of M1 should be very specific:

> **Take a topic/source → call an LLM through an API → receive structured Jewel data → save it to Supabase.**

Your architecture becomes:

```text
                 M1
┌──────────┐
│ Python   │
│ script   │
└────┬─────┘
     │
     │ prompt + context
     ▼
┌──────────┐
│ LLM API  │
└────┬─────┘
     │
     │ structured JSON
     ▼
┌──────────┐
│ Python   │
│ validate │
└────┬─────┘
     │
     ▼
┌──────────────┐
│   Supabase   │
│    jewels    │
└──────────────┘
```

### What you'll learn in M1

I'd break M1 into **5 small milestones** rather than trying to learn everything simultaneously.

| Step     | Learn                            | Build                             |
| -------- | -------------------------------- | --------------------------------- |
| **M1.1** | Python basics for APIs           | First LLM API call                |
| **M1.2** | API keys & environment variables | Secure configuration              |
| **M1.3** | JSON / structured output         | Jewel returned as structured data |
| **M1.4** | Supabase API                     | Save Jewel automatically          |
| **M1.5** | Prompt + code separation         | Reusable Jewel generator          |

The final result should be something like:

```bash
python generate_jewel.py
```

and:

```text
Topic: Impermanence

Generating...

✓ Jewel generated
✓ Source information returned
✓ Structure validated
✓ Saved to Supabase

Jewel ID: 8f3...
Status: draft
```

---

## M1.1 — Start with the LLM API

Since you're learning AI engineering, **don't start with n8n yet**.

Use Python first.

You'll learn what is actually happening underneath an automation tool.

Your project could initially look like:

```text
advaitaamritam/
│
├── README.md
│
├── prompts/
│   └── daily-jewel.md
│
├── content/
│   └── 2026/
│
├── docs/
│   └── learning/
│       ├── m0-prompting.md
│       └── m1-api.md
│
└── src/
    └── generate_jewel.py
```

Later we'll add:

```text
src/
├── ai/
├── supabase/
├── models/
└── validation/
```

but **don't create all of that yet**.

---

## One important change from M0

In M0, you probably had ChatGPT produce something like:

```text
Title:
...

Original:
...

Translation:
...
```

For M1, we want the LLM to produce **machine-readable structured data**.

Conceptually:

```json
{
  "title": "What Remains Unchanged?",
  "original": "न जायते म्रियते वा कदाचिन्...",
  "transliteration": "...",
  "translation": "...",
  "author_speaker": "Sri Krishna",
  "source": "Bhagavad Gita",
  "source_reference": "2.20",
  "theme": "Self",
  "reflection": "...",
  "contemplation": "...",
  "image_prompt": "...",
  "status": "draft"
}
```

This is a **very important AI engineering concept**:

> Natural-language generation → structured data → application logic.

Your Python program can now inspect each field instead of trying to parse prose.

---

# M1.2 — Keep your API key out of GitHub

This is your first important security lesson.

Never do this:

```python
api_key = "sk-xxxxxxxx"
```

inside your repository.

Instead:

```text
.env
```

and:

```text
OPENAI_API_KEY=...
SUPABASE_URL=...
SUPABASE_KEY=...
```

Then put `.env` in:

```text
.gitignore
```

For example:

```gitignore
.env
__pycache__/
.venv/
```

Your GitHub repository should **never contain your actual API keys**.

---

# M1.3 — Supabase becomes your application database

You've already created the database, so M1 is where you start treating it as an actual backend rather than a spreadsheet.

Your flow becomes:

```text
Python
  │
  ├── generate Jewel
  │
  ├── validate Jewel
  │
  └── INSERT
        ↓
     Supabase
```

And your existing:

```text
status
```

becomes useful:

```text
draft
  ↓
review
  ↓
approved
  ↓
published
```

The API should initially create everything as:

```text
status = draft
```

**Never automatically publish in M1.**

Human review remains part of the pipeline.

---

# M1.4 — Your first proper experiment

Don't immediately build the whole generator.

Make your first program do just this:

```text
User enters:

"Create a Jewel about impermanence"

        ↓

Python

        ↓

LLM API

        ↓

Print response
```

Then modify it:

```text
LLM API
   ↓
structured JSON
   ↓
print fields
```

Then:

```text
LLM API
   ↓
structured JSON
   ↓
Supabase
```

That progression is important because you'll understand **each layer**, rather than ending up with a magical script you don't understand.

---

# Your M1 definition of done

I'd define M1 as complete when you can run:

```bash
python generate_jewel.py
```

and have:

```text
Input
  ↓
LLM API
  ↓
Structured Jewel
  ↓
Validation
  ↓
Supabase
```

with **zero manual copy/paste**.

The image can remain manual initially.

So M1 doesn't need:

* ❌ n8n
* ❌ RAG
* ❌ vector database
* ❌ agents
* ❌ automatic publishing
* ❌ Instagram API
* ❌ YouTube API

Those come later.

---

## Recommended M1 learning order

I'd actually teach you this **hands-on**, rather than giving you a giant course list:

**M1.1 → Make first API call**

We'll cover:

* What an API actually is
* API endpoint
* request/response
* authentication
* tokens
* Python SDK
* environment variables

**M1.2 → Structured output**

We'll take your existing `daily-jewel.md` prompt and turn it into a structured Jewel schema.

**M1.3 → Supabase**

We'll connect Python to the table you've already created.

**M1.4 → Refactor**

We'll separate:

```text
prompt
model
configuration
generation
validation
database
```

**M1.5 → GitHub**

We'll document what you learned and commit the M1 implementation.

---

### Your immediate next step

I'd start with **M1.1: your first LLM API call**, and do it on your Mac rather than using a notebook or a cloud IDE. That will teach you the fundamentals you'll reuse throughout the rest of this project.

Since you're specifically learning AI engineering, I'll keep explaining **what each piece does and why**, rather than just giving you code to copy.
