import json
from pathlib import Path
from .base import BaseTemplate, MCP_COMMAND


class ClaudeCodeTemplate(BaseTemplate):
    """Template for Claude Code editor."""
    
    def render(self, src_dir: Path, dst_dir: Path) -> None:
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        md_files = self.get_markdown_files(src_dir)
        
        claude_md = "# CLAUDE.md\n\n## Using Gel database\n\n"
        for md_file in md_files:
            claude_md += f"@gel-rules/{md_file.name}\n"
        claude_md += "\nUse Gel MCP server to find advanced code examples and run queries with args and globals.\n"
        
        (dst_dir / "CLAUDE.md").write_text(claude_md)
        
        mcp_config = {
            "mcpServers": {
                "gel": MCP_COMMAND
            }
        }
        (dst_dir / ".mcp.json").write_text(json.dumps(mcp_config, indent=2))
        
        rules_dir = dst_dir / "gel-rules"
        rules_dir.mkdir(exist_ok=True)
        
        for src_file in md_files:
            content = src_file.read_text()
            frontmatter, body = self.parse_frontmatter(content)
            (rules_dir / src_file.name).write_text(body)
