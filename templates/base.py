from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Tuple


MCP_COMMAND = {
    "command": "uvx",
    "args": [
        "--refresh",
        "--python",
        "3.13",
        "--directory",
        ".",
        "--from",
        "git+https://github.com/geldata/gel-mcp.git",
        "gel-mcp"
    ]
}


class BaseTemplate(ABC):
    """Base template class for rendering Gel rules."""
    
    @abstractmethod
    def render(self, src_dir: Path, dst_dir: Path) -> None:
        """Render source files to destination directory."""
        pass
    
    def get_markdown_files(self, src_dir: Path):
        """Get all markdown files from source directory."""
        return list(src_dir.glob("*.md"))
    
    def parse_frontmatter(self, content: str) -> Tuple[Dict[str, str], str]:
        """Parse YAML frontmatter from markdown content."""
        if not content.startswith('---'):
            return {}, content
            
        lines = content.split('\n')
        end_idx = None
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                end_idx = i
                break
        
        if end_idx is None:
            return {}, content
            
        frontmatter_lines = lines[1:end_idx]
        frontmatter = {}
        for line in frontmatter_lines:
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip()
        
        body = '\n'.join(lines[end_idx + 1:])
        return frontmatter, body
