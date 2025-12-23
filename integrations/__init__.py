"""Integrations package for external API wrappers.

Keep thin wrappers here and import from Django apps (e.g. `scraper`).
"""

__all__ = ["google_maps"]

from . import google_maps  # noqa: F401
