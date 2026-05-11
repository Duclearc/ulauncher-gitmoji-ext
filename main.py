"""Ulauncher extension: search bundled gitmojis and copy code or emoji."""

from __future__ import annotations

import json
import os
from typing import Any

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.ActionList import ActionList
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "gitmojis.json")
ICON_PATH = os.path.join(os.path.dirname(__file__), "images", "icon.png")
INITIAL_LIMIT = 5
SEARCH_LIMIT = 25


def _copy_and_hide(text: str) -> ActionList:
    return ActionList([CopyToClipboardAction(text), HideWindowAction()])


def _parse_query(raw: str) -> tuple[bool, str]:
    """Return (list_all_mode, search_query_lower).

    ``list_all_mode`` is True for ``all`` or ``all <term>`` (case-insensitive).
    """
    raw = (raw or "").strip()
    lowered = raw.lower()
    if lowered == "all":
        return True, ""
    if lowered.startswith("all "):
        return True, raw[4:].strip().lower()
    return False, lowered


class GitmojiExtension(Extension):
    def __init__(self) -> None:
        super().__init__()
        with open(DATA_FILE, encoding="utf-8") as f:
            payload: dict[str, Any] = json.load(f)
        self.gitmojis: list[dict[str, Any]] = payload["gitmojis"]
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event: KeywordQueryEvent, extension: GitmojiExtension):
        list_all, query = _parse_query(event.get_argument() or "")
        fmt = extension.preferences.get("default_action", "code")

        def matches_entry(g: dict[str, Any]) -> bool:
            if not query:
                return True
            return any(
                query in str(g.get(k, "")).lower()
                for k in ("code", "name", "description")
            )

        matches = [g for g in extension.gitmojis if matches_entry(g)]
        if not list_all:
            if query:
                matches = matches[:SEARCH_LIMIT]
            else:
                matches = matches[:INITIAL_LIMIT]

        if not matches:
            return RenderResultListAction(
                [
                    ExtensionResultItem(
                        icon=ICON_PATH,
                        name="No gitmoji found",
                        description="Try another search-term or use 'gm all'",
                        on_enter=DoNothingAction(),
                    )
                ]
            )

        items: list[ExtensionResultItem] = []
        for g in matches:
            emoji = str(g.get("emoji", ""))
            code = str(g.get("code", ""))
            desc = str(g.get("description", ""))
            label = f"{emoji}  {code}"
            payload = emoji if fmt == "emoji" else code

            items.append(
                ExtensionResultItem(
                    icon=ICON_PATH,
                    name=label,
                    description=desc,
                    on_enter=_copy_and_hide(payload),
                )
            )

        return RenderResultListAction(items)


if __name__ == "__main__":
    GitmojiExtension().run()
