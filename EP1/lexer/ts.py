from tag import Tag
from token import Token
# from lexer import Lexer

class TS:
   '''
   Classe para a tabela de simbolos representada por um dicionario: {'chave' : 'valor'}
   '''
   def __init__(self):
      '''
      Repare que as palavras reservadas sao todas cadastradas
      a principio com linha e coluna em zero
      '''
      # lexer = Lexer('C:\\Users\\Mateus\\Documents\\UniBh\\8_Semestre\\Compiladores\\Teoria\\exercicio_pratico_avaliativo\\EP1\\lexer\\prog1.txt')
      self.ts = {}

      self.ts['if'] = Token(Tag.KW_IF, 'if', 0, 0)
      self.ts['else'] = Token(Tag.KW_ELSE, 'else', 0, 0)
      self.ts['then'] = Token(Tag.KW_THEN, 'then', 0, 0)
      self.ts['print'] = Token(Tag.KW_PRINT, 'print', 0, 0)

   def getToken(self, lexema):
      token = self.ts.get(lexema)
      return token

   def addToken(self, lexema, token):
      self.ts[lexema] = token

   def printTS(self):
      for k, t in (self.ts.items()):
         print(k, ":", t.toString())