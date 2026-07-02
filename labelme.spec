# -*- mode: python ; coding: utf-8 -*-
import os
from pathlib import Path

import labelme as _pkg

_SRC = Path(_pkg.__file__).parent

_a = Analysis(
    ['labelme_launcher.py'],
    pathex=[],
    binaries=[],
    datas=[
        (str(_SRC / "_config" / "default_config.yaml"), os.path.join("labelme", "_config")),
        (str(_SRC / "icons"), os.path.join("labelme", "icons")),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
_pyz = PYZ(_a.pure)

_exe = EXE(
    _pyz,
    _a.scripts,
    _a.binaries,
    _a.datas,
    [],
    name='labelme',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
