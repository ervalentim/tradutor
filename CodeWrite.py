class CodeWriter:

    def __init__(self, fname):
        self.output = []
        self.module_name = "Main"
        self.syn_count = 0
        self.output_file_name = fname

    def set_file_name(self, s):
        self.module_name = s[s.rfind("/") + 1:s.index(".")]
        print(self.module_name)

    def registerName(self, segment, index):
        if segment == "local":
            return "LCL"
        elif segment == "argument":
            return "ARG"
        elif segment == "this":
            return "THIS"
        elif segment == "that":
            return "THAT"
        elif segment == "pointer":
            return "R" + str(3 + index)
        elif segment == "temp":
            return "R" + str(5 + index)

        return f"{self.module_name}.{index}"

    def writePush(self, seg, index):
        if seg == "constant":
            self.write(f"@{index}  // push {seg} {index}")
            self.write("D=A")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")
        elif seg in ["static", "temp", "pointer"]:
            self.write(f"@{self.register_name(seg, index)}  // push {seg} {index}")
            self.write("D=M")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")
        else:
            self.write(f"@{self.register_name(seg, 0)}  // push {seg} {index}")
            self.write("D=M")
            self.write(f"@{index}")
            self.write("A=D+A")
            self.write("D=M")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")
    
    def writePop(self, seg, index):
        if seg in ["static", "temp", "pointer"]:
            self.write(f"@SP  // pop {seg} {index}")
            self.write("M=M-1")
            self.write("A=M")
            self.write("D=M")
            self.write(f"@{self.registerName(seg, index)}")
            self.write("M=D")
        else:
            self.write(f"@{self.registerName(seg, 0)}  // pop {seg} {index}")
            self.write("D=M")
            self.write(f"@{index}")
            self.write("D=D+A")
            self.write("@R13")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M-1")
            self.write("A=M")
            self.write("D=M")
            self.write("@R13")
            self.write("A=M")
            self.write("M=D")
    
    def writeArithmeticAdd(self):
        self.write("@SP  // add")
        self.write("M=M-1")
        self.write("A=M")
        self.write("D=M")
        self.write("A=A-1")
        self.write("M=D+M")

    def writeArithmeticSub(self):
        self.write("@SP  // sub")
        self.write("M=M-1")
        self.write("A=M")
        self.write("D=M")
        self.write("A=A-1")
        self.write("M=M-D")

    def writeArithmeticNeg(self):
        self.write("@SP  // neg")
        self.write("A=M")
        self.write("A=A-1")
        self.write("M=-M")

    def write_arithmetic_and(self):
        self.write("@SP // and")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("A=A-1")
        self.write("M=D&M")

    def write_arithmetic_or(self):
        self.write("@SP // or")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("A=A-1")
        self.write("M=D|M")

    def write(self, s):
        self.output.append(f"{s}\n")

    def code_output(self):
        return "".join(self.output)

    def save(self):
        with open(self.output_file_name, "w") as file:
            file.write("".join(self.output))


code_writer = CodeWriter()
code_writer.write_arithmetic_and()
code_writer.write_arithmetic_or()
code_writer.write_arithmetic_not()
code_writer.write_arithmetic_eq()
code_writer.write_arithmetic_gt()
code_writer.write_arithmetic_lt()
print(code_writer.output)