from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import subprocess
import shutil
import os

class BuildWithRust(build_py):
    def run(self):
        # Build the Rust library
        subprocess.check_call(['cargo', 'build', '--release'])
        
        # Copy the shared library to the package directory
        src = 'target/release/librelaxed_ik_lib.so'
        dst = 'relaxed_ik/librelaxed_ik_lib.so'
        os.makedirs('relaxed_ik', exist_ok=True)
        shutil.copy2(src, dst)
        
        super().run()

setup(
    name="relaxed-ik",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        'relaxed_ik': ['*.so', 'configs/*'],
    },
    include_package_data=True,
    python_requires=">=3.8",
    cmdclass={'build_py': BuildWithRust},
    author="Your Name",
    description="RelaxedIK inverse kinematics solver",
)