import json
from json.decoder import JSONDecodeError
from logging import getLogger
from pathlib import Path
from string import Template

from .templates import index_header, index_content, index_footer, table_page

logger = getLogger(__name__)

def create_table_templates(data):
    columns = list(data["meta"].keys())
    header_columns = [f"<th>{d}</th>" for d in columns]
    header_html = index_header.format("\n".join(header_columns))

    index_content_string = [f"<td>${d}</td>" for d in columns]
    index_content_template = Template(
        index_content.format(
            "\n".join(index_content_string)
        )
    )

    if not isinstance(data["data"], list):
        raise OSError

    table_columns = list(data["data"][0].keys())
    table_templates = Template(
        table_page.format(
            "\n".join([f"<th>{c}</th>" for c in table_columns])
        )
    )

    table_contents_template = Template(
        "\n".join(
            ["<tr>"] + [f"<td>${c}</td>" for c in table_columns] + ["</tr>"]
        )
    )

    return header_html, index_content_template, table_templates, table_contents_template

def convert_json_to_table_html(json_path, output_dir):
    json_path = Path(json_path)
    output_dir = Path(output_dir)

    if not json_path.exists():
        raise OSError("Json file not found")
    output_dir.mkdir(exist_ok=True)

    data = []
    try:
        with open(json_path, "r") as f:
            for line in f:
                line = line.rstrip()
                if not line:
                    continue
                line = json.loads(line)
                data.append(line)
    except JSONDecodeError as e:
        logger.error("Please follow data format in readme. JSONL is only accepted.")
        raise e

    header_html, index_content_template, table_templates, table_contents_template = create_table_templates(data[0])

    index_contents = []
    for idx, d in enumerate(data):
        _id = d.get("ID", idx)
        title = d.get("title", idx)

        table_contents = [table_contents_template.safe_substitute(**ta) for ta in d["data"]]
        _table = table_templates.safe_substitute(title=title, table="\n".join(table_contents))
        with open(output_dir / f"{_id}.html", "w") as f:
            f.write(_table)

        index_contents.append(
            index_content_template.safe_substitute(
                ID=_id, **d["meta"]
            )
        )

    with open(output_dir / "index.html", "w") as f:
        f.write("\n".join([header_html] + index_contents + [index_footer]))

if __name__ == "__main__":
    json_path = "/Users/ujiie/samples/sample.jsonl"
    output_dir = "/Users/ujiie/samples/htmls"
    convert_json_to_table_html(json_path, output_dir)