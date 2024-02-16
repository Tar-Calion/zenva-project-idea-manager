from idea_manager.gemini_pro_client import GeminiProClient
from idea_manager.project_charter_generator import ProjectCharterGenerator

# Capture user input
project_idea = input("Enter your project idea: ")

file_prefix = f"{project_idea.replace(' ', '_')}"

# Generate project charter
project_charter_generator = ProjectCharterGenerator(project_idea, file_prefix)
project_charter = project_charter_generator.generate()
