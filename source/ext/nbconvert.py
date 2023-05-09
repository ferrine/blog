"""Patching latest nbsphinx because i'm completely
not satisfied with how cells are managed.
"""
from nbsphinx import RST_TEMPLATE
from nbsphinx import setup
import nbsphinx
import re


BLOCK_REGEX = r"(({{% block {block} -%}}\n)(.*?)({{% endblock {block} %}}\n))"
PATCH_TEMPLATE = r"{{% block {block} -%}}\n{patch}{{% endblock {block} %}}\n"


def search(block, template):
    pattern = BLOCK_REGEX.format(block=block)
    m = re.search(pattern, template, re.DOTALL)
    assert m is not None, f"Block {block} is not found"
    return m.group(3)


def patch(block, template, patch):
    pattern = BLOCK_REGEX.format(block=block)
    sub = PATCH_TEMPLATE.format(block=block, patch=patch)
    return re.sub(pattern, sub, template, flags=re.DOTALL)


def remove_block_on_tag(block, tags, template):
    content = search(block, RST_TEMPLATE)
    conditions = [f"{t!r} in cell.metadata.tags" for t in tags]
    content1 = f"""\
{{%- if {" or ".join(conditions)} -%}}
{{%- else -%}}
{content}
{{%- endif -%}}
"""
    return patch(block, template, content1)


RST_TEMPLATE = remove_block_on_tag(
    "input", ["remove_cell", "remove_input"], RST_TEMPLATE
)
RST_TEMPLATE = remove_block_on_tag(
    "nboutput", ["remove_cell", "remove_output"], RST_TEMPLATE
)
nbsphinx.RST_TEMPLATE = RST_TEMPLATE
__all__ = ["setup"]
