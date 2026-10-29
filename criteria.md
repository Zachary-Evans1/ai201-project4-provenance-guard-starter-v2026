# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False Positives

A false positive, where a human gets a Likely AI label, only happens in 1/10 runs on 10 different pieces human-written text.



**Why this target: This will allow for small errors while keeping a maximum 10% false-positive rate on your test set.**



---

## 2. Score Spread

Clearly Human-Written examples and clearly AI-Written examples should have a score difference of at least 0.3 in 4/5 test cases in all three trials.



**Why this target: I wanted the score separation to not be to hard or easy to reach, so 0.3 seemed like a good separation, and 4/5 in all three trials shows my model is accurate in this regard.**



---

## 3. Label Coverage

Each label will appear at least once in all three trials.



**Why this target: If each label appears once in each of the test trials, that will show that the label thresholds are reachable.**



---

## 4. The Appeal Path

An appeal will only change status to "under_review" and be recorded if the original label is `Likely AI` or `Unsure.`



**Why this target: The appeal system exists mostly for false positives, false negatives don't really need to be appealed, nor do those appeals need to be recorded.**



---

## 5. Bad input

If the text input is an empty string, contains only whitespace or punctuation, over 1000 words, or fewer than 5 words, the input will be rejected and give the user an error message in every test case.



**Why this target: This covers a lot of edge cases with user input, I choose a limit of 1000 because I've found when writing an average double spaced two page paper I use around 600-800 words, so a limit of 1000 seems reasonable.**



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
