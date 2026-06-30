# Strip AI & Non-Essentials Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Remove all AI/automation code and non-essential files, leaving only manual annotation.

**Architecture:** Surgical deletion of AI files and non-essentials, then stripping AI references from core files (_app.py, canvas.py, __init__.py, config).

**Tech Stack:** Python 3.11+, PySide6, numpy, pillow, scikit-image

## Global Constraints

- Keep settings dialog and examples directory
- Remove translations, CI, tests, docs, dev tooling, AI agents configs
- osam dependency must be removed from pyproject.toml
- App must start and support all manual annotation modes after removal

---

### Task 1: Delete AI files and non-essential directories

**Files:**
- Delete: `labelme/_automation/` (entire dir)
- Delete: `labelme/_widgets/_ai_assisted_annotation_widget.py`
- Delete: `labelme/_widgets/_ai_text_to_annotation_widget.py`
- Delete: `labelme/_widgets/download.py`
- Delete: `.github/`
- Delete: `docs/` (except superpowers/specs/ and superpowers/plans/)
- Delete: `tests/`
- Delete: `tools/`
- Delete: `Makefile`
- Delete: `.out-of-scope/`
- Delete: `AGENTS.md`
- Delete: `CLAUDE.md`
- Delete: `CONTEXT.md`
- Delete: `CLA.md`
- Delete: `CITATION.cff`
- Delete: `CHANGELOG.md`
- Delete: `_typos.toml`

- [ ] Delete all listed files/directories in one batch commit

### Task 2: Clean labelme/__init__.py

- [ ] Remove `import onnxruntime` and the preceding comment
- [ ] Commit

### Task 3: Clean labelme/_widgets/__init__.py

- [ ] Remove imports and exports of AI widgets (`AiAssistedAnnotationWidget`, `AiTextToAnnotationWidget`, `download_ai_model`)
- [ ] Commit

### Task 4: Clean labelme/_config/default_config.yaml

- [ ] Remove AI model configuration keys
- [ ] Commit

### Task 5: Clean labelme/_app.py

- [ ] Remove AI widget imports
- [ ] Remove AI menu actions and toolbar integration
- [ ] Remove AI signal connections and slots
- [ ] Commit

### Task 6: Clean labelme/_widgets/canvas.py

- [ ] Remove AI-Points and AI-Box edit modes
- [ ] Remove AI inference trigger code
- [ ] Remove AI-related signals
- [ ] Commit

### Task 7: Clean pyproject.toml

- [ ] Remove `osam>=0.4.0` from dependencies
- [ ] Remove dev dependencies group
- [ ] Remove tool configs (ruff, pytest, etc.)
- [ ] Commit

### Task 8: Verify application starts and works

- [ ] Run `uv sync` to update lock file
- [ ] Run `python -m labelme` to verify no import errors
- [ ] Smoke test: open image, draw shapes, save/load JSON
- [ ] Commit final state
