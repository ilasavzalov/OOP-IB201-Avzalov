class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.current_line = []
        self.current_length = 0
    def add_word(self, word):
        if self.current_length == 0:
            self.current_line.append(word)
            self.current_length = len(word)
        elif self.current_length + 1 + len(word) <= self.width:
            self.current_line.append(word)
            self.current_length += 1 + len(word)
        else:
            self.end()
            self.current_line.append(word)
            self.current_length = len(word)
    def end(self):
        if self.current_line:
            print(' '.join(self.current_line))
            self.current_line = []
            self.current_length = 0


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.current_line = []
        self.current_length = 0
    def add_word(self, word):
        if self.current_length == 0:
            self.current_line.append(word)
            self.current_length = len(word)
        elif self.current_length + 1 + len(word) <= self.width:
            self.current_line.append(word)
            self.current_length += 1 + len(word)
        else:
            self.end()
            self.current_line.append(word)
            self.current_length = len(word)
    def end(self):
        if self.current_line:
            line_text = ' '.join(self.current_line)
            spaces = self.width - len(line_text)
            print(' ' * spaces + line_text)
            self.current_line = []
            self.current_length = 0


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
