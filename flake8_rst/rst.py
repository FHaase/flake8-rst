import re
import textwrap

RST_RE = re.compile(
    r'(?P<before>'
    r'^(?P<indent> *)\.\. (code-block|sourcecode):: python\n'
    r'((?P=indent) +:.*\n)*'
    r'\n*'
    r')'
    r'(?P<code>(^((?P=indent) +.*)?\n)+)',
    re.MULTILINE,
)
INDENT_RE = re.compile('^ +(?=[^ ])', re.MULTILINE)
TRAILING_NL_RE = re.compile(r'\n+\Z', re.MULTILINE)


def find_sourcecode(src: str) -> str:
    for match in RST_RE.finditer(src):

        min_indent = min(INDENT_RE.findall(match['code']))
        trailing_ws_match = TRAILING_NL_RE.search(match['code'])

        trailing_ws = trailing_ws_match.group()
        code = textwrap.dedent(match['code'])
        line = src[:match.start()].count('\n') + match['before'].count('\n')
        yield f'{code.rstrip()}{trailing_ws}', len(min_indent), line
