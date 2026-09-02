# Use Case Analysis Pass 2 - Cognitive Complexity Weighting

| Use Case | T1: Decompose Complex (×6) | T1: Unbounded Space (×6) | T1: Learn Iterative (×6) | T1: Multiple Paths (×6) | T2: Tool Integration (×5) | T2: Sub-agent Coord (×5) | T2: Multi-turn Context (×5) | T2: Reviewable/Testable (×5) | T3: Repeatable (×3) | T3: Verify Results (×3) | T3: Fast Feedback (×3) | T4: Clear Paths (×2) | T4: Bounded Rules (×2) | T4: Constrained Solution (×2) | T5: Manage Memory (×1) | T5: Escalate (×1) | T5: Fast Validation (×1) | Total Weighted Score |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IT service desk and incident response | 0 | 0 | 3 | 0 | 3 | 3 | 3 | 5 | 9 | 9 | 6 | 4 | 2 | 2 | 1 | 1 | 1 | 52 |
| Software engineering agents | 6 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 3 | 0 | 3 | 0 | 0 | -2 | 1 | 1 | 1 | 51 |
| Sales development and lead qualification | 3 | 0 | 3 | 3 | 3 | 0 | 3 | 3 | 6 | 3 | 6 | 4 | 2 | 2 | 1 | 1 | 0 | 43 |
| Fraud, AML, and real-time risk | 3 | 3 | 3 | 3 | 5 | 3 | 5 | 5 | 6 | 3 | 6 | 0 | -2 | -2 | 1 | 1 | -1 | 42 |
| Security operations | 6 | 3 | 6 | 3 | 5 | 3 | 5 | 5 | 3 | 3 | 3 | 0 | -2 | -2 | -1 | 1 | -1 | 40 |
| Marketing campaign creation and optimization | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 6 | 3 | 6 | 2 | 0 | 0 | -1 | 1 | 0 | 38 |
| Customer support resolution | 0 | -6 | 0 | -6 | 0 | 0 | 0 | 3 | 9 | 9 | 9 | 4 | 4 | 4 | 1 | 1 | 1 | 33 |
| Finance operations: invoices, AP, reconciliation, close | 0 | -6 | 0 | -6 | 0 | 0 | 0 | 3 | 9 | 9 | 9 | 4 | 4 | 4 | 1 | 1 | 1 | 33 |
| Legal contract review and due diligence | 6 | 6 | 6 | 6 | 3 | 0 | 5 | 3 | 0 | 0 | 0 | 0 | -2 | -2 | -1 | 1 | -1 | 30 |
| Manufacturing quality, scheduling, and predictive maintenance | 3 | 0 | 3 | 3 | 5 | 3 | 3 | 3 | 3 | 0 | 3 | 0 | -2 | -2 | 1 | 1 | 0 | 27 |
| Supply chain, inventory, and logistics rerouting | 3 | 0 | 3 | 3 | 5 | 3 | 5 | 3 | 3 | 0 | 3 | 0 | -2 | -2 | -1 | 1 | 0 | 27 |
| Deep research and competitive intelligence | 6 | 6 | 6 | 6 | 3 | 0 | 3 | 3 | 0 | -3 | -3 | 0 | -2 | 0 | 1 | 1 | -1 | 26 |
| HR service desk, recruiting, and onboarding | 0 | -6 | 3 | -6 | 0 | 3 | 3 | 3 | 9 | 3 | 3 | 4 | 2 | 2 | 1 | 1 | 1 | 26 |
| Healthcare admin: documentation, coding, prior auth, claims | 6 | 6 | 6 | 3 | 3 | 0 | 5 | 3 | 3 | -3 | -3 | 0 | -2 | -2 | -1 | 1 | 0 | 25 |
| Personal computer-use agents: shop, book, fill forms, travel | 6 | 6 | 6 | 6 | 5 | 0 | 5 | 0 | 0 | -3 | -3 | 0 | -2 | -2 | 1 | 1 | -1 | 25 |
| Procurement and supplier negotiation | 3 | 0 | 3 | 3 | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | -2 | 0 | 1 | 1 | 0 | 18 |
| Enterprise knowledge and research assistants | 3 | 0 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | -3 | -3 | 0 | -2 | 0 | 1 | 1 | 0 | 15 |

---
## Findings vs. Internet Consensus

*All scores below recomputed from the attribute columns; the table above is sorted by corrected total.*

### Pass 2 Results (Cognitive Complexity Weighting)

**Top 6:**
1. IT service desk and incident response — 52
2. Software engineering agents — 51
3. Sales development and lead qualification — 43
4. Fraud, AML, and real-time risk — 42
5. Security operations — 40
6. Marketing campaign creation and optimization — 38

**Bottom 4:** Healthcare admin (25), Personal computer-use agents (25), Procurement and supplier negotiation (18), Enterprise knowledge and research assistants (15).

### Movement vs. Pass 1 (Operational Efficiency Weighting)

| Use Case | Pass 1 rank | Pass 2 rank | Movement |
|----------|---|---|---|
| Software engineering agents | 12 | 2 | +10 |
| Security operations | 9 | 5 | +4 |
| Legal contract review and due diligence | 16 | 9 | +7 |
| Fraud, AML, and real-time risk | 7 | 4 | +3 |
| Personal computer-use agents | 17 | 15 | +2 |
| IT service desk and incident response | 3 | 1 | +2 |
| Customer support resolution | 1 | 7 | -6 |
| Finance operations | 2 | 8 | -6 |
| HR service desk, recruiting, and onboarding | 5 | 13 | -8 |

### Key Divergences

#### Overrated in Current Discourse
- **Customer support resolution** — #1 online and #1 in Pass 1 (29), but #7 in Pass 2 (33). Ranked high for efficiency, not for sophistication. The bounded solution space that makes it easy to ship is exactly what caps its ceiling.
- **HR service desk and recruiting** — a fixture of every industry list, but #13 in Pass 2 (26), the largest drop of any use case. Penalized for bounded scope and weak iterative improvement.
- **Enterprise knowledge and research assistants** — heavily marketed, last in Pass 2 (15). Retrieval without a constrained action space scores poorly under both weightings.

#### Underrated in Current Discourse
- **IT service desk and incident response** — #1 in Pass 2 (52) and #3 in Pass 1 (27). **The only use case in the top three of both weightings.** Password resets are bounded and verifiable; incident investigation is unbounded and exploratory. The same queue contains both shapes of work, which is why it wins regardless of which philosophy you apply.
- **Security operations** — rarely appears in general "top use cases" lists, #5 in Pass 2 (40). Strong tool ecosystem, sub-agent coordination, and pattern learning.
- **Fraud, AML, and real-time risk** — #4 in Pass 2 (42). Mainstream coverage fixates on regulatory burden; the weighting highlights tool integration and iterative learning.

#### Correctly Ranked
- **Software engineering agents** — #2 in Pass 2 (51), up from #12 in Pass 1 (1). The single largest swing in the analysis, and the result that triggered the reweighting. Hype and analysis agree here.
- **Deep research and competitive intelligence** — #12 in Pass 2 (26). Solid cognitive complexity, weak execution and repeatability. Promising but unproven at scale.

### Philosophical Differences

**Pass 1 (Operational Efficiency) rewards:** implementation simplicity, quick ROI, high-volume repetitive automation, cost reduction through headcount replacement. This is the weighting behind most vendor marketing, which is why support and sales tools dominate coverage.

**Pass 2 (Cognitive Complexity) rewards:** problem-solving depth, iterative learning, multi-tool coordination, capability amplification for expert users rather than task replacement.

Neither is wrong. They are different purchases.

### Strategic Implications

1. **Want quick ROI?** Use Pass 1. Customer support, finance ops, IT ticket routing.
2. **Want defensible capability?** Use Pass 2. Software engineering, security operations, fraud.
3. **Want to hedge?** Start with IT service desk and incident response — the only use case in the top three of both weightings, and therefore the one bet that does not depend on getting the strategy question right first.
4. **The methodological caveat:** Pass 1 and Pass 2 use different attributes, multipliers, and maximums. Only the *ordering* is comparable across passes, never the raw scores.
