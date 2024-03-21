from .models import Company

def company_information(request):
    """
    Retrieve information about the company.

    Retrieves details about the company, including contact information, social media links, and services.

    Returns:
        Dictionary: General details about the company
    """
    company = Company.objects.first()  # Assuming there's only one company instance
    social_company = company.socialmedias.all()
    service_company = company.services.all()
    message_to_whatsapp = company.get_link_to_whatsapp("I'm interested in your professional services.")
    context = {
        'company_name': company.name,
        'company_location': company.location,
        'company_phone': company.phone_number,
        'company_email': company.email,
        'company_slogan': company.slogan,
        'company_social': social_company,
        'company_services': service_company,
        'company_get_started': message_to_whatsapp,
    }
    return context
