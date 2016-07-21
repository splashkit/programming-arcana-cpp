#!/usr/bin/env python
# encoding: utf-8
"""
EEBNFTokeniser.py

Created by Andrew Cain on 2011-04-05.
Copyright (c) 2011 Andrew Cain. All rights reserved.
"""

import sys
import logging
logger = logging.getLogger("EEBNFTokeniser")

class EEBNFTokeniser():
    
    def __init__(self):
        self._lines = []                        # the file as an array of lines
        self._token_start = -1                  # the position of the start of this token
        self._char_no = -1                      # current character position in line
        self._line_no = 0                       # current line number
        self._filename = 'supplied data'        # name of the file being tokenised
        self._escape_table = {
            "{": "\{",
            '}': "\}",
            # "[": "\[",
            # "]": "\]",
            '\\': "{\\textbackslash}",
            '_': "\_",
            '#': "\#",
            '%': "\%",
            '&': "\&",
            '^': "\^{}",
            }
        
    
    def tokenise(self, filename):
        '''
            Initialises the tokeniser with characters loaded from the specified 
            filename. Call `next_token` process each token.
        '''
        
        if isinstance(filename, list):
            logger.debug('Tokenising list')
            self._lines = filename
        else:
            logger.debug('Tokenising %s', filename)
            self._filename = filename
            f = open(filename)
            self._lines = f.readlines()
            f.close()
        
        self._char_no = -1
        self._line_no = 0 #starts at first line
        self._token_val = 'none'
    
    
    
    def line_details(self):
        '''
            Returns a string with character position, line no. and filename details from
            the current position of the tokeniser.
        '''
        return 'char %d line %d in %s' % (self._token_start + 1, self._line_no + 1, self._filename)
    
    
    
    def _next_char(self):
        '''
            Returns the next character from the input file.
        '''
        self._char_no += 1
        # print self._char_no, ' ', self._line_no
        if len(self._lines) <= self._line_no:
            return '\0'
        if len(self._lines[self._line_no]) <= self._char_no:
            return '\n'
        return self._lines[self._line_no][self._char_no]
    
    def _peek(self, chars):
        '''
            Return a string with next number of "chars" line or \\n if at or 
            past the line end.
        '''
        if len(self._lines[self._line_no]) <= self._char_no + 1:
            result = '\n'
        else:
            result = self._lines[self._line_no][self._char_no + 1:self._char_no + chars + 1]
        #print 'peeking at', result
        return result
    
    def _peekNextChar(self):
        n = 1
        ch = self._peek(n)
        
        while ch == ' ' or ch == '/t':
            n = n + 1
            ch = self._peek(n)
        return ch
    
    def _read_matching(self, start, match_fn):
        '''
            Return a string starting with the "start" character and moving
            along the current line (increasing self._char_no) until the match_fn 
            returns True on the current new character of the line. Result does 
            *not* include the last matched character. 
        '''
        result = start
        cha = self._next_char();
        #print 'matching', cha
        while match_fn(cha, result):
            result += cha
            cha = self._next_char();
            #print 'matching', cha
        self._char_no -= 1 #step back
        return result

    def _advance_line(self):
        '''
            Move the line index to the next line. Reset the line character no to
            the initial value (-1).
        '''
        self._line_no += 1
        self._char_no = -1
    
    def _read_until(self, start, end_fn):
        '''
            Return a string starting with (and including) the "start" character
            and moving along the stream of file characters (across multiple lines 
            if needed) and stopping when the end_fn returns True on the current result
            of characters. 
        '''
        result = start
        cha = self._next_char();
        result += cha
        #print 'until', result
        while not end_fn(result):
            if cha == '\n':
                self._advance_line()
            cha = self._next_char();
            result += cha
            #print 'until', result
        #self._char_no -= 1 #step back
        return result

    def _match_and_read(self, cha):
        '''
            Looks at (peeks) the next character so see if it matches `cha`. 
            If `cha` does match then the character cursor is moved and True is 
            returned, otherwise False is returned.
        '''
        #print 'matching and reading', cha, ' = ', self._peek(1)
        if self._peek(1) == cha:
            self._next_char()
            return True
        else:
            return False

    def _escape(self, text):
        """Produce entities within text."""
        return "".join(self._escape_table.get(c,c) for c in text)

    def read_to_eol(self):
        '''
            Read and return a string with the rest of the current line, 
            stripped of any starting or trailing whitespace characters. The cursor 
            is advanced to the next line.
        '''
        result = self.pas_lines[self._line_no][self._char_no + 1:-1]
        self._advance_line()
        return result.strip()

    def read_to_end_of_comment(self):
        '''
            Read and return a string starting from the current cursor position
            and reading up to end of the "comment" section. Leading whitespace is stripped. 
            (*...*)
        '''
        comment_text = self._read_until('', lambda txt: txt[-2:] == "*)" )
        
        return comment_text[:-2].strip()


    def next_token(self):
        '''Find and return a tuple with the next token details. Tuple contains 
        the token (type, value) as strings. The token types and details are: 
        
            number,       # such as 1234, 123.45, -123, +123.4
            comment,      # (* ... *)
            terminal,     # "terminal" or 'terminal'
            non terminal, # non terminal
            symbol,       # one of '{}(),[]*+|~$'
            
        '''
        
        while (True):
            t = self._next_char();
            # print '*',t,'*', t == '\n'
            
            self._token_start = self._char_no
            
            # Ignore white space characters
            if t == ' ' or t == '\t':
                pass
            # Move to next line (if at end of line)
            elif t == '\n': 
                self._advance_line()
            # Numbers (integer only, no sign)
            elif t in '1234567890':
                result = ('number', self._read_matching(t, lambda cha, tmp: cha in '1234567890'))
                logger.debug('Tokenisier: read %s - %s', result[0], result[1])
                return result
            # Comment, single line // or meta comment line ///
            elif t == '(' and self._peek(1) == '*': #start of comment
                if self._match_and_read('*'):
                    comment = self.read_to_end_of_comment()
                    result = ('comment', comment)
                else:
                    result = ('error', t)
                logger.debug('Tokenisier: read %s', result[0])
                return result
            # Identifier (id) of alphanumeric characters including 
            elif t.isalpha():
                name = self._read_matching(t, lambda cha, tmp: cha not in ",(){}[]=;+*|")
                result = ('id', name.strip())
                logger.debug('Tokenisier: read %s - %s', result[0], result[1])
                return result
            # Symbol
            elif t in '(),[]{}=;+*|~$':
                result = ('symbol', t)
                logger.debug('Tokenisier: read %s - %s', result[0], result[1])
                return result
            # Catch any single quotes inside a string value.
            elif t == "'":
                string = self._read_until('', lambda temp: temp[-1:] == "'")
                result = ('terminal', self._escape(string[:-1].replace("\\'", "'")))
                logger.debug('Tokenisier: read %s - %s', result[0], result[1])
                return result
            elif t == '"':
                string = self._read_until('', lambda temp: temp[-1:] == '"')
                result = ('terminal', self._escape(string[:-1].replace('\\"', '"')))
                logger.debug('Tokenisier: read %s - %s', result[0], result[1])
                return result
            # End of file \ string
            elif t == '\0':
                result = ('end', '')
                return result
            # Hmm.. unknown token. What did we forget? 
            else:
                logger.error("Unknown token type: "+t)
                return ('error', t)

#----------------------------------------------------------------------------

def test_basic():
    def assert_next_token(tokeniser, result):
        token = tokeniser.next_token()
        # print token
        assert token == result, "Token: "+str(token) + " Expected: "+str(result)
    
    lines = [   
        '(* Comment *) \n',
        'program = "\\"program", identifier, ";", [uses clause], block, "." ;\n',
        ' '
        ]
    
    t = EEBNFTokeniser()
    t.tokenise(lines)
    
    assert_next_token(t, ('comment', 'Comment'))
    assert_next_token(t, ('id', 'program'))
    assert_next_token(t, ('symbol', '='))
    assert_next_token(t, ('terminal', '"program'))
    assert_next_token(t, ('symbol', ','))
    assert_next_token(t, ('id', 'identifier'))
    assert_next_token(t, ('symbol', ','))
    assert_next_token(t, ('terminal', ';'))
    assert_next_token(t, ('symbol', ','))
    assert_next_token(t, ('symbol', '['))
    assert_next_token(t, ('id', 'uses clause'))
    assert_next_token(t, ('symbol', ']'))
    assert_next_token(t, ('symbol', ','))
    assert_next_token(t, ('id', 'block'))
    assert_next_token(t, ('symbol', ','))
    assert_next_token(t, ('terminal', '.'))
    assert_next_token(t, ('symbol', ';'))
    assert_next_token(t, ('end', ''))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s',stream=sys.stdout)
    test_basic()