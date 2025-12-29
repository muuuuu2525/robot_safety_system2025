import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'robot_safety_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.py*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asano',
    maintainer_email='muuuuu2525@users.noreply.github.com',
    description='Robot safety system package for obstacle detection.',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'sensor = robot_safety_system.sensor_simulator:main',
            'brake = robot_safety_system.safety_brake:main',
        ],
    },
)
