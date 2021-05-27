import sys
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


def format(color, style=''):
    _color = QColor()
    _color.setNamedColor(color)
    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    if('under' in style):
        _format.setFontUnderline(True)
    return _format


STYLES = {
    'dot': format("#ff99ff", 'bold'),
    'keyword': format('orange', 'bold'),
    'brace': format('yellow'),
    'imm': format('white'),
    'comment': format('grey', 'italic'),
    'registers': format('lightblue'),
    'label': format('#66ff99'),
    'string': format('white')
}


class PythonHighlighter(QSyntaxHighlighter):    
    keywords = ["add","sub","xor","or","and","sll","srl","sra","slt","addi","ori","andi","lb","lh","lw","sb","sh","sw","beq","bne","blt","bge","jal","jalr","lui","auipc","mul","div","rem"]
    braces = ['\(', '\)']

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)
        rules = []
        rules += [(r'\b%s\b' % w, 0, STYLES['keyword']) for w in PythonHighlighter.keywords]
        rules += [(r'%s' % b, 0, STYLES['brace']) for b in PythonHighlighter.braces]
        rules += [(r'\bx(([0-9])|([1-2][0-9])|(3[0-1]))\b', 0, STYLES['registers']),]
        rules += [(r'\.[^\n]+', 0, STYLES['dot'])]
        rules += [(r'[^\n]+:', 0, STYLES['label'])]
        rules += [(r'\b[0-9]+\b', 0, STYLES['imm'])]
        rules += [(r'\b0x[0-9A-Fa-f]+\b', 0, STYLES['imm'])]
        rules += [(r'\b0b[0-1]+\b', 0, STYLES['imm'])]
        rules += [(r'\".*\"', 0, STYLES['string'])]
        rules += [(r'#[^\n]*', 0, STYLES['comment'])]
        self.rules = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
