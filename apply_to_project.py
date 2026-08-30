import os
import sys
import shutil
import datetime

sys.stdout.reconfigure(encoding='utf-8')

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))

def apply_template_to_project(target_project_path, project_name=None):
    if not os.path.exists(target_project_path):
        print(f"Error: Target project directory does not exist: {target_project_path}")
        return False

    if not project_name:
        project_name = os.path.basename(os.path.normpath(target_project_path))

    today_str = datetime.date.today().strftime('%Y-%m-%d')
    print(f"=== Applying Master AI Context Template to: {project_name} ===")
    print(f"Target Path: {target_project_path}")

    # Copy files
    for item in os.listdir(TEMPLATE_DIR):
        if item in ['apply_to_project.py', '.git']:
            continue
        src = os.path.join(TEMPLATE_DIR, item)
        dest = os.path.join(target_project_path, item)
        if os.path.isdir(src):
            shutil.copytree(src, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dest)
        print(f"  ✓ Copied: {item}")

    # Replace placeholders in target AI_CONTEXT
    for root, dirs, files in os.walk(os.path.join(target_project_path, "AI_CONTEXT")):
        for f in files:
            if f.endswith(".md"):
                f_path = os.path.join(root, f)
                with open(f_path, "r", encoding="utf-8") as rf:
                    content = rf.read()
                content = content.replace("{{PROJECT_NAME}}", project_name)
                content = content.replace("{{DATE}}", today_str)
                with open(f_path, "w", encoding="utf-8") as wf:
                    wf.write(content)

    # Replace placeholders in root docs
    for root_file in ["AGENTS.md", "CLAUDE.md", "CHANGELOG_AI.md"]:
        r_path = os.path.join(target_project_path, root_file)
        if os.path.exists(r_path):
            with open(r_path, "r", encoding="utf-8") as rf:
                content = rf.read()
            content = content.replace("{{PROJECT_NAME}}", project_name)
            content = content.replace("{{DATE}}", today_str)
            with open(r_path, "w", encoding="utf-8") as wf:
                wf.write(content)

    print(f"\n==========================================")
    print(f"SUCCESS! Master AI Context initialized in: {target_project_path}")
    print(f"You can now open any AI tool in this project and type 'start'!")
    print(f"==========================================")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        name = sys.argv[2] if len(sys.argv) > 2 else None
        apply_template_to_project(target, name)
    else:
        print("Usage: python apply_to_project.py <Target_Project_Path> [Project_Name]")
