import json
from enum import Enum, auto

import tinycss2
from tinycss2 import ast


class StateWaiting(Enum):
    KEY = auto()
    VALUE = auto()
    COLON = auto()


def parse(css_style_sheet: str):
    rules = tinycss2.parse_stylesheet(css_style_sheet)

    result = {}

    for rule in rules:
        current_hash = ''
        current_name = ''
        # Обработать заголовок.
        for token in rule.prelude:
            if isinstance(token, ast.IdentToken):
                result[token.serialize()] = {}
                current_name = token.serialize()
                if current_hash:
                    result[token.serialize()]['hash'] = current_hash
                    current_hash = ''
            elif isinstance(token, ast.HashToken):
                current_hash = token.serialize()

        current_key = ''
        current_value = None
        state = StateWaiting.KEY
        result[current_name]['value'] = {}
        # Обработать тело.
        for token in rule.content:
            if token.type == 'whitespace' or token.type == 'comment':
                pass
            elif state == StateWaiting.KEY and token.type == 'ident':
                current_key = token.serialize()
                state = StateWaiting.COLON
            elif state == StateWaiting.COLON and token.type == 'literal' and token.value == ':':
                state = StateWaiting.VALUE
            elif state == StateWaiting.VALUE:
                match token.type:
                    case 'number':  # число
                        current_value = token.value
                    case 'percentage' | 'dimension':  # именованное значение
                        current_value = token.serialize()
                    case '() block':  # кортеж
                        current_value = token.serialize().replace('(', '[').replace(')', ']')  # преобразуем в список
                        current_value = json.loads(current_value)
                    case '[] block' | '{} block':  # список или словарь
                        current_value = json.loads(token.serialize())

                result[current_name]['value'][current_key] = current_value
                current_key = ''
                current_value = None

    return result


if __name__ == '__main__':
    print(parse('#main p { color: (0, 0, 0) }'))
