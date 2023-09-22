
def render_markdown(md_filepath):
    """
    collect markdown file content to render on each page
    as main content
    """
    with open(md_filepath, 'r') as md_obj:
        md_data = md_obj.read()
    return md_data