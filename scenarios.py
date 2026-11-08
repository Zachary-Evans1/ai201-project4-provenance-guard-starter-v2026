"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.

Criterion numbers match criteria.md: 1 false positives, 2 score spread,
3 label coverage, 4 appeal path, 5 bad input.
"""

# ── Your own writing ─────────────────────────────────────────────────────────
# Criterion 1 is meaningless with anyone else's prose, so these ten slots are
# yours to fill. Paste ten pieces you actually wrote — essays, emails, posts,
# notes, anything human. Each should be 5 to 1000 words (criterion 5's limits).
# The first five double as the "clearly human" side of criterion 2.
MY_WRITING = [
    "People with physical disabilities and chronic illnesses are a very diverse group, with many different experiences. For some it is openly visible to everyone around them, while with others, the disability is not visible. Their support structures can also differ, some may have to deal with their problems alone, while others have family and friends to help them through it. Society expects people to be constantly productive and independent, which for a person with a physical disability or chronic illness may be difficult or impossible.",
    "Physical disabilities and chronic illnesses differ from other groups of diversity for many reasons. First, physical disabilities and chronic illnesses can directly affect a person's abilities to complete everyday activities. While being part of a certain race, gender, or sexuality can expose someone to oppression and discrimination, physical disabilities and chronic illnesses can also directly affect a person's physical abilities, energy levels, or capacity to complete everyday tasks. Another difference is that disabilities and chronic illnesses are not always visible. A person with an invisible disability or illness might be judged by others because their symptoms cannot be seen. This can lead to them having to argue or justify why they need accommodations. The final difference I’m going to talk about is limited energy and changing needs. Some people with physical disabilities or chronic illnesses may experience reduced energy or fatigue. This can lead them to having to prioritize work, medical appointments, and any other daily responsibilities over rest and leisure, potentially affecting their well-being.",
    "One thing that makes this different from working with other cultural groups is that software developers need to consider how a person's abilities can affect their direct interaction with software. For example, when designing software for people from different cultural backgrounds, a developer may need to consider language options and how information is presented. When designing for someone with a physical disability or chronic illness, they also need to focus on how a person will be able to interact with software. Developers can make things easier and harder for those with physical disabilities and chronic illnesses. One way they can make things harder is to assume that everyone will interact with a system in the same way. They may design software that requires people to see, hear, or move in ways that some users may struggle with or be unable to do. Developers can make things easier as well by developing accessibility features. These can include things like making software work with screen readers, closed captions or transcripts for videos, providing text alternatives for images, avoiding relying on color alone to portray meaning, and other options like text size and high-contrast modes. The main thing software developers need to keep in mind is that not every person will interact with a system the same way and that developers need to be willing to design with those differences in mind.",
    "Overall, people with physical disabilities and chronic illnesses face challenges that I and others may not always understand or be able to recognize. Compared to other diverse groups, their needs may differ in many ways. Things like invisible symptoms can make it difficult for people to understand that a person might need accommodation. As a future software engineer, I think it is important to remember that not everyone will interact with what I develop in the same way. When creating software, I need to make sure to consider accessibility and communicating with people from these communities to make sure what I develop is usable by as many people as possible. I think that software developers and society as a whole need to be more aware of physical disabilities and chronic illnesses and the hardships that may come with them.",
    "As we age, many changes happen in our lives, some good and some challenging. Some of these challenges involve mental health concerns. While I am not an older individual, I can understand the changes that can happen later in a person’s life. Things like losing your friends and loved ones and declining physical health are just two of the many challenges getting older can bring to a person’s mental health. I would like to cover these challenges, and how health professionals can help patients manage these concerns.",
    "The first mental health challenge that comes with age is isolation. As people get older, their friends and family of a similar age will unfortunately pass away, while their children or younger friends will have their own lives to live. This can lead to feelings of isolation and grief. Some older people will also end up in nursing homes, which can make them feel more isolated from those they are close to, but can also help them make new connections with their peers. Losing someone you’ve known for your whole life can be damaging to mental health, and an older person may have to go through multiple losses close together, sometimes without anyone close to them to help them grieve. Without adequate support, a person's mental health may continue to decline.",
    "The second mental health problem that can come with age is a person’s declining physical health. We learned last week how disabilities can affect mental health, and some disabilities are more common with age, such as mobility difficulties, chronic pain, or worsening eyesight. Losing physical abilities can make a person feel like they are losing their independence. They may need a walker or wheelchair to move around, glasses to see, or a doctor to help manage their pain. All these things can make a person feel they are less independent than they used to be. For some, this can have a heavy emotional impact and potentially contribute to disorders like depression. These changes can also make it harder for older adults to participate in social activities, which may further contribute to feelings of isolation.",
    "Medical workers cannot solve or fix the issues I’ve brought up, but they can work to help a client manage the outcomes. Medical professionals can encourage older individuals to maintain social connections and point them to resources like their area's senior center. If in a nursing home, the staff can hold events for groups to get everyone socializing. To help cope with grief, they can listen to a patient and be empathetic and offer emotional support. To help them adapt to physical limitations and help preserve their independence, medical workers can find mobility aids, such as walkers or wheelchairs, make recommendations that could help improve accessibility at a client’s home, help the client find alternative ways to enjoy hobbies they feel they can no longer enjoy the way they used to, and encourage them to maintain as much independence as their circumstances allow. This can be done by including patients in decisions about their care whenever possible, allowing them to make choices for themselves even if they need assistance, and for healthcare workers to avoid doing everything for a patient just because it’s simpler or faster. Doing even a few of these suggestions can help make an older individual’s time in the healthcare system more positive.",
    "In conclusion, getting older can come with difficulties for a person’s mental health. They can lose close friends and loved ones or find that surviving friends and family members are too busy to meet often. They can also experience declining physical health, which can make them feel less independent, and may prevent them from doing past activities they enjoyed. Healthcare workers should take these into account and try to help their patients work through these challenges to hopefully help improve their mental health and give them a more positive experience in the healthcare system.",
    "The Yale School of Art website is a website that has an unconventional design. The website’s main purpose is to be a university website for the Yale School of Art, including information about the school, applications, programs, resources for students, and information about the faculty and staff.",
]

# ── Clearly AI-written samples ───────────────────────────────────────────────
# Written to read like typical generic model output: balanced, formal, heavy on
# transition words, no personal detail. Used for criteria 2 and 3.
AI_SAMPLES = [
    "In today's fast-paced digital landscape, effective communication has become more important than ever. Organizations must navigate a complex array of channels, audiences, and expectations. By prioritizing clarity, consistency, and empathy, teams can build stronger relationships with their stakeholders. Moreover, leveraging data-driven insights allows leaders to make informed decisions that align with long-term strategic goals. Ultimately, a thoughtful approach to communication fosters trust and drives sustainable growth across the organization.",
    "Renewable energy represents a transformative opportunity for communities worldwide. Solar, wind, and hydroelectric power offer sustainable alternatives to traditional fossil fuels, while simultaneously reducing greenhouse gas emissions. Furthermore, the decreasing cost of these technologies has made them increasingly accessible to both developed and developing nations. It is important to recognize, however, that successful implementation requires robust infrastructure, supportive policy frameworks, and meaningful public engagement.",
    "Time management is a crucial skill for achieving both personal and professional success. By setting clear priorities, breaking large tasks into manageable steps, and minimizing unnecessary distractions, individuals can significantly enhance their productivity. Additionally, establishing consistent routines helps create a sense of balance and reduces stress. Ultimately, mastering time management empowers people to focus on what matters most and to pursue their goals with greater confidence and purpose.",
    "The benefits of regular exercise extend far beyond physical fitness. Research consistently demonstrates that physical activity improves cardiovascular health, enhances mood, and supports cognitive function. Moreover, incorporating movement into daily life does not require expensive equipment or specialized facilities. Whether through walking, swimming, or structured workouts, individuals can tailor their routines to suit their preferences and needs. Ultimately, a commitment to regular activity contributes to a healthier and more fulfilling life.",
    "Effective leadership is grounded in a combination of vision, integrity, and adaptability. Leaders who communicate a compelling direction inspire their teams to pursue shared objectives with enthusiasm. Furthermore, a commitment to ethical conduct builds the trust necessary for collaboration to flourish. In an ever-changing environment, the ability to adapt strategies in response to new information is equally essential. Ultimately, leadership is less about authority and more about cultivating the conditions in which others can thrive.",
]

# ── Borderline sample ────────────────────────────────────────────────────────
# The tree passage from the README's "split" case. It's a third-party text, not
# a sample of yours or of AI output — it's here because its combined score
# landed in the unsure band earlier, which is what criterion 3 needs.
BORDERLINE = (
    "Everyone knows what a tree is: a large woody thing that provides shade. "
    "Oaks, pines and similarly large majestic trees probably come immediately to mind. "
    "A stricter, botanical definition is that a tree is any plant with a self-supporting, "
    "perennial woody stem (i.e. living for more than one year). The first question that "
    "normally comes back at this point is to ask what then is a shrub? To horticulturalists, "
    "a 'tree' is defined as having a single stem more than 6 m (20 ft) tall, which branches "
    "at some distance above ground, whereas a shrub has multiple stems from the ground and is "
    "less than 6 m tall. This is a convenient definition for those writing tree identification "
    "books who wish to limit the number of species they must include. In this book, however, "
    "shrubs are thought of as being just small trees since they work in exactly the same way "
    "as their bigger neighbours. Thus, 'trees' cover the towering giants over 100 m through to "
    "the little sprawling alpine willows no more than a few centimetres tall."
)


SCENARIOS = [
    {
        # Criterion 1 — target: at most 2 of 10 human pieces labelled AI.
        "name": "my own writing",
        "criterion": 1,
        "texts": MY_WRITING,
    },
    {
        # Criterion 2 — target: clearly-AI vs clearly-human differ by >= 0.3 in
        # 4 of 5 pairs, in all three trials. Pairs are AI_SAMPLES[i] with
        # MY_WRITING[i]; the 0.3 gap is judged on combined_score from the
        # responses. The human side is YOUR writing, so fill MY_WRITING first.
        "name": "score spread",
        "criterion": 2,
        "texts": AI_SAMPLES + MY_WRITING[:5],
    },
    {
        # Criterion 3 — target: every label (human, unsure, AI) appears at least
        # once in each trial. Three texts spread across the score range, one
        # per expected label.
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            AI_SAMPLES[0],     # expected: high-confidence AI
            MY_WRITING[0],     # expected: high-confidence human (once filled)
            BORDERLINE,        # expected: unsure
        ],
    },
    # Criterion 4 — the appeal path is NOT a scenario here. run_eval.py only
    # sends /submit, and the appeal needs a content_id from a real submission.
    # Test it by hand against /appeal: submit an AI-labelled text and a
    # human-labelled text, appeal each, and check the status and audit log.
    # Say in the write-up that you did it this way.
    {
        # Criterion 5 — target: every bad input rejected with an error message,
        # in every test case. Each body is a whole request, sent as written.
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t   ", "creator_id": "eval_bad_whitespace"},
            {"text": "!!! ... ??? --- ;;; ***", "creator_id": "eval_bad_punct"},
            {"text": "This is too short", "creator_id": "eval_bad_four_words"},
            {"text": "word " * 1001, "creator_id": "eval_bad_1001_words"},
            {"creator_id": "eval_bad_missing"},  # no text field at all
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
