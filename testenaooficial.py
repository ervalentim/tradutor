from CodeWrite import CodeWriter  # Importe a classe CodeWriter do seu módulo
print("teste chega aqui")
# Crie uma instância do CodeWriter
code_writer = CodeWriter("output.asm")

# Teste o método set_file_name com diferentes nomes de arquivo
test_file_names = ["File1.vm", "File2.vm", "File3.vm"]

for file_name in test_file_names:
    code_writer.set_file_name(file_name)
    assert code_writer.module_name == file_name.split(".")[0], f"Erro no teste para o arquivo {file_name}"

print("Teste bem-sucedido!")