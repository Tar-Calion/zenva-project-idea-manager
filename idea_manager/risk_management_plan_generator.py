from idea_manager.gemini_pro_client import GeminiProClient
from Markdown2docx import Markdown2docx


class RiskManagementPlanGenerator:

    def __init__(self, project_charter, file_prefix):
        self.project_charter = project_charter
        self.file_prefix = file_prefix

    def generate(self):

        # Generate risk management plan
        risk_management_plan = self.__generate_risk_management_plan(self.project_charter)

        # Save risk management plan
        self.__save_files(risk_management_plan)

    def __generate_risk_management_plan(self, project_charter):
        prompt = (f"Act as a senior project manager with experience in software projects."
                  " Write a risk assessment plan that identifies assesses and outlines strategies"
                  " to manage risks in the project based on the following charter:\n"
                  f"BEGIN\n"
                  f"{project_charter}\n"
                  f"END")

        print("Prompt:", prompt)

        client = GeminiProClient()
        risk_management_plan = client.generate_output(prompt)

        print("Risk management plan:", risk_management_plan)

        return risk_management_plan

    def __save_files(self, risk_management_plan):
        file_name = f"{self.file_prefix}_risk_management_plan"

        # Save project charter as .md
        with open(f"output/{file_name}.md", "w") as file:
            file.write(risk_management_plan)

        # Convert to docx
        markdown2docx = Markdown2docx(f"output/{file_name}")
        markdown2docx.eat_soup()
        markdown2docx.write_html()
