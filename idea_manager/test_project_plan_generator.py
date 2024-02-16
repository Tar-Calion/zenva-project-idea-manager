import unittest
from idea_manager.project_plan_generator import ProjectPlanGenerator
import textwrap


class TestProjectPlanGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ProjectPlanGenerator("None, None", "None")

    def test_parse_markdown_table(self):
        markdown_table = textwrap.dedent("""\
        | **Name** | **Age** | **Occupation** |
        |----------|---------|----------------|
        | John     | 25      | Engineer       |
        | Jane     | 30      | Doctor         |
        """)
        expected_result = [
            ['Name', 'Age', 'Occupation'],
            ['John', '25', 'Engineer'],
            ['Jane', '30', 'Doctor']
        ]
        self.assertEqual(self.generator._ProjectPlanGenerator__parse_markdown_table(markdown_table), expected_result)

    def test_parse_markdown_table_empty(self):
        markdown_table = ""
        expected_result = []
        self.assertEqual(self.generator._ProjectPlanGenerator__parse_markdown_table(markdown_table), expected_result)

    def test_parse_markdown_table_no_stars(self):
        markdown_table = textwrap.dedent("""\
        | Name | Age | Occupation |
        |------|-----|------------|
        | John | 25  | Engineer   |
        | Jane | 30  | Doctor     |
        """)
        expected_result = [
            ['Name', 'Age', 'Occupation'],
            ['John', '25', 'Engineer'],
            ['Jane', '30', 'Doctor']
        ]
        self.assertEqual(self.generator._ProjectPlanGenerator__parse_markdown_table(markdown_table), expected_result)

    def test_parse_markdown_table_with_empty_cells(self):
        markdown_table = textwrap.dedent("""\
        | **Name** | **Age** | **Occupation** |
        |----------|---------|----------------|
        | John     | 25      | Engineer       |
        | Jane     |         | Doctor         |
        """)
        expected_result = [
            ['Name', 'Age', 'Occupation'],
            ['John', '25', 'Engineer'],
            ['Jane', '', 'Doctor']
        ]
        self.assertEqual(self.generator._ProjectPlanGenerator__parse_markdown_table(markdown_table), expected_result)

    def test_parse_markdown_table_without_border(self):
        markdown_table = textwrap.dedent("""\
        **Name** | **Age** | **Occupation**
        ---------|---------|----------------
        John     | 25      | Engineer
        Jane     | 30      | Doctor
        """)
        expected_result = [
            ['Name', 'Age', 'Occupation'],
            ['John', '25', 'Engineer'],
            ['Jane', '30', 'Doctor']
        ]
        self.assertEqual(self.generator._ProjectPlanGenerator__parse_markdown_table(markdown_table), expected_result)


if __name__ == '__main__':
    unittest.main()
