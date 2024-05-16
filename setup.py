from setuptools import setup, find_packages
import subprocess
import site, os

def parse_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]
    
requirements = parse_requirements('requirements.txt')

site_packages_dir = site.getsitepackages()[0]

clone_path = os.path.join(site_packages_dir, 'ArtSnake', 'deep-blind-watermark-removal')

os.makedirs(clone_path, exist_ok=True)

subprocess.run(['git', 'clone', 'https://github.com/vinthony/deep-blind-watermark-removal.git', clone_path])

setup(
    name='ArtSnake',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    url='https://github.com/MekhyW/ArtSnake',
    license='MIT',
    author='Andre Melo, Felipe Catapano and Rafael Katri',
    author_email='your@email.com',
    description='A brief description of your library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
)
