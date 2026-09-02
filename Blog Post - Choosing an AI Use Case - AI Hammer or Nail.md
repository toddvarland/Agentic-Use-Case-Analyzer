# Choosing an AI use case? AI Hammer or Nail?

Every "Top 10 Agentic AI Use Cases" article says the same thing. Customer support first, then sales development, IT service desk, HR recruiting. I've read a lot of these. They're not wrong, exactly, but they read like they were assembled from the same press releases, and none of them tell you *why* those use cases belong at the top.

That bugged me. Some agent deployments work and some burn a year of engineering time and never leave pilot, and "customer support is a good use case" doesn't help you predict which is which.

So I stopped reading lists and built a scoring rubric instead. The key thing I learned in a dozen years at AWS, sometimes the hard way, is that you have to define the problem honestly before you start solving it. My objective was to find a set of attributes that actually predict whether an agent will succeed at a task, score the commonly cited use cases against them, and see whether the ranking that falls out matches the internet consensus.

It didn't. That turned out to be the interesting part.

Let me set a challenge for both of us. By the time we're done here, I want this to feel like no big deal, pretty straightforward, something you could run yourself on Monday against whatever is actually on your roadmap. The goal is to demystify this, not to hand you another framework to take on faith.

Four parts: how I set it up, what the first rubric said, why it was wrong, and what the rebuild changed.

## What I'm not covering

A word on scope first, because most evaluation frameworks quietly overpromise and I'd rather say up front what this one can't do.

I'm not scoring vendors or products. I'm not estimating ROI, timelines, or headcount. There's no regulatory or compliance dimension, which matters a great deal in healthcare and financial services, and I'll come back to it. And I'm not scoring your team, which in my experience is at least as predictive as anything on this list.

What I am doing is scoring the shape of the work itself: whether a task has the characteristics that let an agent do it well. That's a narrower question than "should we build this," and it's the one I kept seeing people skip.

## The setup

Here's the parts list:

- The 20 most-cited agentic AI use cases, pulled from the usual roundups. I carried 17 forward that were distinct enough to score separately.
- About 20 attributes describing what makes a task agent-friendly. The task is repeatable, the solution set is constrained, input data is high-volume and structured, the agent can verify its own results, the agent can escalate to a human, and so on. Several of those bundle together once you start scoring, so the first rubric ends up with 15 columns rather than 20.
- A three-point scale. **True (1)** if the use case clearly has the attribute, **Somewhat (0)** if it's mixed, **False (-1)** if it doesn't.
- A weight per attribute, because these obviously don't matter equally.

Multiply, add up the row, sort the column. That's the whole method. It fits in a spreadsheet and takes an afternoon.

The weights are the knobs and dials here, and they're where all the real decisions live. For the first pass I put the ×3 multiplier on what I assumed mattered most for automation: high-volume structured input, repeatability, verifiable results, speed as a priority, and a stable environment the agent can navigate on its own. Bounded process and clear rules got ×2. The supporting attributes, memory management, log review, human escalation, got ×1.

Then I scored everything.

## The answer I expected

The weighted results came out about where the listicles said they would:

| Use case | Score |
| --- | --- |
| Customer support resolution | 29 |
| Finance operations: invoices, AP, close | 28 |
| IT service desk and incident response | 27 |
| Sales development and lead qualification | 21 |
| HR service desk and recruiting | 17 |
| Marketing campaign optimization | 17 |

Customer support on top, AP invoice matching and IT service desk right behind it. If you'd shown me this table without the rest of the analysis I would have nodded and moved on. It agrees with the consensus, and it agrees with my own intuition about which projects actually ship.

Then I looked at the bottom of the same table.

Software engineering agents scored **1**. Twelfth out of seventeen, in a three-way tie with supply chain rerouting and predictive maintenance, against 29 for customer support.

## Key learning #1: when the rubric tells you something you know is false, the rubric is the broken part

I use coding agents every day. So does much of the industry these days. Whatever you want to argue about this category, it's real, it's in production, it's spending actual money, and by some telemetry it's close to half of all agent tool calls. A rubric that buries it in the bottom third, below procurement negotiation, is not describing the world I work in.

So I went back and asked what the rubric was actually measuring. Here's what it rewarded:

- Bounded solution spaces
- Few turns of new input
- Immediate, automatic verification
- Exact policies and prescriptive rules

And here's what writing software is:

- An unbounded solution space. There are a million ways to write the function.
- Many iterative loops. You write, you run, you read the error, you try again.
- Verification that's real but slow and partial. Tests catch some of it. Not all of it.
- Requirements that arrive vague and get clarified by building.

Every single thing that makes software engineering a good agent task, my rubric was scoring as a defect. It wasn't measuring agent suitability at all. It was measuring resemblance to a business process automation project circa 2015. Of course customer support won. I'd built a rubric that could only ever pick customer support.

## Rebuilding around the thing I got wrong

The fix wasn't to nudge software engineering up a few points. It was to admit I'd encoded one philosophy, "what high-volume repetitive process can we automate," and then treated it as neutral. So I built the opposite rubric on purpose and ran the same 17 use cases through it.

The second rubric asks a different question: what intellectually demanding problem can we put an agent on alongside a human expert? Seventeen attributes, five tiers.

**Tier 1, Cognitive Complexity (×6).** Can the agent decompose an ambiguous problem? Is the solution space open enough to need exploration? Can it improve through iteration and test feedback? Are there multiple valid paths with trade-offs to weigh?

**Tier 2, Tool Integration and Coordination (×5).** Can it drive multiple tools and APIs? Coordinate sub-agents? Hold context across a long multi-turn session? Are results reviewable through logs and test suites?

**Tier 3, Execution Excellence (×3).** Repeatable patterns, partial self-verification, fast feedback loops.

**Tier 4, Process Clarity (×2).** Clear resolution paths, bounded rules, constrained solutions.

**Tier 5, Support and Safety (×1).** Operator memory management, human escalation, fast validation loops. Important, but table stakes rather than differentiators.

Same three-point scale, same arithmetic, new ranking:

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

Software engineering went from a weighted score of 1 to 51, twelfth place to second. Customer support fell from the top to mid-pack. IT service desk stayed at the top of both, which is the most interesting result in the whole exercise, and I'll come back to it.

Keep in mind that the two passes are not on the same scale. Different attributes, different multipliers, different maximums. "Customer support went from 29 to 33" doesn't mean it improved. The only thing you can legitimately compare across passes is the ordering, and the ordering moved a lot.

## Key learning #2: the ranking is a picture of your weighting, not of reality

This is the part I'd want you to take away if you take away one thing.

I built two rubrics. Both are defensible. Both are internally consistent. Neither one has a bug in it. And they produce nearly opposite recommendations about where to start.

Think about tuning an engine. You can tune for peak horsepower (get to a new place fast) or you can tune for fuel economy (get to a new place economically). Same engine, same dyno, same instrumentation, two different tunes, and the winner flips depending on which one you picked. Nobody stands around arguing about which dyno number is the true one, because everybody understands that you state what you're tuning for first and the number follows from that.

We don't do that with agentic AI use cases. We publish the number and leave the tune implicit.

Which means every ranked list you've ever read, including both of mine, is mostly a readout of what the author decided to weight. When a vendor tells you customer support is the obvious first use case, they aren't lying to you. They're telling you their tune, and their tune is speed to deployment and ticket volume. That's a perfectly reasonable thing to optimize for. It just isn't the same claim as "this is the highest-value place to put an agent," and the two get conflated constantly.

So the useful question isn't "what's the best agentic AI use case." It's "which of these two rubrics describes what my company is actually trying to buy?" Need a number on the board in two quarters? The first rubric is your tune, and customer support really is your answer. Trying to build something a competitor can't copy in a quarter? Second rubric, and the answer looks like security operations or engineering tooling.

Pick your weighting first. The ranking is downstream of it.

## Key learning #3: look for the use cases that win under both

IT service desk and incident response came out first under cognitive complexity and third under operational efficiency. It's the only use case that does well no matter which philosophy you apply.

Once you see it, it makes sense. A password reset is bounded, repeatable, high-volume, and instantly verifiable, which is the first profile exactly. A production incident at 2am is unbounded investigation across logs, metrics, and recent commits, with several plausible root causes to weigh, which is the second profile exactly. Same team, same tools, same ticket queue, both shapes of work sitting in it.

Fraud and AML have a similar dual character and score respectably under both. So does finance ops, for narrower reasons.

If I were spending someone's budget, I'd start there. A use case that only wins under one weighting is a bet on that weighting being right. A use case that wins under both is a bet on the domain, and you get to be wrong about your strategy without being wrong about your project.

## Where this breaks

I want to be honest about the limits, because this is a spreadsheet and an afternoon, not a research paper.

The weights are my judgment. I decided problem decomposition is worth 6x and human escalation is worth 1x. Somebody who's been burned by an agent that couldn't hand off cleanly would weight that differently, get a different answer, and I couldn't prove them wrong.

There's no regulatory dimension in the second rubric. Healthcare admin scores 25 on cognitive complexity, which is fine, and says exactly nothing about whether you can ship it inside a HIPAA boundary on a sane timeline. Same problem across financial services. That's a real gap and it's the first thing I'd add.

It scores the use case, not your team. A boring use case with three people who have shipped agents before beats an exciting one with a team that hasn't, every time, and none of that shows up in the arithmetic.

And it can't see technology maturity. A use case can score well and still fail because tool-calling reliability or memory systems aren't there yet. The rubric assumes today's capabilities are fixed. They very much aren't.

## To recap

The tools you have available here come down to four choices, and the whole result depends on getting them in balance:

1. **The use cases on the list.** I took the internet's list. Yours should be your roadmap.
2. **The attributes you score against.** Roughly 20, describing the shape of the work.
3. **The weights.** The knobs and dials. This is the choice that determines your answer, so make it out loud and write down why.
4. **How you read the output.** Ordering within a pass is meaningful. Raw scores across passes are not.

Get those in balance and the ranking that falls out is genuinely useful. Leave the third one implicit, which is what most published lists do, and you've produced a number that looks objective and is really just your assumptions with arithmetic on top.

## Try it on your own list

Looking in the rear-view mirror at this exercise, the ranking turned out to be the least valuable thing it produced. What I actually got was a much clearer picture of what I had been assuming, and I didn't know I was assuming it until a rubric I built myself told me something I knew was false.

The whole thing costs an afternoon and whatever you value your own time at, which makes it roughly the cheapest planning artifact you'll build this quarter. Take the attributes, take whatever use cases are actually on your roadmap, and score them twice. Once tuned for speed to value, once tuned for capability depth. If a use case wins both, start there. If the two rankings disagree violently, you've learned something more useful than a score: your team hasn't agreed yet on what you're optimizing for, and you found that out in a spreadsheet instead of in month nine of a build.

The attribute lists, both weighting schemes, and the full scored tables are in the repo. Take them, change my weights, and tell me what you get. Hopefully there are a few useful items in here you can take away, and I'd genuinely like to know which ones I have wrong.
