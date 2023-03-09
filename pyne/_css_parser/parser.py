import tinycss2
from tinycss2 import ast


def parse(css_style_sheet: str):
    rules = tinycss2.parse_stylesheet(css_style_sheet)

    result = {}

    _current_hash = ''
    for rule in rules:
        # Обработать заголовок.
        for token in rule.prelude:
            if isinstance(token, ast.IdentToken):
                result[token.serialize()] = {}
                if _current_hash:
                    result[token.serialize()]['hash'] = _current_hash
                    _current_hash = ''
            elif isinstance(token, ast.HashToken):
                _current_hash = token.serialize()

    return result


if __name__ == '__main__':
    print(parse('#main p { color: (0, 0, 0) }'))
