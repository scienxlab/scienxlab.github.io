import sys
import glob
import re


def simplify_credits(html):
    """
    Replace the credit part of the HTML footer. Return the new text.
    """
    s = r'<a class="muted-link" href="https://pradyunsg\.me">@pradyunsg</a>\'s'
    pattern = re.compile(s)
    html = pattern.sub(r'', html)

    s = r'Copyright &#169; 2023, Scienxlab'
    pattern = re.compile(s)
    new_s = '&#169; 2023, Scienxlab | <a href="https://creativecommons.org/licenses/by/4.0/">CC BY</a>'
    html = pattern.sub(new_s, html)

    return html


def add_analytics(html):
    """
    Add snippet to head.
    """
    s = r'</head>'
    pattern = re.compile(s)
    new_s = '<script defer data-domain="code.scienxlab.com" src="https://plausible.io/js/plausible.js"></script></head>'
    html = pattern.sub(new_s, html)

    return html


def main(path):
    """
    Process the HTML files in path, save in place (side-effect).
    """
    fnames = glob.glob(path.strip('/') + '/*.html')
    for fname in fnames:
        with open(fname, 'r+') as f:
            html = f.read()

            new_html = simplify_credits(html)
            new_html = add_analytics(new_html)

            f.seek(0)
            f.write(new_html)
            f.truncate()
    return


if __name__ == '__main__':
    _ = main(sys.argv[1])
