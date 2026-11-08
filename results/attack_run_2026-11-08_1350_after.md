# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 13:50
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `34b7a267-e0e3-4d5e-935a-fd1abb7f64a6` | human | 0.284 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `daeb945c-b94c-4b90-8e38-147b4afda967` | unsure | 0.000 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `0b7b6299-c389-4a5e-b827-2187127dc344` | unsure | 0.000 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `fafbfb1c-913b-4774-867b-faec859b761c` | unsure | 0.000 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `afad9789-a2dc-42fc-bb22-30ca2f4f7024` | unsure | 0.000 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `04459b4d-e7bf-4c7e-b6e6-877ace978f52` | human | 0.002 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0c8d8635-7929-4e3b-bf63-e68d4cf385c8` | ai | 0.049 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `4f80f286-45f8-4a9f-9c1d-6ccee2076c85` | human | 0.274 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `8b862cc1-ae98-4333-bb3a-b5b8312716e5` | unsure | 0.000 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c3c9adce-ae01-426f-8c26-43501b744bb5` | unsure | 0.000 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `cd74d3ec-3f5a-48b7-adac-667f2827d8c3` | unsure | 0.000 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `3954c9ae-c510-4c96-86a0-d0cc7548dc2c` | unsure | 0.000 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `0654d7b7-3459-41a6-beaf-12781a64cf06` | unsure | 0.000 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `08db3f75-d1a7-4a0c-8e4d-e9b8dfcb2d63` | unsure | 0.000 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `09cacc3b-d68f-4231-8cd0-40e02e4e2514` | unsure | 0.000 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `801d8f52-7d35-45d2-915f-7ac339948935` | unsure | 0.000 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `437b2112-a75d-480a-95ec-80c0132bdfe9` | unsure | 0.000 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `839ad511-32f8-4402-9ee3-b0af7f8ea477` | human | 0.233 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ad6df328-98df-4c6b-891b-fe9be935f489` | human | 0.090 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `cb601241-b861-437a-b517-740338259f02` | unsure | 0.000 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `712cf0e0-6d2c-491b-954c-0a1bb44e43b6` | unsure | 0.000 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `6581c556-a082-4d41-a50f-c169327cce96` | unsure | 0.000 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `182d44d4-2419-4df4-a340-90b7b8f69ee8` | unsure | 0.000 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `897e1bfb-9eca-4541-879c-19264bdc0923` | unsure | 0.000 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `e386d0e8-aa46-415f-8f14-e3a5e4c60fc1` | ai | 0.322 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `56e5ff2d-dc49-41d5-8eab-b27d0614ccb6` | human | 0.396 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6f47f403-046e-467b-8563-8560fdecea4f` | human | 0.396 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8b416d4f-ae02-46e1-886a-b87f969576a4` | human | 0.396 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5d427fe2-38a4-4fe3-b0fd-26712d0b191a` | human | 0.396 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d374845-4fda-48a3-9d72-845892471108` | human | 0.396 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2bd096a0-1186-4675-a769-4cc5e3b17c1f` | human | 0.396 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `56f019a9-57a6-472e-b302-fd16b98a65e1` | human | 0.396 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0dde0416-9223-4f55-9b9a-01db0563f958` | human | 0.396 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6d41e3e1-7523-4079-a195-335fac5e32e4` | human | 0.396 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `959cc55c-fa5b-42af-87d9-1a870ef6cc48` | human | 0.396 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "34b7a267-e0e3-4d5e-935a-fd1abb7f64a6",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2837,
  "model_score": 0.1635,
  "style_score": 0.30884066208183336,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "daeb945c-b94c-4b90-8e38-147b4afda967",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5943,
  "style_score": 0.5455944593423653,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "0b7b6299-c389-4a5e-b827-2187127dc344",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6662,
  "style_score": 0.40706162405103347,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "fafbfb1c-913b-4774-867b-faec859b761c",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6114,
  "style_score": 0.3055888575455365,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "afad9789-a2dc-42fc-bb22-30ca2f4f7024",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.3212,
  "style_score": 0.45222590079355846,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "04459b4d-e7bf-4c7e-b6e6-877ace978f52",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.0018,
  "model_score": 0.5727,
  "style_score": 0.20049047761449515,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "0c8d8635-7929-4e3b-bf63-e68d4cf385c8",
  "creator_id": "attacker_EV07",
  "guess": "ai",
  "confidence": 0.0494,
  "model_score": 0.5862,
  "style_score": 0.7213333333333334,
  "label": "We believe this text is likely generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "4f80f286-45f8-4a9f-9c1d-6ccee2076c85",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.2743,
  "model_score": 0.2452,
  "style_score": 0.2598395969294858,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "8b862cc1-ae98-4333-bb3a-b5b8312716e5",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.7042,
  "style_score": 0.248090427535156,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c3c9adce-ae01-426f-8c26-43501b744bb5",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.9792,
  "style_score": 0.4058030172934497,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "cd74d3ec-3f5a-48b7-adac-667f2827d8c3",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6175,
  "style_score": 0.29314589036712324,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "3954c9ae-c510-4c96-86a0-d0cc7548dc2c",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.7387,
  "style_score": 0.34874150665193926,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "0654d7b7-3459-41a6-beaf-12781a64cf06",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8051,
  "style_score": 0.3126349879978605,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "08db3f75-d1a7-4a0c-8e4d-e9b8dfcb2d63",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8329,
  "style_score": 0.3105668334674988,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "09cacc3b-d68f-4231-8cd0-40e02e4e2514",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8005,
  "style_score": 0.38105145772661764,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "801d8f52-7d35-45d2-915f-7ac339948935",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8814,
  "style_score": 0.29941892726080355,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "437b2112-a75d-480a-95ec-80c0132bdfe9",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8816,
  "style_score": 0.359243289638959,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "839ad511-32f8-4402-9ee3-b0af7f8ea477",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2329,
  "model_score": 0.3223,
  "style_score": 0.23261017358267924,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ad6df328-98df-4c6b-891b-fe9be935f489",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.0896,
  "model_score": 0.4625,
  "style_score": 0.22270483268849237,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "cb601241-b861-437a-b517-740338259f02",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.2044,
  "style_score": 0.5499439267700857,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "712cf0e0-6d2c-491b-954c-0a1bb44e43b6",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5943,
  "style_score": 0.5845542290292756,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "6581c556-a082-4d41-a50f-c169327cce96",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.4998,
  "style_score": 0.2853234907619428,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "182d44d4-2419-4df4-a340-90b7b8f69ee8",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.6401,
  "style_score": 0.5709853641054309,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "897e1bfb-9eca-4541-879c-19264bdc0923",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.5583,
  "style_score": 0.29346860856128715,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "e386d0e8-aa46-415f-8f14-e3a5e4c60fc1",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.3216,
  "model_score": 0.9064,
  "style_score": 0.6666666666666666,
  "label": "We believe this text is likely generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "56e5ff2d-dc49-41d5-8eab-b27d0614ccb6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "6f47f403-046e-467b-8563-8560fdecea4f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "8b416d4f-ae02-46e1-886a-b87f969576a4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "5d427fe2-38a4-4fe3-b0fd-26712d0b191a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "7d374845-4fda-48a3-9d72-845892471108",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "2bd096a0-1186-4675-a769-4cc5e3b17c1f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "56f019a9-57a6-472e-b302-fd16b98a65e1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "0dde0416-9223-4f55-9b9a-01db0563f958",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "6d41e3e1-7523-4079-a195-335fac5e32e4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "959cc55c-fa5b-42af-87d9-1a870ef6cc48",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3958,
  "model_score": 0.0287,
  "style_score": 0.3333333333333333,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
