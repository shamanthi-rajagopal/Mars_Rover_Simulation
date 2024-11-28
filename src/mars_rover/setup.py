from setuptools import setup

package_name = 'mars_rover'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Shamanthi',
    maintainer_email='s2rajago@uwaterloo.ca',
    description='A ROS 2 package for controlling a Mars rover.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rover_control = mars_rover.rover_control:main',
        ],
    },
)
