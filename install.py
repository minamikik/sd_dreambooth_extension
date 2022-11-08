import shutil
import sys

from launch import run_pip, run
import os
from modules.paths import script_path

reqs = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
run_pip(f"install -r {reqs}", "requirements for Dreambooth")
python = sys.executable
torch_cmd = "pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 --extra-index-url https://download.pytorch.org/whl/cu116"
run(f'"{python}" -m {torch_cmd}', "Installing torch and torchvision", "Couldn't install torch")
if os.name == "nt":
    python = sys.executable
    bnb_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bitsandbytes_windows")
    site_dir = os.path.join(script_path, "venv", "Lib", "site-packages", "bitsandbytes")
    print("Copying 8Bit Adam files for Windows.")
    for file in os.listdir(bnb_dir):
        fullfile = os.path.join(bnb_dir, file)
        if file == "main.py":
            shutil.copy(fullfile, os.path.join(site_dir,"cuda_setup"))
        else:
            shutil.copy(fullfile, site_dir)