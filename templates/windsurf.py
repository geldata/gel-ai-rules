import json
from pathlib import Path
from .base import BaseTemplate, MCP_COMMAND


class WindsurfTemplate(BaseTemplate):
    """Template for Windsurf editor."""
    
    def render(self, src_dir: Path, dst_dir: Path) -> None:
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        md_files = self.get_markdown_files(src_dir)
        
        windsurf_dir = dst_dir / ".windsurf"
        windsurf_dir.mkdir(exist_ok=True)
        
        mcp_config = {
            "mcpServers": {
                "gel": MCP_COMMAND
            }
        }
        (windsurf_dir / "mcp_example.json").write_text(json.dumps(mcp_config, indent=2))
        
        rules_dir = windsurf_dir / "rules"
        rules_dir.mkdir(exist_ok=True)
        
        for src_file in md_files:
            content = src_file.read_text()
            frontmatter, body = self.parse_frontmatter(content)
            
            windsurf_frontmatter = "---\n"
            windsurf_frontmatter += "trigger: model_decision\n"
            if "description" in frontmatter:
                windsurf_frontmatter += f"description: {frontmatter['description']}\n"
            windsurf_frontmatter += "---\n\n"
            
            full_content = windsurf_frontmatter + body
            
            (rules_dir / src_file.name).write_text(full_content) 