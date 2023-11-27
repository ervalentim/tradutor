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

code_writer.set_file_name("GotoTest.vm")
code_writer.write_goto("Loop")

expected_output = """@GotoTest.Loop
0;JMP
"""
print(code_writer.code_output())
print(expected_output)

assert code_writer.code_output() == expected_output, "O código assembly gerado não corresponde ao esperado."

print("Teste bem-sucedido!")













