# Agentic AI Use Case Evaluation Rubric

Supporting data for the post *Choosing an AI use case? AI Hammer or Nail?*.

Seventeen commonly cited agentic AI use cases, scored against the same attribute
set under two deliberately different weighting schemes. The point of the exercise
is that the two weightings produce nearly opposite rankings, which means a
published "top use cases" list is mostly a readout of whoever chose the weights.

## Supporting data (referenced by the post)

| File | What it is |
| --- | --- |
| [Most Cited Use Cases - Agentic AI.md](Most%20Cited%20Use%20Cases%20-%20Agentic%20AI.md) | The 20 use cases pulled from the usual roundups, with the vendors and stats each one is usually cited with. 17 were carried forward as distinct enough to score. |
| [Use Case Attributes.md](Use%20Case%20Attributes.md) | The raw attribute list — what makes a task agent-friendly, before any weighting. |
| [Use Case Attributes Weighted for Operational Efficiency.md](Use%20Case%20Attributes%20Weighted%20for%20Operational%20Efficiency.md) | The ×3 / ×2 / ×1 scheme, built for speed to deployment and measurable cost reduction. |
| [Use Case Analysis Pass 1.md](Use%20Case%20Analysis%20Pass%201.md) | Scored grid under the operational efficiency weighting. This is the post's "the answer I expected" table. |
| [Use Case Attributes Weighted for Cognitive Complexity.md](Use%20Case%20Attributes%20Weighted%20for%20Cognitive%20Complexity.md) | The five-tier ×6 → ×1 scheme, plus the reasoning for why the efficiency weighting had to be rebuilt. |
| [Use Case Analysis Pass 2.md](Use%20Case%20Analysis%20Pass%202.md) | Scored grid under the cognitive complexity weighting, plus the comparison against internet consensus. |
| [verify_scores.py](verify_scores.py) | Checks that every row total equals the sum of its attribute columns. |

## How the pieces line up

Two counts look inconsistent at first glance, so both are worth stating plainly.

**20 use cases cited, 17 scored.** Three from
[Most Cited Use Cases - Agentic AI.md](Most%20Cited%20Use%20Cases%20-%20Agentic%20AI.md) were
dropped as too overlapping or too thin to score separately: data-analyst agents,
insurance claims and underwriting, and scientific / drug-discovery research loops.

**20 attributes listed, 15 and 17 scored.** `Use Case Attributes.md` is the raw
vocabulary, written before any scoring. The operational efficiency weighting consolidates it to 15 scored
attributes, bundling related items into one column — data volume, multi-source,
quantifiable, freshness, structure and consistency all collapse into a single
input-data attribute, for instance. The cognitive complexity weighting restructures the same ground into
17 attributes across five tiers and adds concerns the first list didn't separate,
notably tool integration and problem decomposition. So the column counts in the
two scored grids (15 and 17) are deliberate, and neither equals the raw list.

## Scoring method

Each use case is scored against each attribute on a three-point scale:

- **True (1)** — the use case clearly has the attribute
- **Somewhat (0)** — mixed or ambiguous
- **False (-1)** — the use case lacks it

Each score is multiplied by its attribute's weight and the row is summed. Within a
single pass, the ordering is meaningful. **Across passes it is not** — the two
weightings use different attributes, multipliers, and maximums, so only the
relative ranking can be compared, never the raw totals.

## Results

Operational efficiency weighting (top 3 of 17): customer support 29, finance
operations 28, IT service desk 27. Software engineering agents place 12th at 1.

Cognitive complexity weighting (top 3 of 17): IT service desk 52, software
engineering 51, sales development 43.

IT service desk and incident response is the only use case in the top three of
both, which makes it the one bet that does not depend on resolving the weighting
question first.

## Verifying the tables

The grids are hand-maintained Markdown, which drifts. Before trusting any number:

```bash
python3 verify_scores.py          # check every row total
python3 verify_scores.py --fix    # rewrite any total that disagrees with its columns
```

## Built With

1. **Background noise** — https://open.spotify.com/playlist/0XC4NqtE1o4BaATYEf9VFP
2. **MacBook Air (M1)**
3. **VS Code**
4. **Claude Opus 5**
5. **GitHub Copilot**
