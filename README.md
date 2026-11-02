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

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

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
