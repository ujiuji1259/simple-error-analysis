import sys
from .convert_json_to_html import convert_json_to_table_html

def convert_table():
    json_path = sys.argv[1]
    output_dir = sys.argv[2]
    convert_json_to_table_html(json_path, output_dir)
