from idea_manager.gemini_pro_client import GeminiProClient
import textwrap
import openpyxl


class ProjectPlanGenerator:

    def __init__(self, project_charter, file_prefix):
        self.project_charter = project_charter
        self.file_prefix = file_prefix

    def generate(self):

        # Generate project plan
        project_plan = self.__generate_project_plan(self.project_charter)

        # Save project plan
        self.__save_files(project_plan)

    def __generate_project_plan(self, project_charter):
        prompt = textwrap.dedent(f"""\
            Generate a project plan as a table given the following project charter:
            BEGIN
            {project_charter}
            END
            Generate a table with following columns. Fill the table with tasks based on the project charter above.
            -Task name
            -Duration
            -Dependencies
            -Status
            -Resources""")

        print("Prompt:", prompt)

        client = GeminiProClient()
        project_plan = client.generate_output(prompt)

        print("Project plan:", project_plan)

        return project_plan

    def __save_files(self, project_plan):
        file_name = f"{self.file_prefix}_project_plan"

        parsed_project_plan = self.__parse_markdown_table(project_plan)

        self.__save_excel(parsed_project_plan, file_name)

    def __parse_markdown_table(self, markdown_table):
        lines = markdown_table.split("\n")
        table = []
        for line in lines[0:1] + lines[2:]:
            cells = line.split("|")
            cells = [cell.strip() for cell in cells if cell.strip()]
            table.append(cells)
        return table

    def __save_excel(self, parsed_project_plan, file_name):

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = "Project Plan"

        for row in parsed_project_plan:
            worksheet.append(row)

        workbook.save(f"output/{file_name}.xlsx")
