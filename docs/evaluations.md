# Evaluation methods and recorded results

[← Project overview](../README.md) · [View Python example](../examples/matching_demo.py)

These are historical project records, not independently audited performance guarantees. Counts reflect each experiment's own corpus and should not be combined into one dataset-size claim.

## Results at a glance

| Evaluation | Scope / result |
|---|---|
| Parser benchmark | 8 models; 80 prompts; selected runs repeated 3 times |
| Best recorded parser run | 99.1% filter F1; 232/240 filter exact matches |
| Known-item retrieval | 13/13 trials; historical 4,967-candidate corpus |
| Extraction validation | 469 documents; historical value F1 0.8911, with later label-quality concerns |
| Label QA | 2,429 teacher labels reviewed by automated quality checks |
| OCR challenge cohort | 200 documents / 663 pages; no certified full-fidelity score claimed |

The sections below explain the scoring boundaries and evidence limitations.

## Prompt parsing

Eight distinct LLMs have non-synthetic benchmark artifacts: GLM-4.6, Claude Haiku 4.5, Mistral Large 2512, GPT-4o mini, Kimi K2 0905, GPT-5.1, DeepSeek V3.2, and Grok 4.3 (names as recorded in the July 8 artifacts).

The benchmark used 80 prompts; selected models/configurations were run three times for 240 cases. Scoring measured filter precision/recall/F1, filter exact match, missing/extra/wrong constraints, semantic coverage, per-family behavior, latency percentiles, tokens, and cost. Extra invented filters counted as false positives. Schema-unexpressible requests were tracked separately rather than charged to the model.

The best recorded rescored run, GLM-4.6, reported **0.991 filter micro-F1** and **232/240 (96.67%) filter exact match**. It is one historical run after iteration, not a claim that every model received identical tuning. The strict aggregate filter scorer merges branch filters; it does not by itself establish Boolean branch correctness. Separate query-expressiveness tests cover branch structure, negation, and related logic.

Other parser work included JSON-only/helper-tool comparisons, unified/sequential/parallel dispatch comparisons, repeated-run stability, and shadow comparisons with older parsing behavior. Historical shadow stability evidence included 315 prompts.

## Search and matching

- Needle-in-a-haystack: recorded live validation retrieved the intended candidate in **13/13 trials** against a **4,967-candidate historical corpus**. This is known-item retrieval testing, not proof of universal recall or long-context LLM performance.
- Domain-rule regression: rank/vessel specificity, credentials, exclusions, and related hard filters; recorded live vessel-specificity evaluation passed **48/48 cases**.
- Matching ambiguity and reviewer feedback are diagnostic inputs; they are not a substitute for an adjudicated matching benchmark.

## Extraction and fine-tuning

The selected NuExtract3 adapter trained on 1,463 examples with a 24,576-token context, rank-16 LoRA, and 21,233,664 trainable parameters (0.4656% of the recorded 4,560,499,200 parameters). Training-size experiments included 500, 1,000, and 1,463 examples.

Validation covered 469 documents with field-value precision/recall/F1, normalized agreement, JSON parse validity, schema validity, per-family breakdowns, and OCR-source/document-length slices. Deterministic schema repair was measured separately from raw generation. Targeted-SFT and document-type experiments used staged validation and baseline comparisons.

The historical baseline reported value F1 of 0.8911. Later audits found reference-label and convention problems; that number is not presented as a definitive current extraction-quality claim. Further training depends on resolving data and OCR evidence gaps.

## Teacher labels and grounding

Teacher-model calibration/bakeoffs compared coverage, disagreement, groundedness, output packaging, and cost. A label-quality sweep covered 2,429 labels. Mismatch audits investigated unsupported values, missing/extra table rows, normalization differences, document types, dates, and certificate coverage. Literal non-matches were review signals, not automatically proven hallucinations.

## OCR

A frozen challenge cohort contained 200 source documents / 663 pages. Work compared Gemini cached/fresh outputs, Mistral OCR, Docling, olmOCR, Chandra, and later Google Vision: seven experimental arms, not seven distinct OCR vendors.

Historical semantic diagnostics included critical-fact preservation and repeated-row/value-attachment checks. Later transcription diagnostics measured document/page alignment, token recall/support, and token error rates. The September 20 seven-arm scorecard used an unaudited reader transcript and explicitly declared no certified fidelity score, passed gate, or winner. Page-local comparison coverage also differed by arm.

These experiments support a claim of conducting OCR evaluation, not a claim of certified full-document OCR accuracy. Cost/latency records also distinguish cache replay, fresh inference, and batched operations.

## Engineering validation

Serial/batched extraction parity, isolated document failures, model artifact checks, worker health, approved/current eligibility, cache hydration/replacement/removal, failed-hydration last-good behavior, and hosted end-to-end smoke tests complement model evaluation.

## Not claimed as completed

Embedding-model benchmarking, quantization-quality comparison, a dedicated reasoning-model bakeoff, and the next corrected-gold retraining cycle are not claimed as completed here.
