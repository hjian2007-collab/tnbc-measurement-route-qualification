# Analysis-lock manifest — TNBC Measurement Route Qualification

**Prepared:** 2026-11-04

**Purpose:** distinguish historically documented locks from retrospective outcome-blind formalization. This manifest is an audit document; it does not back-date or create historical preregistration.

## Governance principle

The registry freeze and its scoring/availability rules have a documented date and canonical SHA-256. The complete MRQ numerical hierarchy was formalized retrospectively from outcome-blind measurement analyses. Accordingly, the manuscript may state that clinical outcomes did not determine route construction and that reported downstream analyses used the formalized specification without outcome-driven rerouting, but it must not state that the complete MRQ hierarchy was prospectively preregistered before all exploratory analyses.

## Lock objects

### 1. Signature registry membership / gene membership
- **Status:** Historically documented hard lock
- **Documented date:** 2026-08-08
- **Version:** TNBC-ImmuneStromal-LockedRegistry-v1.0
- **Hash:** canonical SHA-256 d25800a0aa7f3cc2767e0607299e23e436fd2a60cd485dd774fd58cebf0eb136; binary file SHA-256 022b69b94632e182d0d9d162d76e70a685b58426964cd9786a70870a42a32be2
- **Evidence:** Registry README + Freeze_Manifest
- **Permitted claim:** Registry membership was frozen on 2026-08-08 before the formal 23-signature analysis; genes were not edited based on formal GSE194040 outcomes.
- **Not permitted:** The full MRQ route hierarchy was prospectively preregistered on 2026-08-08.

### 2. Scoring and gene-availability rules
- **Status:** Historically documented hard lock
- **Documented date:** 2026-08-08
- **Version:** Registry v1.0
- **Hash:** covered by canonical registry hash
- **Evidence:** Registry README + Freeze_Manifest
- **Permitted claim:** Response-blind within-dataset z-scoring, unweighted means, no substitution, and coverage rules were fixed with registry v1.0.
- **Not permitted:** All later MRQ thresholds were part of the same historical freeze.

### 3. Pre-freeze feasibility exception
- **Status:** Historically documented exception
- **Documented date:** before 2026-08-08
- **Version:** Feasibility-only six-module screen
- **Hash:** n/a
- **Evidence:** Registry README + Freeze_Manifest
- **Permitted claim:** A six-module outcome-informed feasibility screen occurred before registry freeze and is excluded from confirmatory claims.
- **Not permitted:** No outcome information had ever been inspected before registry freeze.

### 4. Primary I-SPY2 formal model / multiplicity policy
- **Status:** Documented in registry freeze manifest
- **Documented date:** 2026-08-08
- **Version:** Registry v1.0 formal analysis lock
- **Hash:** covered by canonical registry hash
- **Evidence:** Freeze_Manifest rows: primary model, interaction statistic, multiplicity
- **Permitted claim:** The formal I-SPY2 model family and BH-FDR policy were documented in the registry freeze manifest.
- **Not permitted:** Every later secondary/sensitivity model was prospectively specified on 2026-08-08.

### 5. MRQ numerical thresholds and hierarchical route specification
- **Status:** Retrospective outcome-blind formalization; no independent historical timestamp claimed
- **Documented date:** reported in manuscript v4 / audit manifest prepared 2026-11-04
- **Version:** MRQ specification as reported in manuscript v4
- **Hash:** to be represented by released archive commit/release hash
- **Evidence:** Manuscript Methods + registry-derived measurement analyses + code archive
- **Permitted claim:** The hierarchy was formalized retrospectively without using clinical outcomes and applied without outcome-driven rerouting in the reported benchmark and consequence analyses.
- **Not permitted:** The complete MRQ hierarchy was prospectively preregistered or independently time-stamped before all exploratory measurement analyses.

### 6. Controlled raw-cell generative-route benchmark
- **Status:** Evaluation under the reported MRQ specification
- **Documented date:** analysis record; seed 20261103
- **Version:** primary donor-split benchmark
- **Hash:** output tables/scripts to be frozen in public archive
- **Evidence:** Benchmark scripts/output; manuscript Methods
- **Permitted claim:** Benchmark outcomes were not used to reroute individual clinical signatures; benchmark tests known imposed generating mechanisms.
- **Not permitted:** The benchmark establishes natural biological ground truth for cell states.

### 7. Clinical consequence analyses (NeoTRIP / I-SPY2)
- **Status:** Outcome-aware downstream evaluation; route assignments not revised by these outcomes
- **Documented date:** downstream analysis records
- **Version:** three-workflow comparator / I-SPY2 cohort-level workflow evaluation
- **Hash:** output tables/scripts to be frozen in public archive
- **Evidence:** Step3 and Step4C outputs + code archive
- **Permitted claim:** Clinical outcomes assess consequences of the route interpretation; they do not define or revise individual routes.
- **Not permitted:** The clinical cohorts are independent prospective validations of a preregistered MRQ classifier.
