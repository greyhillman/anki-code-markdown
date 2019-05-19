import re

from anki.hooks import addHook


def convert_block(html):
    return re.sub(r"(?<!\\)```(.+?)(?<!\\)```", "<div class=\"code\">\\1</div>", html)

def convert_inline(html):
    return re.sub(r"(?<![\\`])`(?!`)(.+?)(?<![\\`])`(?!`)", "<span class=\"code\">\\1</span>", html)

def remove_escapes(html):
    return re.sub(r"\\`", r"`", html)

def convert(html):
    return remove_escapes(convert_block(convert_inline(html)))

def prepare(html, card, context):
    return convert(html)

addHook("prepareQA", prepare)
