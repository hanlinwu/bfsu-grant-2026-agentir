# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Chinese academic grant proposal (校级科研基金项目申请书) written in LaTeX. The main deliverable is `main.pdf`, compiled from `main.tex`.

## Build Command

```bash
xelatex main.tex
```

The document requires **XeLaTeX** (not pdflatex) due to Chinese font support via `ctex`. The first line of `main.tex` declares `% !TEX program = xelatex`.

## Project Structure

- `main.tex` — The grant proposal document. Contains two parts: "项目设计论证" (sections 1–6: 选题依据, 研究内容, 思路方法, 创新之处, 预期成果, 参考文献) and "前期研究基础".
- `ideas.md` — Research direction brainstorming based on AgenticIR (agent-based image restoration). Contains five research directions to draw from.
- `references/` — Reference PDFs. All files here are for writing **content** inspiration, except `去年项目参考.pdf` which is specifically for **writing style** reference.

## Writing Rules

1. This is a grant proposal — follow the writing style demonstrated in `references/去年项目参考.pdf`.
2. Academic writing must be rigorous with proper citations.
3. **All cited references must be verified on Google Scholar as real publications.** If an arXiv paper has been formally published at a journal or conference, cite the formal publication info instead of the arXiv version.
4. The proposal has a 6000-character limit for Part 1 (项目设计论证) and 1000-character limit for Part 2 (前期研究基础).
5. Write in Chinese (the document language).

## LaTeX Formatting Notes

- Chinese fonts: SimSun (body), SimHei (headings/bold), KaiTi (italic), FangSong (monospace); English font: Times New Roman.
- Body text: 五号 (10.5pt) with 20pt line spacing. Section headings: 小四 (12pt). Part titles: 四号 (14pt).
- Paragraph indent is set to 2em within content sections. Page margins match the official template (left 2.86cm, right 3.17cm, top/bottom 2.54cm).
- Content is written inside `longtable` environments to match the official form layout.
- References should use .bib file and manage automatically. All citations must use superscript format (use `\supercite{}` or configure biblatex with `autocite=superscript`).
- In LaTeX, use `` for left double quotation marks and '' for right double quotation marks; use ` for left single quotation marks and ' for right single quotation marks.
