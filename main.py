from pathlib import Path
from templates.claude_code import ClaudeCodeTemplate
from templates.vscode import VSCodeTemplate
from templates.cursor import CursorTemplate
from templates.windsurf import WindsurfTemplate
from templates.zed import ZedTemplate


def main():
    src_dir = Path("src")
    rendered_dir = Path("rendered")
    
    templates = {
        "claude_code": ClaudeCodeTemplate(),
        "vscode": VSCodeTemplate(), 
        "cursor": CursorTemplate(),
        "windsurf": WindsurfTemplate(),
        "zed": ZedTemplate()
    }
    
    for editor_name, template in templates.items():
        editor_dir = rendered_dir / editor_name
        template.render(src_dir, editor_dir)
        print(f"{editor_name} rendered to {editor_dir}")


if __name__ == "__main__":
    main()
