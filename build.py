from src.create_page import render_website, create_directory_if_not_exist
import os
import yaml
TEMPLATE_DIR = "templates"
BUILD_DIR = "dist"

def init():
    create_directory_if_not_exist(TEMPLATE_DIR)
    create_directory_if_not_exist(os.path.join(TEMPLATE_DIR, "content"))
    create_directory_if_not_exist(os.path.join(TEMPLATE_DIR, "elements"))
    create_directory_if_not_exist(os.path.join(TEMPLATE_DIR, "static"))
    create_directory_if_not_exist(BUILD_DIR)


if __name__ == "__main__":
    init()
    render_website(TEMPLATE_DIR, BUILD_DIR)
