import site
import os

def find_package_path(package_name):
    for directory in site.getsitepackages():
        potential_path = os.path.join(directory, package_name)
        if os.path.exists(potential_path):
            return potential_path
    return None

print(find_package_path('langchain'))
print(find_package_path('langchain_openai'))