class Command:
    class Type:
        ADD = "ADD"
        SUB = "SUB"
        NEG = "NEG"
        EQ = "EQ"
        GT = "GT"
        LT = "LT"
        AND = "AND"
        OR = "OR"
        NOT = "NOT"
        PUSH = "PUSH"
        POP = "POP"
        LABEL = "LABEL"
        GOTO = "GOTO"
        IFGOTO = "IF-GOTO"
<<<<<<< HEAD
=======
        RETURN = "RETURN"
        CALL = "CALL"
        FUNCTION = "FUNCTION"
>>>>>>> 37d5c95172bf4ee6f233755b1b004d98d0318ea4

    def __init__(self, command):
        self.type = command[0].upper()
        self.args = command[1:]