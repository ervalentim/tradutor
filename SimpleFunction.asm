@LCL  // push local 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL  // push local 1
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP  // add
M=M-1
A=M
D=M
A=A-1
M=D+M
@SP // not
A=M
A=A-1
M=!M
@ARG  // push argument 0
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP  // add
M=M-1
A=M
D=M
A=A-1
M=D+M
@ARG  // push argument 1
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP  // sub
M=M-1
A=M
D=M
A=A-1
M=M-D
