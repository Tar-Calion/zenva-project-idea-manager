from idea_manager.gemini_pro_client import GeminiProClient


class ProjectCharterGenerator:

    def generate(self):
        # Capture user input
        project_idea = input("Enter your project idea: ")

        # Generate project charter
        prompt = f"""Generate a Project Charter for the project Idea {project_idea}.

        Create appropriate content for this essential components:
        -Project Title
        -Project Description
        -Objectives
        -Constraints
        -Scope
        -Deliverables
        -Budget
        -Stakeholders
        -High-Level Risks and Assumptions

        Keep it short"""
        client = GeminiProClient()
        project_charter = client.generate_output(prompt)

        # Save project charter as Word document
