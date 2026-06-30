# Design: Strip AI & Non-Essentials from LabelMe

**Date:** 2025-06-30
**Status:** Approved
**Approach:** Surgical removal (Approach A)

## Goal

Remove all AI/automation functionality and non-essential files from the labelme fork, leaving only manual shape annotation.

## Files to Delete

### AI engine
- `labelme/_automation/` — entire directory (7 files: `__init__.py`, `_ai_assist.py`, `_osam_session.py`, `_text_detection.py`, `_shape_builders.py`, `_geometry.py`, `_suppression.py`, `_types.py`)

### AI widgets
- `labelme/_widgets/_ai_assisted_annotation_widget.py`
- `labelme/_widgets/_ai_text_to_annotation_widget.py`
- `labelme/_widgets/download.py`

### Non-essentials
- `.github/` — CI/CD workflows
- `docs/` — documentation
- `tests/` — test suite
- `tools/` — translation updater
- `Makefile` — dev targets
- `.out-of-scope/` — unknown, non-essential
- `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md` — AI agent configs
- `CLA.md`, `CITATION.cff`, `CHANGELOG.md` — non-functional metadata
- `_typos.toml` — spell check config

## Files to Modify

### `labelme/__init__.py`
- Remove `import onnxruntime` and the preceding comment about DLL load order

### `labelme/_widgets/__init__.py`
- Remove imports/exports of `AiAssistedAnnotationWidget`, `AiTextToAnnotationWidget`, `download_ai_model`

### `labelme/_app.py`
- Remove imports: `AiAssistedAnnotationWidget`, `AiTextToAnnotationWidget`, anything from `_automation`
- Remove AI menu actions (model download, etc.)
- Remove AI toolbar integration (AI-assisted and text-to-annotation toolbars)
- Remove signal connections for AI widgets (e.g., `inferenceRequested`)
- Remove AI-related state variables and slots

### `labelme/_widgets/canvas.py`
- Remove AI-Points drawing mode (`EditMode.AI_POINTS`)
- Remove AI-Box drawing mode (`EditMode.AI_BOX`)
- Remove AI inference trigger code (calling back into MainWindow for AI)
- Remove AI-related mouse/key event handling
- Remove `inference_failed`, `inference_produced_no_shapes` signals/slots

### `labelme/_config/default_config.yaml`
- Remove AI model configuration keys (model ID, output format defaults)

### `pyproject.toml`
- Remove `osam>=0.4.0` from dependencies
- Remove dev dependencies group entirely
- Remove tool configs (ruff, pytest, etc.)
- Keep only `[build-system]` and `[project]` with core runtime deps

## Files Left Untouched

### Core shape system
- `labelme/_shape.py`
- `labelme/_shape_clipboard.py`
- `labelme/_label_file.py`

### Core widgets
- `labelme/_widgets/canvas.py` (manual modes only)
- `labelme/_widgets/label_dialog.py`
- `labelme/_widgets/label_list_widget.py`
- `labelme/_widgets/unique_label_qlist_widget.py`
- `labelme/_widgets/tool_bar.py`
- `labelme/_widgets/zoom_widget.py`
- `labelme/_widgets/brightness_contrast_dialog.py`
- `labelme/_widgets/settings_dialog.py`
- `labelme/_widgets/_shape_render.py`
- `labelme/_widgets/_canvas_interaction.py`
- `labelme/_widgets/_status.py`
- `labelme/_widgets/_info_button.py`

### Config & utilities
- `labelme/_config/` (with AI defaults removed from yaml)
- `labelme/_utils/`
- `labelme/_locale.py`
- `labelme/_yaml.py`

### Entry points
- `labelme/__main__.py`
- `labelme/_app.py` (with AI stripped)

### User-requested keeps
- `examples/`

### Project files
- `pyproject.toml` (cleaned)
- `README.md`
- `LICENSE`
- `.gitignore`
- `.gitmodules`
- `.git-blame-ignore-revs`
- `.python-version`
- `uv.lock` (regenerated)

## Risks

- **Canvas._app.py coupling:** `canvas.py` calls back into `_app.py` for AI inference. These callbacks must be cleanly removed without breaking manual drawing flows.
- **DLL load order hack:** `__init__.py` imports `onnxruntime` before PySide6 on Windows. Removing this is safe since onnxruntime is only needed for AI models via osam.
- **Config migration:** Users with existing config files containing AI keys will see warnings; the config loader already handles unknown keys gracefully.

## Verification

After removal, the app must:
1. Start without import errors
2. Open images via File > Open
3. Draw rectangles, polygons, circles, lines, points, linestrips, oriented rectangles
4. Edit/delete existing shapes
5. Use zoom, pan, brightness/contrast
6. Save and reload LabelMe JSON annotations
7. Open settings dialog without AI-related tabs/options
