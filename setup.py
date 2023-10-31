import setuptools

setuptools.setup(
    name="foundational-ros-snap-generator",
    version="0.0.1",
    scripts=[
        "generate_all_ros_meta_snapcraft_file.py",
        "generate_package_xml_recursive_dependencies.py",
        "generate_ros_meta_snapcraft_file.py",
    ],
    install_requires=["catkin_pkg", "Jinja2", "rosdistro"],
)

