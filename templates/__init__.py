"""
Templates package for rendering gel rules to different editor formats.
"""

from .base import BaseTemplate, MCP_COMMAND
from .claude_code import ClaudeCodeTemplate
from .vscode import VSCodeTemplate
from .cursor import CursorTemplate
from .windsurf import WindsurfTemplate
from .zed import ZedTemplate

__all__ = [
    "BaseTemplate",
    "MCP_COMMAND",
    "ClaudeCodeTemplate",
    "VSCodeTemplate",
    "CursorTemplate",
    "WindsurfTemplate",
    "ZedTemplate",
]
