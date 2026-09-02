# Use Case Attributes Weighted for Operational Efficiency

## The Original Weighting System — Optimizing for Throughput

### Design Intent
This weighting asks one question: **what high-volume, repetitive business process can we
automate right now?** It is built for speed to deployment and measurable cost reduction,
not for capability depth. It is the weighting implicitly behind most vendor marketing and
most "Top 10 Agentic AI Use Cases" lists.

15 attributes across 3 tiers. Maximum possible score **30**, minimum **-30**.

### What Scores Well Here
- ✓ High-volume, structured, quantifiable input data
- ✓ Bounded processes with clear, constrained resolution paths
- ✓ Results the agent can verify immediately and automatically
- ✓ Exact policies and prescriptive rules to follow
- ✓ Stable, well-understood environments the agent can self-navigate
- ✗ Unbounded solution spaces requiring exploration
- ✗ Work needing many iterative loops before an answer emerges
- ✗ Correctness that can only be judged slowly or partially

### Why These Multipliers
- **×3 (High)** — the five attributes that determine whether automation is *possible at
  all*. Without volume, repeatability, and verifiability, there is no business case.
- **×2 (Medium)** — the five that determine whether it is *tractable*. Bounded scope and
  exact rules decide how much engineering the build takes.
- **×1 (Low)** — the five that are *table stakes*. Log review, memory management, and
  human escalation matter, but every serious agent platform provides them, so they do not
  separate one use case from another.

### Impact on Use Case Rankings
| Rank | Use case | Score | % of max |
| --- | --- | --- | --- |
| 1 | Customer support resolution | 29 | 97% |
| 2 | Finance operations: invoices, AP, close | 28 | 93% |
| 3 | IT service desk and incident response | 27 | 90% |
| 4 | Sales development and lead qualification | 21 | 70% |
| 12 | Software engineering agents | 1 | 3% |
| 17 | Personal computer-use agents | -5 | -17% |

Customer support scores 29 out of a possible 30 — it is very nearly the perfect use case
*by this definition of perfect*, which is the first clue that the definition is doing more
work than the data.

### Known Blind Spot
This weighting ranks software engineering agents 12th of 17, tied with supply chain
rerouting, below procurement negotiation. That result is wrong, and it is wrong
structurally rather than by a scoring error.

Every property that makes software engineering a *good* agent task — an unbounded solution
space, many iterative loops, correctness that only partial testing can confirm, requirements
clarified by building — is scored here as a **defect**. The rubric does not measure agent
suitability. It measures resemblance to a business process automation project, and so it
can only ever select business process automation.

See [Use Case Attributes Weighted for Cognitive Complexity.md](Use%20Case%20Attributes%20Weighted%20for%20Cognitive%20Complexity.md)
for the rebuilt weighting that corrects this, and the reasoning behind it.

### Fundamental Shift
Read against its counterpart, this represents:
- **Cognitive complexity and tool coordination weighting** ← **Simple business automation weighting**

Use this weighting when the goal is a number on the board within two quarters. Use the
cognitive complexity weighting when the goal is a capability a competitor cannot copy in one.

---

## Weighting Rubric

### High (times 3)
- Input data is high volume, multi-source, quantifiable, fresh, structured and consistent (i.e. not conflicting)
- Agent Can Iterate. Use Case is Repeatable (commonly - input data is/can be non-destructive)
- Agent Can Check (verify) results (i.e. results are decidable)
- Speed to solution and volume of use cases are high priorities
- Agent Can Easily self-navigate a stable environment that is well understood

### Medium (times 2)
- The use case has a clear resolution path which is also bounded
- Solution process is bounded
- Solution set is constrained
- Policy and Rules that are exact and easy to follow
- To solve the problem, there are a low in number of turns where new input must be gathered

### Low (times 1)
- Inputs and Outputs can form a fast loop
- Agent Can Review logs of existing tests and results
- Operator can "manage" the agent's memory
- If sub-agents are used, there is strong goal alignment and cross-agent coordination
- Agent Can Pass exceptions to a human
