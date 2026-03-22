from pathlib import Path

from assembler.assembler import assemble
from execution.loader import load_program
from execution.cpu import CPU
from devices.memory_unit.memory import Memory
from devices.register_unit.pc import ProgramCounter
from devices.register_unit.register_file import RegisterFile
from devices.processing_unit.flags import Flags


def run_program(program_text):
    # 1. assemble
    instructions = assemble(program_text)

    # 2. memory 생성
    memory = Memory(len(instructions))

    # 3. program load
    load_program(memory, instructions)

    # 4. pc / registers 생성
    pc = ProgramCounter()
    registers = RegisterFile()
    flags = Flags()

    # 5. cpu 생성
    cpu = CPU(memory, pc, registers, flags)

    # 6. 실행
    cpu.run()


def main():
    test_dir = Path("tests")

    for file in sorted(test_dir.glob("*")):  
        if file.is_file():
            print("\n---------------")
            print(f"Running {file.name}")
            print("---------------")

            program_text = file.read_text()
            run_program(program_text)


if __name__ == "__main__":
    main()