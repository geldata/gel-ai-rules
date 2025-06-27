import json
from pathlib import Path
from .base import BaseTemplate, MCP_COMMAND


class VSCodeTemplate(BaseTemplate):
    """Template for VSCode editor."""

    def render(self, src_dir: Path, dst_dir: Path) -> None:
        dst_dir.mkdir(parents=True, exist_ok=True)

        md_files = self.get_markdown_files(src_dir)

        vscode_dir = dst_dir / ".vscode"
        vscode_dir.mkdir(exist_ok=True)

        file_instructions = []
        for md_file in md_files:
            file_instructions.append({"file": f"./gel-rules/{md_file.name}"})

        settings = {
            "github.copilot.chat.codeGeneration.instructions": file_instructions
        }
        (vscode_dir / "settings.json").write_text(json.dumps(settings, indent=2))

        mcp_config = {
            "servers": {
                "gel": {
                    "type": "stdio",
                    "command": MCP_COMMAND["command"],
                    "args": MCP_COMMAND["args"],
                }
            }
        }

        (vscode_dir / "mcp.json").write_text(json.dumps(mcp_config, indent=2))

        rules_dir = dst_dir / "gel-rules"
        rules_dir.mkdir(exist_ok=True)

        for src_file in md_files:
            content = src_file.read_text()
            frontmatter, body = self.parse_frontmatter(content)
            (rules_dir / src_file.name).write_text(body)
