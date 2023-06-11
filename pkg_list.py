import pkg_resources

# Get a list of all installed packages
installed_packages = [pkg.key for pkg in pkg_resources.working_set]

# Filter the packages to include only Django modules
django_packages = [pkg for pkg in installed_packages if pkg.startswith('')]

# Create the recommended.txt file with version information
with open('recommended.txt', 'w') as file:
    file.write(f'# To activate this run \n#\n# pip install -r requirements.txt\n# python -m django --version\n#\n# On a Macintosh this should be python3 and pip3\n#\n')
    for package in django_packages:
        version = pkg_resources.get_distribution(package).version
        file.write(f"{package}=={version}\n")


print(f'recommended.txt file created successfully.')
