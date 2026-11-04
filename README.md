# TNBC Measurement Route Qualification — code and audit archive v1.0

This versioned archive accompanies the Nature Communications manuscript:
**Measurement route qualification links biological identity to clinical interpretation of transcriptomic biomarkers**.

Public repository: https://github.com/hjian2007-collab/tnbc-measurement-route-qualification

## Scope

The repository provides a submission-facing reproducibility layer for the frozen 23-signature registry, the MRQ audit trail, controlled raw-cell benchmark outputs, NeoTRIP three-workflow comparator, calibrated semi-synthetic benchmark, and I-SPY2 cohort-level workflow evaluation.

The repository intentionally does **not** redistribute third-party patient-level raw data. Public source datasets should be obtained from their original repositories. Processed submission-facing audit tables are included to permit verification of the reported headline results. The complete binary archive used for release/Zenodo deposition is retained separately as `tnbc-measurement-route-qualification-v1.0.zip`.

## Governance boundary

- Registry version: `TNBC-ImmuneStromal-LockedRegistry-v1.0`
- Registry freeze date: `2026-08-08`
- Canonical registry SHA-256: `d25800a0aa7f3cc2767e0607299e23e436fd2a60cd485dd774fd58cebf0eb136`
- A limited six-module pCR feasibility screen preceded the registry freeze. It is excluded from confirmatory claims and did not determine membership of the 23-signature registry.
- The complete MRQ hierarchy is a retrospective, outcome-blind formalization. No independent historical timestamp is claimed for the full hierarchy before all exploratory measurement analyses.
- I-SPY2 is used as an **independent cohort-level workflow evaluation**, not as independent validation of every individual signature.

See `config/analysis_lock_manifest.md` for the complete lock hierarchy.

## Reproduce the audit

From the repository root:

```bash
python -m pip install -r environment/requirements.txt
python tests/test_headline_results.py
```

Expected final line:

```text
Archive self-test complete: all headline checks passed.
```

The self-test verifies the canonical registry hash and the submission-facing headline results used in Figures 1, 3 and 6.

## Directory structure

```text
config/                         frozen registry and analysis-lock metadata
data/processed/raw_cell_benchmark/
data/processed/neotrip/
data/processed/ispy2/
data/processed/semi_synthetic/
environment/                    validated requirements/runtime
manifests/                      analysis and manuscript-version mapping
outputs/                        expected headline results and self-test log
scripts/python/                 verification implementation
tests/                          one-command self-test
```

## Important interpretation boundary

This repository reproduces and verifies the reported headline analyses. It does not convert the retrospective outcome-blind MRQ formalization into a prospectively preregistered clinical classifier. A statistically significant bulk association is not automatically a route-valid measurement of the biological object implied by its label.

## License

Custom code in this repository is released under the MIT License. Third-party datasets remain subject to their original terms.

## Release status

Repository v1.0 content is prepared and verified. A GitHub Release `v1.0` and Zenodo DOI are the remaining publication steps. The DOI will then be inserted into `CITATION.cff` and the manuscript Code availability statement.
