from setuptools import find_packages, setup

package_name = 'medical_rover_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),

    ('share/' + package_name,
        ['package.xml']),

    ('share/' + package_name + '/launch',
        ['launch/bringup.launch.py']),

    ('share/' + package_name + '/config',
        []),

    ('share/' + package_name + '/rviz',
        []),

    ('share/' + package_name + '/launch',
    ['launch/bringup.launch.py',
    'launch/slam.launch.py']),

    ('share/' + package_name + '/config',
    ['config/slam.yaml']),
    
    ],

    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='saiyyam',
    maintainer_email='saiyyamjain9@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
