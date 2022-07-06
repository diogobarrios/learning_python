def city_country(city, country, population=''):
    """Generate a neatly formatted city with his country"""
    if population:
        full_name = f"{city}, {country} - population {population}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()