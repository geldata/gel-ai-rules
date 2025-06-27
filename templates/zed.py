import json
from pathlib import Path
from .base import BaseTemplate, MCP_COMMAND


class ZedTemplate(BaseTemplate):
    """Template for Zed editor."""

    def render(self, src_dir: Path, dst_dir: Path) -> None:
        dst_dir.mkdir(parents=True, exist_ok=True)

        md_files = self.get_markdown_files(src_dir)

        rules_content = "## Using the Gel database\n\n"
        for md_file in md_files:
            rules_content += f"/file gel-rules/{md_file.name}\n"
        rules_content += "\nUse Gel MCP server to find advanced code examples and execute queries with args and globals.\n"

        (dst_dir / ".rules").write_text(rules_content)

        mcp_config = {
            "context_servers": {
                "gel": {
                    "source": "custom",
                    "command": {
                        "path": MCP_COMMAND["command"],
                        "args": MCP_COMMAND["args"],
                        "env": {},
                    },
                }
            }
        }
        zed_dir = dst_dir / ".zed"
        zed_dir.mkdir(exist_ok=True)
        (zed_dir / "settings.json").write_text(json.dumps(mcp_config, indent=2))

        rules_dir = dst_dir / "gel-rules"
        rules_dir.mkdir(exist_ok=True)

        for src_file in md_files:
            content = src_file.read_text()
            frontmatter, body = self.parse_frontmatter(content)
            (rules_dir / src_file.name).write_text(body)
