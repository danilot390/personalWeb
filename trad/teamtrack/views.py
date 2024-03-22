from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

def profile_team (request,id):
    """
    View function to display a team member's profile.

    Retrieves information about the team member, including profile, contact details,
    social media links, and portfolio. Renders the 'teamtrack/profile.html' template
    with the retrieved data.

    Args:
        request: The request object
        id: The ID of the user

    Returns:
        HttpResponse: Rendered template response
    """
    try: 
        # Retrieve the user with the given id, or return a 4004 response if not found
        user = get_object_or_404(User, pk=id)
        
        # Retrieve profile information for the user
        profile = user.profiles.first()
        contact = user.contacts.first()
        linkedin = user.socialmedias.get(slug='linkedin')
        git = user.socialmedias.get(slug='git')

        # Determine the profile image to use
        img_profile = profile.image.url if profile.image else user.employee.first().image.url
        
        # Retrieve formation, experiences, achievements, references, and portfolio for the user
        formation = profile.formations.all()
        experience = profile.experiences.all()
        achievement = profile.achievements.all()
        reference = profile.references.all()
        portfolio = user.employee.first().portfolio.all()

        # Retrieve Keywords from experiences, formations, and portfolio
        keyword = set([keyword.strip() for exp in experience for keyword in exp.keywords().split(',')])
        keyword = keyword.union(set([keyword.strip() for item in formation for keyword in item.keywords().split(',')]))
        keyword = keyword.union(set([keyword.strip() for project in portfolio for keyword in project.keywords().split(',')]))
        keyword = ', '.join(keyword)
    
        # Prepare information dicitionary
        information = {
            'Name' : profile.user.get_full_name(),
            'Profession' : profile.profession,
            'Phone' : contact.phone_number,
            'Email' : profile.user.email,
            'LinkedIn' : linkedin.url,
            'Git' : git.url,
            'High' : profile.highlight,
            'Location' : contact.location,
            'Profile' : profile.profile,
            'Img_profile' : img_profile,
            'Keywords' : keyword,
        }


        # Prepare the context dictionary
        context = {
            **information,
            'formations' : formation,
            'experiences' : experience, 
            'achievements' : achievement,
            'references' : reference,
            'portfolio' : portfolio,
        }
        # Render the template with the context
        return render(request, 'teamtrack/profile.html', context)
    except User.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'User profile not found'})
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})
