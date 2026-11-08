# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. Submission: A user submits text and their `creator_id` through /submit
2. Validation: The application checks that the submitted text is valid and meets the requirements for an input.
3. Model Signal: The text is analyzed by the language model detector, which produces a score indicating how AI-like the model thinks the text is.
4. Style signal: The stylometry system analyzes writing characteristics, such as sentence-length variation, vocabulary diversity, and punctuation. It then combines those characteristics to give a score
5. Score Combination: The two scores are combined using weights to produce a combined score.
6. Labeling and Logging: The combined score determines whether the text is labeled human, unsure, or ai. The decision and scores are recorded in the audit log.
7. Response and Appeal: The application returns the label and scores to the user. If the label was unsure or ai, the user can submit an appeal, which is recorded in the audit log with an `under_review` status.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures: It measures the predictability of the given text by measuring how surprised an AI model is by the text with a perplexity score. It then converts that score into another score between 0 and 1, where a score closer to 1 means the text is more likely to be AI.**

**Why that might differ between human and AI writing: An AI will produce text that is not surprising to an AI. AI's tend to have specific word choices and sentence patterns, and humans tend to have different and changing writing styles, this means that human writing will "perplex" and AI more than writing by another AI.**

**What it can't see: The signal cannot see who wrote the text, only how predicable the text is to a model. A human who writes the same way an AI would could risk getting flagged.**

### Signal two — the style signal

**What it measures: It measures the spread of sentence lengths, how unique the vocabulary is, and how frequently punctuation appears relative to text length.**

**Why that might differ between human and AI writing: Humans tend to be more varied in how they write, and make more errors. An AI will be more likely to strictly follow the rules of writing. Humans on the other hand will use run-on sentences, overuse or underuse punctuation, and repeat words more often rather than changing it up.**

**What it can't see: The signal cannot see if the text was modified before hand. If I were to take an AI generated sentence and change some words, add or remove some words, and add or remove punctuation, the style signal score could change a lot, without changing the meaning of the text.**

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule: A weighted average between the two scores with a weight of 0.6 for the style signal and a weight of 0.4 for the model signal**

**The numbers: combined = config.WEIGHT_MODEL_SIGNAL(0.4) * model_score + config.WEIGHT_STYLE_SIGNAL(0.6) * style_score.**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

The Case: "Everyone knows what a tree is: a large woody thing that provides shade. Oaks, pines and similarly large majestic trees probably come immediately to mind. A stricter, botanical definition is that a tree is any plant with a self-supporting, perennial woody stem (i.e. living for more than one year). The first question that normally comes back at this point is to ask what then is a shrub? To horticulturalists, a ‘tree’ is defined as having a single stem more than 6 m (20 ft) tall, which branches at some distance above ground, whereas a shrub has multiple stems from the ground and is less than 6 m tall. This is a convenient definition for those writing tree identification books who wish to limit the number of species they must include. In this book, however, shrubs are thought of as being just small trees since they work in exactly the same way as their bigger neighbours. Thus, ‘trees’ cover the towering giants over 100 m through to the little sprawling alpine willows no more than a few centimetres tall." 

The Scores: 
sentence_length_spread   0.33221756618380066
type_token_ratio         0.6666666666666666
punctuation_density      0.2777777777777778
style_signal             0.4262978483091035   (higher = more likely AI)

perplexity     33.4
model_signal   0.6165   (higher = more likely AI)

What my rule does: The score will take the spilt into account with the weight I choose, which favors the style signal score. It will multiply the style score by 0.6 and the model score by 0.4, then add them together.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 <= score <= 0.35 | We believe this text is likely written by a human. |
| unsure | 0.35 < score < 0.65 | We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect. |
| high-confidence AI | 0.65 <= score <= 1.00 | We believe this text is likely generated by an AI. You may submit an appeal for review if you believe this result is incorrect. |

**Why I worded the "unsure" one this way: I worded unsure this way because it does not accuse the user. It instead is telling them the system isn't confident enough to determine the origin of the text, and tells them they can appeal if they believe the result is incorrect.**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
curl -X POST http://127.0.0.1:5000/submit ` -H "Content-Type: application/json" `
>>   -d '{"text":"Everyone knows what a tree is: a large woody thing that provides shade. Oaks, pines and similarly large majestic trees probably come immediately to mind. A stricter, botanical definition is that a tree is any plant with a self-supporting, perennial woody stem. The first question that normally comes back at this point is to ask what then is a shrub? To horticulturalists, a tree is defined as having a single stem more than 6 m tall, whereas a shrub has multiple stems from the ground and is less than 6 m tall. This is a convenient definition for those writing tree identification books who wish to limit the number of species they must include. In this book, however, shrubs are thought of as being just small trees since they work in exactly the same way as their bigger neighbours.","creator_id":"test-user"}'                                                                                                                                                    
```

```json
{                                  
  "combined_score": 0.5569310052910053,
  "confidence": 0.0,
  "content_id": "dc32a951-9ede-4520-a376-07bb497ea5d2",
  "guess": "unsure",
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "model_score": 0.6791,
  "style_score": 0.47548500881834216
}
```

**An appeal**

```bash
curl -X POST http://127.0.0.1:5000/appeal `
>>   -H "Content-Type: application/json" `
>>   -d '{"content_id":"dc32a951-9ede-4520-a376-07bb497ea5d2","reasoning":"I believe this text was incorrectly classified. I wrote it myself and would like the decision reviewed."}'
```

```json
{
  "content_id": "dc32a951-9ede-4520-a376-07bb497ea5d2",
  "message": "Your appeal has been received and is under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.5569310052910053,
      "content_id": "dc32a951-9ede-4520-a376-07bb497ea5d2",
      "creator_id": "test-user",
      "guess": "unsure",
      "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
      "model_score": 0.6791,
      "status": "decided",
      "style_score": 0.47548500881834216,
      "timestamp": "2026-11-02T01:20:08+00:00"
    },
    {
      "content_id": "dc32a951-9ede-4520-a376-07bb497ea5d2",
      "creator_id": "test-user",
      "event": "appeal",
      "reasoning": "I believe this text was incorrectly classified. I wrote it myself and would like the decision reviewed.",
      "status": "under_review",
      "timestamp": "2026-11-02T01:20:54+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for: Help reviewing my label thresholds and the score_to_label() function with ChatGPT*
- *What came back: Feedback about overlapping score boundaries and how to make the three label ranges distinct.*
- *What I changed: It originally did not include 0.35 in the human classification, but I had to change that when I moved to working on scoring.py.*

**Moment 2**

- *What I asked for: Help implementing my submit endpoint.*
- *What came back: Claude generated a working submit endpoint both times I asked it too.*
- *What I changed: Claude Code initially generated placeholder scoring logic because I had not implemented the scoring functions yet. I later replaced that placeholder with this:  `guess, label_text = scoring.score_to_label(combined_score)` once I had implemented the scoring logic. I then tested the code to make sure all the labels were reachable, they were.*

**Moment 3**

- *What I asked for: Help diagnosing the criterion 2 and 3 misses and choosing one improvement.*
- *What came back: Claude read the scoring code, measured the style components of the sample texts, and suggested a windowed type-token ratio.*
- *What I changed: I Implemented claude's change and tested the attacks and criteria again, it did not fix anything, and let one more attack through.*

**Moment 4**

- *What I asked for: Help writing scenarios for my five criteria, including the inputs each one needed.*
- *What came back: Claude wrote five AI-style sample paragraphs, a borderline text drawn from my README, and placeholder slots for my own writing*
- *What I changed: I added my own writing to the placeholder slots claude provided and kept the other samples as they were. I tested the 4th criteria by hand after each run.*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others: Ten submissions per minute gives a real writer enough room to submit several pieces without getting blocked, but will block a script that rapidly tries to overwhelm the system with requests. Two hundred submission per day provides some protection against sustained attacks while still not limiting a real person that much.**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as: The current rate limit key function uses the submitted creator_id when it is valid. Otherwise it falls back to a users IP address to block requests.** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 200
  [ 7/15] 200
  [ 8/15] 200
  [ 9/15] 200
  [10/15] 200
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
============================================================
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->


| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `4cabea86-4aae-4c33-9ac6-28bda12cfdee` | human | 0.247 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f38c62dd-fd4b-4b44-bc1e-41e78a88af99` | unsure | 0.000 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `2f45f55e-3df5-4938-851e-e1644ed8fabf` | unsure | 0.000 |  HELD|
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `bfe39c3b-e027-418c-acad-16f6b41c2449` | unsure | 0.000 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `243ea951-52ea-4593-a2fa-ae75e1c3b21a` | unsure | 0.000 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d9da3c05-5973-424c-a414-8c1bc924871f` | unsure | 0.000 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `396532b2-1893-49c0-ae65-7a71af03225b` | ai | 0.085 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `9007548c-1531-4e8b-b119-311956612d44` | human | 0.274 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `2e664b58-d9fe-4f1c-8650-92bfbfca96e2` | unsure | 0.000 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `af2ff0fd-ca49-46d9-96d9-7dba5b7f8f46` | ai | 0.060 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4898f25f-5ce3-4e24-b3d6-cf3c7c055162` | unsure | 0.000 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `f45c845d-412f-415e-9b79-e33eedbd6795` | unsure | 0.000 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8fa8c2e1-6ff2-4c07-b971-f12fff5575b4` | unsure | 0.000 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `50bf88ea-9ec0-48ae-b0cb-dcf8f5185548` | unsure | 0.000 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `a402813d-88ec-48fe-80bf-8d014dcac70f` | unsure | 0.000 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `aaf3e8d0-cbcf-4d46-9a39-92c418ae1f58` | unsure | 0.000 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a80813aa-04af-4e4b-8c74-d1f1d3e4f9e4` | unsure | 0.000 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `41cc9ce6-aa2d-4adb-b026-c3ab750cef5f` | human | 0.233 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `8e5d3add-418b-44cb-8dfe-85289f543a08` | human | 0.090 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `4c75db32-358b-4d39-a590-e3ff4211e94f` | unsure | 0.000 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b5fec01a-867d-4805-aee3-a2e84bd10db2` | unsure | 0.000 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `19b38d03-4584-40ba-81cf-51c4e77c7fa2` | unsure | 0.000 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `fa3a24d2-56d4-4328-9a9c-532d5ff8d43b` | unsure | 0.000 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `faf822f5-c418-4cf8-9d1b-0311b3ac8cec` | unsure | 0.000 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  HELD|
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `7ccd2694-572f-48f1-9e15-a31712f14411` | ai | 0.322 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5e7d1b6c-da5d-417b-b820-8789c52763cf` | human | 0.396 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `802fb2c6-0afe-40ca-bacd-d1edaef3964c` | human | 0.396 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dd19a792-91a2-4ba3-a6a3-9d8fc1633f7f` | human | 0.396 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ad6c3e0a-70e2-4b26-86e7-90f3fc9c7e50` | human | 0.396 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9d0f558e-3f56-4f0e-981b-79f6991f6af3` | human | 0.396 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a1ac8c30-f761-4834-806e-e4b818cf534f` | human | 0.396 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ad6113ad-f0ab-4732-9825-45008475d09e` | human | 0.396 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a027a005-9d25-46eb-9fac-e1727de2aaa9` | human | 0.396 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `78b71404-fb50-43fc-95de-248b5452d248` | human | 0.396 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3ce477f4-168f-4121-8f1b-cd43be020abb` | human | 0.396 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

`flood_same_creator` - 429 after the tenth run, so my rate limit worked.

So 52/56 Held and 4/56 Broke

4 that broke: EV01, EV08, MF07 and RQ07

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "4cabea86-4aae-4c33-9ac6-28bda12cfdee",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.2469,
  "model_score": 0.1635,
  "style_score": 0.3303112503171275,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}

{
  "id": "EV08",
  "status": 200,
  "content_id": "9007548c-1531-4e8b-b119-311956612d44",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.2743,
  "model_score": 0.2452,
  "style_score": 0.2598395969294858,
  "label": "We believe this text is likely written by a human.",
  "error": null,
  "verdict": ""
}

{
  "id": "MF07",
  "status": 200,
  "content_id": "7ccd2694-572f-48f1-9e15-a31712f14411",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.3216,
  "model_score": 0.9064,
  "style_score": 0.6666666666666666,
  "label": "We believe this text is likely generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}

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

{
  "id": "FP03",
  "status": 200,
  "content_id": "8fa8c2e1-6ff2-4c07-b971-f12fff5575b4",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8051,
  "style_score": 0.34333779924284036,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}

{
  "id": "FP04",
  "status": 200,
  "content_id": "50bf88ea-9ec0-48ae-b0cb-dcf8f5185548",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.8329,
  "style_score": 0.3076256569969106,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}

{
  "id": "EV07",
  "status": 200,
  "content_id": "396532b2-1893-49c0-ae65-7a71af03225b",
  "creator_id": "attacker_EV07",
  "guess": "ai",
  "confidence": 0.0853,
  "model_score": 0.5862,
  "style_score": 0.7422680412371134,
  "label": "We believe this text is likely generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}

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

{
  "id": "EV05",
  "status": 200,
  "content_id": "243ea951-52ea-4593-a2fa-ae75e1c3b21a",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.0,
  "model_score": 0.3212,
  "style_score": 0.479461673151282,
  "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
  "error": null,
  "verdict": ""
}

{
  "id": "PI01",
  "status": 200,
  "content_id": "8e5d3add-418b-44cb-8dfe-85289f543a08",
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

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it: 

The worst outcome for my run in my opinion is RQ07. No false positive broke, none were labeled as AI, just unsure. MF07 might be a false positive, but this tester is meant for english text, so I'm not counting it. The worst outcome then is RQ07 it's the only attack that caused an error, meaning its probably the most dangerous attack to my system.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False Positives | <=2/10 are labeled AI | 0/10 | 0/10 | 0/10 | MET |
| 2. Score Spread | Clearly AI has a 0.3 difference from a clearly human example | 0/5 | 0/5 | 0/5 | MISSED |
| 3. Label Coverage | 1 Label from each category | 3 unsure | 3 unsure | 3 unsure | MISSED |
| 4. The Appeal Path | An appeal will only change status to "under_review" and be recorded if the original label is `Likely AI` or `Unsure.` | 3/3 | 3/3 | 3/3 | MET |
| 5. Bad input | Bad inputs get rejected and give the user an error message | 6/6 | 6/6 | 6/6 | MET |

Criterion 4 was tested by hand, not by scenarios.py. I did 3 appeals for each category, human, unsure, and AI so 3 tests per trial.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.7924,
    "style_score": 0.37973095405985485,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "People with physical disabilities and chronic illnesses are a very div"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.7788,
    "style_score": 0.35451327301408453,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "Physical disabilities and chronic illnesses differ from other groups o"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.8312,
    "style_score": 0.40595236731036954,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "One thing that makes this different from working with other cultural g"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.7963,
    "style_score": 0.38771352714523594,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "Overall, people with physical disabilities and chronic illnesses face "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.6819,
    "style_score": 0.3473794127812938,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "As we age, many changes happen in our lives, some good and some challe"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.7906,
    "style_score": 0.31237371350406284,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "The first mental health challenge that comes with age is isolation. As"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.8117,
    "style_score": 0.38056378605028296,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "The second mental health problem that can come with age is a person\u2019s "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.5713,
    "style_score": 0.3350310682229024,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "Medical workers cannot solve or fix the issues I\u2019ve brought up, but th"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.6105,
    "style_score": 0.32851106081931636,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "In conclusion, getting older can come with difficulties for a person\u2019s"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.0,
    "model_score": 0.6735,
    "style_score": 0.334741795239767,
    "label": "We are not confident enough to determine whether this text was written by a person or generated by an AI. You may submit an appeal for review if you believe this result is incorrect.",
    "sent": "The Yale School of Art website is a website that has an unconventional"
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

Criterion 2: Score Spread, Clearly AI has a 0.3 difference from a clearly human example
Stage: Signal one and Signal two
Diagnosis: My AI samples are shorter than my human samples, also, I used more formal writing from school assignments for my human samples, which is leading to both groups, human and AI text, to get a low perplexity score. The length of the samples matters because type_token_ratio rises as text get shorter, so the AI samples look more varied by default

Criterion 3: Label Coverage, 1 Label from each category
Stage: Signal one and Signal two
Diagnosis: Every input landed in unsure (0.35–0.65), so neither high-confidence label was reached. The model signal put every test at 0.65-0.82, which means the model predicted all three texts closer AI. The style signal put them at 0.31–0.42, which puts all three texts closer to Human. As the combination score is 0.4/0.6 the difference in the two signal scores for each run pulled all three tests towards the middle.

EV01:
Stage: Signal two
Diagnosis: The typos were meant to trick the system to label it human by rasing word variety. This happened with my system, the type-token ratio score was high, so it ended up with a style score of 0.33 which led to the combined score being less than the human threshold.

EV08:
Stage: Signal 2
Diagnosis: The text is 10 words in two sentences, so there's too little context for the signal to read reliably. The type-token ratio was 1.0, which pulled the style score heavily towards human.

MF07
Stage: Signal two
Diagnosis: The Arabic text was labeled AI. In `stylometry.py::words`, the regex `[a-z0-9']+` matches no Arabic characters, so the text produces zero words. `type_token_ratio` returns 0 for an empty word list, and the style signal reads that as complete repetition, which pushes toward AI. `sentence_length_spread` also returns 0 for a single sentence, which reads as uniform sentences, also toward AI. Together the style score is 0.667, and with the 0.6 weight the combined score is at least 0.40 before the model signal is added. The validation in `app.py::submit` only checks that the text is a string with letters or digits, so it lets this input through.

RQ07
Stage: Route
Diagnosis: The route checks the field types but never checks that the body is a dict, this causes payload.get("text") to fail when presented with a json array instead of text, leading to a 500 error.

---

## The Improvement

**What I changed: I changed the `type_token_ratio` function in `stylometry.py`. I changed the function to not count overall unique words over the total words, but the ratio over a 50-word sliding window instead. This takes away the benefit that smaller texts had over longer texts, so now the messages are more equal in their scoring. If the text is under 50 words, the old ratio still is used.**

**Which diagnosis pointed at it: Both Criterion 2 and 3, but more at Criterion 3.**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

From my count I got this score:
| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `34b7a267-e0e3-4d5e-935a-fd1abb7f64a6` | human | 0.284 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `daeb945c-b94c-4b90-8e38-147b4afda967` | unsure | 0.000 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `0b7b6299-c389-4a5e-b827-2187127dc344` | unsure | 0.000 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `fafbfb1c-913b-4774-867b-faec859b761c` | unsure | 0.000 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `afad9789-a2dc-42fc-bb22-30ca2f4f7024` | unsure | 0.000 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `04459b4d-e7bf-4c7e-b6e6-877ace978f52` | human | 0.002 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0c8d8635-7929-4e3b-bf63-e68d4cf385c8` | ai | 0.049 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `4f80f286-45f8-4a9f-9c1d-6ccee2076c85` | human | 0.274 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `8b862cc1-ae98-4333-bb3a-b5b8312716e5` | unsure | 0.000 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c3c9adce-ae01-426f-8c26-43501b744bb5` | unsure | 0.000 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `cd74d3ec-3f5a-48b7-adac-667f2827d8c3` | unsure | 0.000 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `3954c9ae-c510-4c96-86a0-d0cc7548dc2c` | unsure | 0.000 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `0654d7b7-3459-41a6-beaf-12781a64cf06` | unsure | 0.000 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `08db3f75-d1a7-4a0c-8e4d-e9b8dfcb2d63` | unsure | 0.000 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `09cacc3b-d68f-4231-8cd0-40e02e4e2514` | unsure | 0.000 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `801d8f52-7d35-45d2-915f-7ac339948935` | unsure | 0.000 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `437b2112-a75d-480a-95ec-80c0132bdfe9` | unsure | 0.000 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `839ad511-32f8-4402-9ee3-b0af7f8ea477` | human | 0.233 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ad6df328-98df-4c6b-891b-fe9be935f489` | human | 0.090 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `cb601241-b861-437a-b517-740338259f02` | unsure | 0.000 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `712cf0e0-6d2c-491b-954c-0a1bb44e43b6` | unsure | 0.000 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `6581c556-a082-4d41-a50f-c169327cce96` | unsure | 0.000 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `182d44d4-2419-4df4-a340-90b7b8f69ee8` | unsure | 0.000 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `897e1bfb-9eca-4541-879c-19264bdc0923` | unsure | 0.000 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `e386d0e8-aa46-415f-8f14-e3a5e4c60fc1` | ai | 0.322 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `56e5ff2d-dc49-41d5-8eab-b27d0614ccb6` | human | 0.396 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6f47f403-046e-467b-8563-8560fdecea4f` | human | 0.396 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8b416d4f-ae02-46e1-886a-b87f969576a4` | human | 0.396 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5d427fe2-38a4-4fe3-b0fd-26712d0b191a` | human | 0.396 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d374845-4fda-48a3-9d72-845892471108` | human | 0.396 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2bd096a0-1186-4675-a769-4cc5e3b17c1f` | human | 0.396 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `56f019a9-57a6-472e-b302-fd16b98a65e1` | human | 0.396 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0dde0416-9223-4f55-9b9a-01db0563f958` | human | 0.396 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6d41e3e1-7523-4079-a195-335fac5e32e4` | human | 0.396 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `959cc55c-fa5b-42af-87d9-1a870ef6cc48` | human | 0.396 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

`flood_same_creator` - 429 after the tenth run, so my rate limit worked.

So 51/56 Held and 5/56 Broke

5 that broke: EV01, EV06, EV08, MF07 and RQ07

1 more broke than last time.

## Run Log and Verdicts After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False Positives | <=2/10 are labeled AI | 0/10 | 0/10 | 0/10 | MET |
| 2. Score Spread | Clearly AI has a 0.3 difference from a clearly human example | 0/5 | 0/5 | 0/5 | MISSED |
| 3. Label Coverage | 1 Label from each category | 3 unsure | 3 unsure | 3 unsure | MISSED |
| 4. The Appeal Path | An appeal will only change status to "under_review" and be recorded if the original label is `Likely AI` or `Unsure.` | 3/3 | 3/3 | 3/3 | MET |
| 5. Bad input | Bad inputs get rejected and give the user an error message | 6/6 | 6/6 | 6/6 | MET |

Criteria 4 was tested by hand again, as it was in the first run log

**Did it help, and how do I know: No, it made it very slightly worse. I know because the Run Log did not change at all, and with the attacks one less attack was held back.**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

     Criterion 2: The main fix would be changing the human sample examples, I took them from my own assignments, which means that the writing in them was more formal, it would be better to find some actual examples that are written in a less formal matter. I didn't make it in this unit because the tests are meant to go against the same set of examples, so I didn't feel comfortable changing them.

     Criterion 3: The fix is a wider signal range, which would be a redesign of the scoring system. I didn't make it in this unit because the milestone allowed one change.
     
     RQ07: The fix is to check if the body is a dict in pp.py::submit before reading any fields. I didn't make it in this unit because the milestone allowed one change. It would probably be the next change I made

     MF07: The fix is a Unicode-aware word regex in stylometry.py::words, such as \w+. I didn't make it in this unit because the milestone allowed one change.

     EV01: The fix would be to correct or normalize spelling before counting unique words, or to flag text with many unknown words as too unreliable to score. I didn't make it in this unit because the milestone allowed one change.

     EV06: This broke only in the after run. The window I added to type_token_ratio pushed it over the edge into human. The fix would be to cap the spread or ignore one-word sentences.  I didn't make it in this unit because the milestone allowed one change.

     EV08: The fix is a higher minimum length for scoring. I chose 5, which let this one get through. I didn't make it in this unit because the milestone allowed one change.



**The trade I'd make if this ran for real: I'd keep false positives low, even though it would let more AI text through as unsure. A wrongly accused writer loses more than the website does for AI text that gets passed as human. The readers would pay the most for it, as they get no real signal whether something is AI or not from an unsure. The writers most likely to get labeled as unsure were formal writers or ESL writers.**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
