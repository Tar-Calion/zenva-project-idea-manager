from idea_manager.gemini_pro_client import GeminiProClient
from idea_manager.project_charter_generator import ProjectCharterGenerator
from idea_manager.risk_management_plan_generator import RiskManagementPlanGenerator
from idea_manager.project_plan_generator import ProjectPlanGenerator

# Capture user input
project_idea = input("Enter your project idea: ")

file_prefix = f"{project_idea.replace(' ', '_')}"

# Generate project charter
project_charter_generator = ProjectCharterGenerator(project_idea, file_prefix)
project_charter = project_charter_generator.generate()

# Generate risk management plan
risk_management_plan_generator = RiskManagementPlanGenerator(project_charter, file_prefix)
risk_management_plan = risk_management_plan_generator.generate()

# Generate project plan
project_plan_generator = ProjectPlanGenerator(project_charter, file_prefix)
project_plan_generator.generate()

print("Project Charter and Risk Management Plan generated successfully!")
