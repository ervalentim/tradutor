class Parser:
  def __init__ (self, filename):
    self.file = open(filename,"r")
    self.tokens = [ x.split() for x in self.file.readlines() if "//" not in x and x.strip() != ""]

  def command(self):
    return self.tokens.pop(0)
  
  def hasMoreCommands(self):
    return self.tokens != []

p = Parser("teste.vm")
while p.hasMoreCommands():
  command = p.command()
  print (command)