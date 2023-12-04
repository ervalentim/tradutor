from CodeWrite import CodeWriter  # Importe a classe CodeWriter do seu módulo
# # Crie uma instância do CodeWriter
code_writer = CodeWriter("output.asm")

# # Teste o método set_file_name com diferentes nomes de arquivo
# test_file_names = ["File1.vm", "File2.vm", "File3.vm"]

# for file_name in test_file_names:
#     code_writer.set_file_name(file_name)
#     assert code_writer.module_name == file_name.split(".")[0], f"Erro no teste para o arquivo {file_name}"

# print("Teste bem-sucedido!")

# code_writer.set_file_name("TestLabel.vm")

# # Adicione um comando label ao código VM
# label_name = "Loop"
# code_writer.write_label(label_name)

# # Verifique se o código gerado contém o rótulo esperado
# expected_output = f"({code_writer.module_name}${label_name})\n"

# assert code_writer.code_output() == expected_output, "Erro no teste do método writeLabel"

# print("Teste bem-sucedido!")

# code_writer.set_file_name("GotoTest.vm")
# code_writer.write_goto("Loop")

# expected_output = """@GotoTest.Loop
# 0;JMP
# """

# assert code_writer.code_output() == expected_output, "O código assembly gerado não corresponde ao esperado."

# print("Teste bem-sucedido!")

# code_writer.set_file_name("IfTest.vm")
# code_writer.write_if("Loop")

# expected_output = """@SP
# AM=M-1
# D=M
# @IfTest.Loop
# D;JNE
# """
# assert code_writer.code_output() == expected_output, "O código assembly gerado não corresponde ao esperado."

# print("Teste bem-sucedido!")

# code_writer.set_file_name("CallTest.vm")

# code_writer.write_call("Main.calledFunction", 1)

# expected_output = """@Main.calledFunction$ret.0
# D=A
# @SP
# A=M
# M=D
# @SP
# M=M+1
# @LCL
# D=M
# @SP
# A=M
# M=D
# @SP
# M=M+1
# @ARG
# D=M
# @SP
# A=M
# M=D
# @SP
# M=M+1
# @THIS
# D=M
# @SP
# A=M
# M=D
# @SP
# M=M+1
# @THAT
# D=M
# @SP
# A=M
# M=D
# @SP
# M=M+1
# @SP
# D=M
# @6
# D=D-A
# @ARG
# M=D
# @SP
# D=M
# @LCL
# M=D
# @Main.calledFunction
# 0;JMP
# (Main.calledFunction$ret.0)
# """

# print(code_writer.code_output())
# assert code_writer.code_output() == expected_output, "O código assembly gerado não corresponde ao esperado."

# print("Teste bem-sucedido!")

# Teste da função write_function
# code_writer = CodeWriter()

code_writer = CodeWriter("output.asm")

# Configurar o nome do arquivo VM
code_writer.set_file_name("SimpleFunction.vm")

# Escrever a função SimpleFunction.test
code_writer.write_function("test", 2)

# Adicionar o código VM
vm_code = """
push local 0
push local 1
add
not
push argument 0
add
push argument 1
sub
return
"""

for line in vm_code.split('\n'):
    if line.strip():  # Ignorar linhas em branco
        code_writer.write(line)

# Visualizar o código assembly gerado
print("Código Assembly gerado:")
print(code_writer.code_output())









