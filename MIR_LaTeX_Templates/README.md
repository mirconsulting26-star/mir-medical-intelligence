# MIR Medical Intelligence — LaTeX Templates

This package contains two reusable IEEE-style LaTeX templates for the MIR Medical Intelligence research program.

## 1. Research proposal

`proposal/mir_medical_intelligence_research_proposal.tex`

- Single-column.
- Designed as a comprehensive research-program proposal and roadmap.
- Includes scientific framing, research questions, hypotheses, dataset strategy, methodology, ML/DL/statistics, missingness, uncertainty, adaptive evidence acquisition, federated learning, agentic AI, architecture, work packages, roadmap, safety/regulation, governance, reproducibility, and publication strategy.
- Uses the two-researcher structure:
  - Mir AbdulRehman — Co-Research Lead — AI/ML & Software Engineering
  - Sababa Ateeq — Co-Research Lead — Biomedical & Medical AI

## 2. Research paper

`research_paper/mir_medical_intelligence_research_paper.tex`

- Double-column `IEEEtran` journal-style manuscript.
- Structured around a conventional scientific article: Introduction, Related Work, Materials and Methods, Model Development, Evaluation, Results, Discussion, Limitations, Clinical Safety/Ethics/Regulation, Reproducibility, Conclusion, declarations, author contributions, and references.
- The adaptive evidence-acquisition section can be removed for papers that do not study that track.

## Compile

From the package root:

```bash
cd MIR_LaTeX_Templates/proposal
pdflatex mir_medical_intelligence_research_proposal.tex
bibtex mir_medical_intelligence_research_proposal
pdflatex mir_medical_intelligence_research_proposal.tex
pdflatex mir_medical_intelligence_research_proposal.tex
```

For the paper:

```bash
cd ../research_paper
pdflatex mir_medical_intelligence_research_paper.tex
bibtex mir_medical_intelligence_research_paper
pdflatex mir_medical_intelligence_research_paper.tex
pdflatex mir_medical_intelligence_research_paper.tex
```

The two `.tex` files reference the shared bibliography at `shared/mir_references.bib`.

## Important IEEE note

These are deliberately built around `IEEEtran`. The proposal uses `onecolumn` because you requested a single-column research proposal; IEEE's own IEEEtran documentation notes that one-column mode is primarily a draft/proposal-style mode rather than the normal final publication format. The research paper uses the normal two-column journal-style configuration. Before submitting to any specific IEEE journal or conference, use that venue's current official template/instructions because IEEE states that publication-specific templates can differ.

## First edits you should make

1. Replace the placeholder ORCID values.
2. Replace the placeholder email and affiliation.
3. Update the title for each individual paper.
4. Replace every `%`/placeholder comment with study-specific content.
5. Add the exact datasets, versions, access dates, ethics details, and software versions used.
6. Maintain author contributions based on the actual work performed in each paper.
7. Expand `shared/mir_references.bib` as the project literature develops.

## Suggested project use

Keep the proposal as the evolving master research-program document. For each publishable study, copy the paper template into a separate manuscript directory and give it a study-specific name, for example:

`papers/01_laboratory_anomaly_detection/`

Then version the protocol, code, data documentation, experiment registry, manuscript, and release together.
