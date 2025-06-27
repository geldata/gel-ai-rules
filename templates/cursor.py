import json
from pathlib import Path
from .base import BaseTemplate, MCP_COMMAND


class CursorTemplate(BaseTemplate):
    """Template for Cursor editor."""

    def render(self, src_dir: Path, dst_dir: Path) -> None:
        dst_dir.mkdir(parents=True, exist_ok=True)

        md_files = self.get_markdown_files(src_dir)

        cursor_dir = dst_dir / ".cursor"
        cursor_dir.mkdir(exist_ok=True)

        mcp_config = {"mcpServers": {"gel": MCP_COMMAND}}
        (cursor_dir / "mcp.json").write_text(json.dumps(mcp_config, indent=2))

        rules_dir = cursor_dir / "rules"
        rules_dir.mkdir(exist_ok=True)

        for src_file in md_files:
            content = src_file.read_text()
            frontmatter, body = self.parse_frontmatter(content)

            cursor_frontmatter = "---\n"
            if "description" in frontmatter:
                cursor_frontmatter += f"description: {frontmatter['description']}\n"
            cursor_frontmatter += "globs:\nalwaysApply: false\n---"

            full_content = cursor_frontmatter + "\n" + body

            mdc_file = rules_dir / (src_file.stem + ".mdc")
            mdc_file.write_text(full_content)
