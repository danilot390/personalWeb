from django.shortcuts import render

from about.models import Company
def typeProject(portfolio):
    """
    Categorize the portfolio projects by project type.

    Arg:
        portfolio(list): List of portfolio projects.

    Returns:
        dict: Dictionary with project type as key and corresponding projects as values.
    """
    projects = {}

    for project in portfolio:
        try:
            projects[project.type.slang].append(project)
        except KeyError:
            projects[project.type.slang] = [project]

    return projects

def load_about (request):
    """
    Render the About Us page with information about the company.

    Retrieves details about the company, including mission and vision,
    skills, values, portfolios and services.

    Args:
        request(HttpRequest): The request object.
    Return:
        HttpResponse: Rendered template with context data.
    """
    # Retrieve the Company detail
    company = Company.objects.first()
    employees = company.employees.all()

    # Extract portfolios from employees
    portfolio = [portfolio for employee in employees for portfolio in employee.portfolio.all()]

    # Extract unique project types from portfolio
    project_type = {project.type_project.slang for project in portfolio}

    # Extract unique skills from the employees
    skill_employees = {skill.skill for employee in employees for skill in employee.skills.all()}


    # Preparea the context dictionary
    context = {
        'company' : company,
        'employees' : employees,
        'portfolio' : portfolio,
        'type_project' : project_type,
        'skills_company' : skill_employees,
    }

    # Render the template with the context
    return render(request, 'about_templates/about.html', context)

