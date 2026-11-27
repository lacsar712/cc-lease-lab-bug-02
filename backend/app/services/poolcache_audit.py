"""资源池页缓存旧占用读轨审计。"""
from __future__ import annotations

from app.services import poolcache as core
from app.services import poolcache_cutover as cutover
from app.services import poolcache_dualwrite as dual


def audit_summary() -> dict:
    return {
        "title": "资源池页缓存旧占用审计",
        "core": core.dashboard(),
        "cutover": cutover.board(),
        "dualwrite": dual.dual_board(),
        "half": core.half_fix_display(),
    }
