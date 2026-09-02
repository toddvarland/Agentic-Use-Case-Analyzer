# Use Case Analysis Pass 3 - Cognitive Complexity Weighting

| Use Case | T1: Decompose Complex (×6) | T1: Unbounded Space (×6) | T1: Learn Iterative (×6) | T1: Multiple Paths (×6) | T2: Tool Integration (×5) | T2: Sub-agent Coord (×5) | T2: Multi-turn Context (×5) | T2: Reviewable/Testable (×5) | T3: Repeatable (×3) | T3: Verify Results (×3) | T3: Fast Feedback (×3) | T4: Clear Paths (×2) | T4: Bounded Rules (×2) | T4: Constrained Solution (×2) | T5: Manage Memory (×1) | T5: Escalate (×1) | T5: Fast Validation (×1) | Total Weighted Score |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Software engineering agents | 6 | 6 | 6 | 6 | 5 | 5 | 5 | 5 | 3 | 0 | 3 | 0 | 0 | -2 | 1 | 1 | 1 | 51 |
| Legal contract review and due diligence | 6 | 6 | 6 | 6 | 3 | 0 | 5 | 3 | 0 | 0 | 0 | 0 | -2 | -2 | -1 | 1 | -1 | 30 |
| Deep research and competitive intelligence | 6 | 6 | 6 | 6 | 3 | 0 | 3 | 3 | 0 | -3 | -3 | 0 | -2 | 0 | 1 | 1 | -1 | 26 |
| Healthcare admin: documentation, coding, prior auth, claims | 6 | 6 | 6 | 3 | 3 | 0 | 5 | 3 | 3 | -3 | -3 | 0 | -2 | -2 | -1 | 1 | 0 | 25 |
| Security operations | 6 | 3 | 6 | 3 | 5 | 3 | 5 | 5 | 3 | 3 | 3 | 0 | -2 | -2 | -1 | 1 | -1 | 39 |
| Customer support resolution | 0 | -6 | 0 | -6 | 0 | 0 | 0 | 3 | 9 | 9 | 9 | 4 | 4 | 4 | 1 | 1 | 1 | 33 |
| IT service desk and incident response | 0 | 0 | 3 | 0 | 3 | 3 | 3 | 5 | 9 | 9 | 6 | 4 | 2 | 2 | 1 | 1 | 1 | 52 |
| Fraud, AML, and real-time risk | 3 | 3 | 3 | 3 | 5 | 3 | 5 | 5 | 6 | 3 | 6 | 0 | -2 | -2 | 1 | 1 | -1 | 41 |
| Finance operations: invoices, AP, reconciliation, close | 0 | -6 | 0 | -6 | 0 | 0 | 0 | 3 | 9 | 9 | 9 | 4 | 4 | 4 | 1 | 1 | 1 | 33 |
| Sales development and lead qualification | 3 | 0 | 3 | 3 | 3 | 0 | 3 | 3 | 6 | 3 | 6 | 4 | 2 | 2 | 1 | 1 | 0 | 43 |
| Marketing campaign creation and optimization | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 6 | 3 | 6 | 2 | 0 | 0 | -1 | 1 | 0 | 38 |
| HR service desk, recruiting, and onboarding | 0 | -6 | 3 | -6 | 0 | 3 | 3 | 3 | 9 | 3 | 3 | 4 | 2 | 2 | 1 | 1 | 1 | 28 |
| Supply chain, inventory, and logistics rerouting | 3 | 0 | 3 | 3 | 5 | 3 | 5 | 3 | 3 | 0 | 3 | 0 | -2 | -2 | -1 | 1 | 0 | 27 |
| Personal computer-use agents: shop, book, fill forms, travel | 6 | 6 | 6 | 6 | 5 | 0 | 5 | 0 | 0 | -3 | -3 | 0 | -2 | -2 | 1 | 1 | -1 | 21 |
| Procurement and supplier negotiation | 3 | 0 | 3 | 3 | 3 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | -2 | 0 | 1 | 1 | 0 | 18 |
| Manufacturing quality, scheduling, and predictive maintenance | 3 | 0 | 3 | 3 | 5 | 3 | 3 | 3 | 3 | 0 | 3 | 0 | -2 | -2 | 1 | 1 | 0 | 28 |
| Enterprise knowledge and research assistants | 3 | 0 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | -3 | -3 | 0 | -2 | 0 | 1 | 1 | 0 | 15 |

---

## Findings vs. Internet Consensus

### Pass 3 Results (Cognitive Complexity Weighting)
**Top 5:**
1. IT service desk and incident response - 52
2. Software engineering agents - 51
3. Fraud, AML, and real-time risk - 41
4. Security operations - 39
5. Marketing campaign optimization - 38

### Current Internet Consensus
**Most cited/discussed:**
1. Customer support resolution (consistently #1)
2. Software engineering agents (growing rapidly, but often underestimated for complexity)
3. IT service desk and incident response (widely implemented)
4. Sales development and lead qualification (heavily marketed by vendors)
5. Fraud/AML and security ops (compliance-driven, less discussed in mainstream media)

### Key Divergences

#### **Overrated in Current Discourse:**
- **Customer support resolution** (#1 online, #6 in Pass 3 at 33 points)
  - Internet treats it as simplest/most obvious use case
  - Pass 3 recognizes limited complexity and bounded solution space
  - Ranked high in efficiency, not in sophistication

- **Sales development and lead qualification** (#4-5 online, #10 in Pass 3 at 43 points)
  - Heavily marketed by B2B SaaS vendors and tool companies
  - Pass 3 shows it lacks true cognitive complexity and unbounded exploration

- **HR service desk and recruiting** (frequent in lists, #12 in Pass 3 at 28 points)
  - Consistently cited across industry lists
  - Penalized in Pass 3 for low iterative improvement and bounded nature

#### **Underrated in Current Discourse:**
- **IT service desk and incident response** (commonly discussed but not #1, now ranked #1 at 52 points)
  - Combines cognitive complexity (incident investigation) with execution excellence
  - Can learn and improve from log analysis and patterns
  - Internet treats as similar to customer support; actually far more sophisticated

- **Fraud, AML, and real-time risk** (discussed mainly in finance circles, #3 in Pass 3 at 41 points)
  - Online discourse often focuses on regulatory burden (negative)
  - Pass 3 highlights strong tool integration, iterative learning, and multiple detection paths
  - Undervalued in mainstream media coverage

- **Security operations** (discussed primarily by security vendors, #4 in Pass 3 at 39 points)
  - Rarely appears in general "top agentic use cases" lists
  - Actually ranks high due to tool ecosystem, sub-agent coordination, and pattern learning
  - Treated as niche; actually broadly applicable

#### **Correctly Ranked:**
- **Software engineering agents** (heavily hyped, now #2 at 51 points)
  - Internet consensus: "game-changing but complex"
  - Pass 3 confirms: extremely high cognitive complexity and tool integration
  - Validation: OpenAI, GitHub, Anthropic, and startups (Devin, etc.) all betting heavily
  - One of the few where hype aligns with analytical weighting

- **Deep research and competitive intelligence** (emerging, #6 in Pass 3 at 26 points)
  - OpenAI Deep Research positioning it as next frontier
  - Pass 3 shows solid cognitive complexity but weak execution/repeatability
  - Realistic: promising but still unproven at scale

### Philosophical Differences

**Internet Consensus Bias:**
- Favors implementation simplicity and quick ROI
- Emphasizes high-volume, repetitive task automation
- Focuses on cost reduction (replacing headcount)
- Vendor marketing drives coverage (support, sales tools dominate)

**Pass 3 Weighting Bias:**
- Favors cognitive sophistication and problem-solving depth
- Emphasizes iterative learning and multi-tool coordination
- Focuses on capability expansion (augmenting experts, not replacing workers)
- Recognizes that complex domains (security, finance, legal, healthcare) require more agent sophistication

### Strategic Implications

1. **If you want quick ROI:** Follow internet consensus (customer support, sales dev, HR)
2. **If you want technical leadership:** Focus on Pass 3 top performers (IT service desk + security ops + software engineering)
3. **The missing narrative:** Most internet coverage treats agentic AI as a cost-cutting tool; Pass 3 suggests greatest value is in capability amplification for complex domains

