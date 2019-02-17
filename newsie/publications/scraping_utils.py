def strip_tags(html):
    content = ''
    for node in html:
        content += ''.join(node.findAll(text=True)) + ' '

    content = content[:-1]
    return content