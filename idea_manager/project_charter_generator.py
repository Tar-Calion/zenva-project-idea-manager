from idea_manager.gemini_pro_client import GeminiProClient
from Markdown2docx import Markdown2docx
import textwrap


class ProjectCharterGenerator:

    def __init__(self, project_idea, file_prefix):
        self.project_idea = project_idea
        self.file_prefix = file_prefix

    def generate(self):

        # Generate project charter
        project_charter = self.__generate_project_charter(self.project_idea)

        # Save project charter
        self.__save_files(project_charter)

        return project_charter

    def __generate_project_charter(self, project_idea):
        prompt = textwrap.dedent(f"""\
            Generate a Project Charter for the project Idea: "{project_idea}".
            Create appropriate content for this components:
            -Project Title
            -Project Description
            -Objectives
            -Constraints
            -Scope
            -Deliverables
            -Budget
            -Stakeholders
            -High-Level Risks and Assumptions
            Keep it short. Use Markdown to format the chapters""")

        print("Prompt:", prompt)

        client = GeminiProClient()
        project_charter = client.generate_output(prompt)

        print("Project Charter:", project_charter)

        return project_charter

    def __save_files(self, project_charter):
        file_name = f"{self.file_prefix}_project_charter"

        # Save project charter as .md
        with open(f"output/{file_name}.md", "w") as file:
            file.write(project_charter)

        # Convert to docx
        markdown2docx = Markdown2docx(f"output/{file_name}")
        markdown2docx.eat_soup()
        markdown2docx.save()
