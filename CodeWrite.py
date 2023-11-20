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
    
    def writePop(seg, index):
        if seg in ["static", "temp", "pointer"]:
            write(f"@SP  // pop {seg} {index}")
            write("M=M-1")
            write("A=M")
            write("D=M")
            write(f"@{register_name(seg, index)}")
            write("M=D")
        else:
            write(f"@{register_name(seg, 0)}  // pop {seg} {index}")
            write("D=M")
            write(f"@{index}")
            write("D=D+A")
            write("@R13")
            write("M=D")
            write("@SP")
            write("M=M-1")
            write("A=M")
            write("D=M")
            write("@R13")
            write("A=M")
            write("M=D")


    def write(self, line):
        self.output.append(line)

    def save_to_file(self, file_name):
        with open(file_name, "w") as file:
            file.write("\n".join(self.output))