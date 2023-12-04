import os
from Parser import Parser
from CodeWrite import CodeWriter
from Command import Command

def from_file(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return f.read()
    except IOError as e:
        print(f"Error reading file: {e}")
        return ""


def translate_file(file, code):
    input_text = from_file(file)
    p = Parser(input_text)
    while p.hasMoreCommands():
        command = p.nextCommand()
        if command is not None:
            if command.type == Command.Type.ADD:
                code_writer.writeArithmeticAdd()

            elif command.type == Command.Type.SUB:
                code_writer.writeArithmeticSub()

            elif command.type == Command.Type.PUSH:
                code_writer.writePush(command.args[0], int(command.args[1]))

            elif command.type == Command.Type.POP:
                code_writer.writePop(command.args[0], int(command.args[1]))

            elif command.type == Command.Type.NEG:
                code_writer.writeArithmeticNeg()

            elif command.type == Command.Type.AND:
                code_writer.write_arithmetic_and()

            elif command.type == Command.Type.OR:
                code_writer.write_arithmetic_or()

            elif command.type == Command.Type.NOT:
                code_writer.write_arithmetic_not()

            elif command.type == Command.Type.EQ:
                code_writer.write_arithmetic_eq()

            elif command.type == Command.Type.GT:
                code_writer.write_arithmetic_gt()

            elif command.type == Command.Type.LT:
                code_writer.write_arithmetic_lt()

            elif command.type == Command.Type.IFGOTO:
                code_writer.write_if(command.args[0])

            elif command.type == Command.Type.LABEL:
                code_writer.write_label(command.args[0])

            elif command.type == Command.Type.GOTO:
                code_writer.write_goto(command.args[0])

            elif command.type == Command.Type.CALL:
                code_writer.write_call(command.args[0], int(command.args[1]))

            elif command.type == Command.Type.FUNCTION:
                code_writer.write_function(command.args[0], int(command.args[1]))

            elif command.type == Command.Type.RETURN:
                code_writer.write_return()
        else:
            break


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Please provide a single file path argument.")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("The file doesn't exist.")
        sys.exit(1)

    if os.path.isdir(file_path):
        output_file_name = os.path.join(file_path, f"{os.path.basename(file_path)}.asm")
        print(output_file_name)
        code_writer = CodeWriter(output_file_name)

        code_writer.write_init()

        for filename in os.listdir(file_path):
            if filename.endswith(".vm"):
                input_file_name = os.path.join(file_path, filename)
                print(f"compiling {input_file_name}")
                translate_file(input_file_name, code_writer)

        code_writer.save()
    elif os.path.isfile(file_path):
        if not file_path.endswith(".vm"):
            print("Please provide a file name ending with .vm")
            sys.exit(1)
        else:
            input_file_name = file_path
            pos = input_file_name.index('.')
            output_file_name = f"{input_file_name[:pos]}.asm"
            code_writer = CodeWriter(output_file_name)
            print(f"compiling {input_file_name}")
            code_writer.write_init()
            translate_file(input_file_name, code_writer)
            code_writer.save()
