import sys
import os


"""
This script generates the necessary HTML code for a new project and updates the `projects.html` file.
It also creates a new HTML file for the project with the appropriate content.

Usage:
Run the script from the terminal with the following arguments:
    python generate_project.py <project_name> <full_name> <description> <image_name> <pdf_name>

Arguments:
    <project_name>  - The name of the project (used for the HTML file, e.g., "time_series").
    <full_name>     - The full name of the project (e.g., "Time Series Analysis").
    <description>   - A brief description of the project.
    <image_name>    - The name of the image file (e.g., "time_series.png"). Place it in the "images" folder.
    <pdf_name>      - The name of the PDF file (e.g., "Time_Series_Project.pdf"). Place it in the "pdfs" folder.

Example:
    python generate_project.py time_series "Time Series Analysis" "Monthly evolution of the manufacturing of medical and dental instruments and supplies from January 1990 to January 2020." "time_series.png" "Time_Series_Project.pdf"

"""


def generate_project_code(project_name, full_name, description, image_name, pdf_name):
    # Generate the code for projects.html
    project_html_code = f"""
      <!-- {full_name} -->
      <div class="project-card">
        <img src="images/{image_name}" alt="{full_name}">
        <div class="project-content">
          <h3>{full_name}</h3>
          <p>{description}</p>
          <a href="{project_name}.html" class="btn small">See more</a>
        </div>
      </div>
"""
    # Generate the content for the project HTML file
    project_page_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{full_name} Project</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div class="resume-container">
    <header class="resume-header">
      <h1>{full_name} – Project Presentation</h1>
      <a href="projects.html" class="btn">← Back to projects</a>
    </header>

    <div style="width: 100%; height: 90vh; margin-top: 1rem;">
      <iframe src="pdfs/{pdf_name}" width="100%" height="100%" style="border: none;"></iframe>
    </div>
  </div>
</body>
</html>
"""
    return project_html_code, project_page_content

def main():
    if len(sys.argv) != 6:
        print("Usage: python generate_project.py <project_name> <full_name> <description> <image_name> <pdf_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    full_name = sys.argv[2]
    description = sys.argv[3]
    image_name = sys.argv[4]
    pdf_name = sys.argv[5]

    # Generate the code
    project_html_code, project_page_content = generate_project_code(project_name, full_name, description, image_name, pdf_name)

    # Append the code to projects.html 
    projects_file_path = "projects.html"
    if os.path.exists(projects_file_path):
        with open(projects_file_path, "r") as projects_file:
            lines = projects_file.readlines()
        
        insertion_index = len(lines) - 6
        lines.insert(insertion_index, project_html_code)
        
        with open(projects_file_path, "w") as projects_file:
            projects_file.writelines(lines)
        print(f"Code for {project_name} added to projects.html.")
    else:
        print(f"Error: {projects_file_path} not found.")
        sys.exit(1)

    # Create the project HTML file
    project_file_path = f"{project_name}.html"
    with open(project_file_path, "w") as project_file:
        project_file.write(project_page_content)
    print(f"File {project_file_path} created.")

if __name__ == "__main__":
    main()