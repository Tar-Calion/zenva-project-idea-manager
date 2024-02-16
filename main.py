from idea_manager.gemini_pro_client import GeminiProClient
from idea_manager.project_charter_generator import ProjectCharterGenerator
from idea_manager.risk_management_plan_generator import RiskManagementPlanGenerator

# Capture user input
project_idea = input("Enter your project idea: ")

file_prefix = f"{project_idea.replace(' ', '_')}"

# Generate project charter
project_charter_generator = ProjectCharterGenerator(project_idea, file_prefix)
project_charter = project_charter_generator.generate()

# Generate risk management plan
# load file output\project_charter_Extra_lead_lining_in_refrigerators_as_an_emergency_atomic_bunker_.md
# project_charter = open("output/project_charter_Extra_lead_lining_in_refrigerators_as_an_emergency_atomic_bunker_.md", "r").read()
risk_management_plan_generator = RiskManagementPlanGenerator(project_charter, file_prefix)
risk_management_plan = risk_management_plan_generator.generate()

print("Project Charter and Risk Management Plan generated successfully!")
