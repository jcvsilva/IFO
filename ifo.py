#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse

# Create a parser for args
parser = argparse.ArgumentParser(description='Process torrents RAR\'s.')

# Add an argument
parser.add_argument('dir_arg', help='Directório a processar.')

# Parse arguments
args = parser.parse_args()

print(args.dir_arg)

dir_list = os.listdir(".")

for folder in dir_list:
    if os.path.isdir(folder):
        sub_dir_list = os.listdir(os.path.join(".", folder))
        # print(f'List sub: {sub_dir_list}')
        
        for image in sub_dir_list:
            try:
                os.mkdir(os.path.join(".", folder, "RAW"))
                # print("RAW created")
            except FileExistsError:
                # print("RAW already exists.")
                continue
            
        for image in sub_dir_list:
            if image.lower().endswith('.cr2'):
                # print(f'Old dir: {os.path.join(".", folder, image)} new dir: {os.path.join(".", folder, "RAW", image)}')
                os.rename(os.path.join(".", folder, image), os.path.join(".", folder, "RAW", image))
                
            