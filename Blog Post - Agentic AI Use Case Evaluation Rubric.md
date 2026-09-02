# Scoring 17 Agentic AI Use Cases, and What Broke My First Rubric

Every "Top 10 Agentic AI Use Cases" article says the same thing. Customer support first, then sales development, IT service desk, HR recruiting. I've read a lot of these. They're not wrong, exactly, but they all read like they were assembled from the same press releases, and none of them tell you *why* those use cases belong at the top.

That bugged me. Some agent deployments work and some burn a year of engineering time and never leave pilot, and "customer support is a good use case" doesn't help you predict which is which. So I decided to stop reading lists and build a scoring rubric instead.

My objective was simple: come up with a set of attributes that actually predict whether an agent will succeed at a task, score the commonly cited use cases against them, and see whether the ranking that falls out matches the internet consensus.

It didn't. That turned out to be the interesting part.

## The setup

Here's the parts list:

- The 20 most-cited agentic AI use cases, pulled from the usual roundups. I carried 17 forward that were distinct enough to score separately.
- A list of about 20 attributes that describe what makes a task agent-friendly. Things like: the task is repeatable, the solution set is constrained, input data is high-volume and structured, the agent can verify its own results, the agent can escalate to a human.
- A three-point scale. **True (1)** if the use case clearly has the attribute, **Somewhat (0)** if it's mixed, **False (-1)** if it doesn't.
- A weight per attribute, because these obviously don't matter equally.

Multiply, add up the row, sort the column. That's the whole method. It fits in a spreadsheet and takes an afternoon.

For the first weighting I put the ×3 multiplier on the things I assumed mattered most for automation: high-volume structured input, repeatability, verifiable results, speed as a priority, and a stable environment the agent can navigate on its own. Bounded process and clear rules got ×2. The supporting stuff, memory management, log review, human escalation, got ×1.

Then I scored everything.

## Pass 1 and 2: the answer I expected

The weighted results came out about where the listicles said they would:

| Use case | Score |
| --- | --- |
| Customer support resolution | 29 |
| Finance operations: invoices, AP, close | 28 |
| IT service desk and incident response | 27 |
| Sales development and lead qualification | 21 |
| HR service desk and recruiting | 17 |
| Marketing campaign optimization | 17 |

Customer support on top. AP invoice matching and IT service desk right behind it. If you'd shown me this table without the rest of the analysis I would have nodded and moved on. It agrees with the consensus, and it agrees with my own intuition about which projects ship.

Then I looked at the bottom of the same table.

Software engineering agents scored **1**. Twelfth out of seventeen, in a three-way tie with supply chain rerouting and predictive maintenance, against 29 for customer support.

## Key learning #1: when the rubric tells you something you know is false, the rubric is the broken part

I use coding agents every day. So does most of the industry. Whatever list you want to argue about, this one is real, it's in production, it's spending actual money, and by some telemetry it's close to half of all agent tool calls. A rubric that puts it in the bottom third, below procurement negotiation, is not describing the world.

So I went back and asked what the rubric was actually measuring. Here's what it was rewarding:

- Bounded solution spaces
- Few turns of new input
- Immediate, automatic verification
- Exact policies and prescriptive rules

And here's what writing software is:

- An unbounded solution space. There are a million ways to write the function.
- Many iterative loops. You write, you run, you read the error, you try again.
- Verification that's real but slow and partial. Tests catch some of it. Not all of it.
- Requirements that arrive vague and get clarified by building.

Every single thing that makes software engineering a *good* agent task, my rubric was scoring as a defect. It wasn't measuring agent suitability at all. It was measuring resemblance to a business process automation project circa 2015. Of course customer support won. I'd built a rubric that could only ever pick customer support.

## Pass 3: rebuilding around the thing I got wrong

The fix wasn't to nudge software engineering up a few points. It was to admit I'd encoded one philosophy, "what high-volume repetitive process can we automate," and pretend it was neutral. So I built the opposite rubric on purpose and ran the same 17 use cases through it.

The second rubric asks a different question: "what intellectually demanding problem can we put an agent on alongside a human expert?" Seventeen attributes, five tiers.

**Tier 1, Cognitive Complexity (×6).** Can the agent decompose an ambiguous problem? Is the solution space open enough to need exploration? Can it improve through iteration and test feedback? Are there multiple valid paths with trade-offs to weigh?

**Tier 2, Tool Integration and Coordination (×5).** Can it drive multiple tools and APIs? Coordinate sub-agents? Hold context across a long multi-turn session? Are results reviewable through logs and test suites?

**Tier 3, Execution Excellence (×3).** Repeatable patterns, partial self-verification, fast feedback loops.

**Tier 4, Process Clarity (×2).** Clear resolution paths, bounded rules, constrained solutions.

**Tier 5, Support and Safety (×1).** Operator memory management, human escalation, fast validation loops. Important, but table stakes, not differentiators.

Same three-point scale. Same arithmetic. New ranking:

| Use case | Score |
| --- | --- |
| IT service desk and incident response | 52 |
| Software engineering agents | 51 |
| Sales development and lead qualification | 43 |
| Fraud, AML, and real-time risk | 42 |
| Security operations | 40 |
| Marketing campaign optimization | 38 |
| Customer support resolution | 33 |
| Finance operations | 33 |

Software engineering went from 1 to 51, twelfth place to second. Customer support fell from the top to mid-pack. IT service desk stayed at the top of both, which is the most interesting result in the whole exercise, and I'll come back to it.

One caveat before anyone quotes those numbers at me: the two passes are not on the same scale. Different attributes, different multipliers, different maximums. "Customer support went from 29 to 33" doesn't mean it improved. The only thing you can legitimately compare across passes is the *ordering*, and the ordering moved a lot.

## Key learning #2: the ranking is a picture of your weighting, not of reality

This is the part I'd want someone to take away.

I built two rubrics. Both are defensible. Both are internally consistent. Neither one has a bug in it. And they produce nearly opposite recommendations about where to start.

That means every ranked list of agentic AI use cases you've ever read, including both of mine, is mostly a readout of what the author decided to weight. When a vendor tells you customer support is the obvious first use case, they are not lying. They're telling you their weighting, and their weighting is speed to deployment and volume of tickets. That's a completely reasonable thing to optimize for. It's just not the same as "this is the highest-value place to put an agent," and the two get conflated constantly.

So the useful question isn't "what's the best agentic AI use case." It's "which of these two rubrics describes what my company is actually trying to buy?" If you need a number on the board in two quarters, Pass 1 is your rubric and customer support really is your answer. If you're trying to build something a competitor can't copy in a quarter, Pass 3 is your rubric and the answer looks like security operations or engineering tooling.

Pick your weighting first. The ranking is downstream of it.

## Key learning #3: look for the use cases that win under both

IT service desk and incident response came out first under the cognitive complexity rubric and near the top under operational efficiency. It's the only use case that does well no matter which philosophy you apply.

Once you see it, it makes sense. A password reset is bounded, repeatable, high-volume, and instantly verifiable. That's the Pass 1 profile exactly. A production incident at 2am is unbounded investigation across logs, metrics, and recent commits, with several plausible root causes to weigh. That's the Pass 3 profile exactly. Same team, same tools, same ticket queue, both shapes of work.

Fraud and AML have a similar dual character and score respectably in both. So does finance ops, though for narrower reasons.

If I were spending someone's budget, I'd start there. A use case that only wins under one weighting is a bet on that weighting being right. A use case that wins under both is a bet on the domain, and you get to be wrong about your strategy without being wrong about your project.

## Where this thing breaks

I want to be honest about the limits, because it's a spreadsheet and an afternoon, not a research paper.

The weights are my judgment. I decided problem decomposition is worth 6x and human escalation is worth 1x. Someone who's been burned by an agent that couldn't hand off cleanly would weight that differently and get a different answer, and I couldn't prove them wrong.

There's no regulatory or compliance dimension in the second rubric. Healthcare admin scores 25 on cognitive complexity, which is fine, and says nothing about whether you can actually ship it inside a HIPAA boundary in a reasonable timeframe. Same problem for anything in financial services. That's a real gap and it's the first thing I'd add.

It scores the use case, not your team. A boring use case with three people who've shipped agents before beats an exciting one with a team that hasn't, every time, and none of that shows up in the arithmetic.

And it can't see technology maturity. A use case can score well and still fail because the memory systems or the tool-calling reliability aren't there yet. The rubric assumes today's capabilities are fixed. They very much aren't.

One more, on my own analysis. When I went back to check the arithmetic, 21 of the 51 scored rows had totals that didn't match what their columns actually summed to. All of it was small, a point or two per row, and the corrected numbers are what you see above. It didn't change either headline: customer support still wins the first rubric, IT service desk and software engineering still take the top two spots in the second.

It did move things in the middle, though. Finance ops passed IT service desk in the first pass. Software engineering came off the negative side of the ledger entirely. If I'd been trying to split a decision between two adjacent use cases, hand arithmetic would have decided it for me, and I'd never have known. Keep this in a spreadsheet with real formulas, or check the sums with six lines of Python. Don't hand-maintain a 17-by-17 grid of integers in Markdown, which is a lesson I apparently need to relearn every few years.

## Try it on your own list

The whole thing costs an afternoon and whatever you value your own time at, which makes it roughly the cheapest planning artifact you'll build this quarter.

Take the 17 attributes, take whatever use cases are actually on your roadmap, and score them twice. Once weighted for speed to value, once weighted for capability depth. If a use case wins both, start there. If the two rankings disagree violently, you've learned something more useful than a score: your team hasn't agreed yet on what you're optimizing for, and you found out in a spreadsheet instead of in month nine of a build.

The attribute lists, both weighting schemes, and the full scored tables are in the repo. Take them, change my weights, and tell me what you get. I'd genuinely like to know which ones I have wrong.
