### **역할: CPU 전체 실행 흐름 통제**

> Control Unit은 CPU의 지휘자 역할을 한다.\
> 데이터를 직접 저장하거나 연산하지 않고,\
> 각 장치가 언제 어떤 동작을 수행해야 하는지 결정하고 제어 신호를 생성한다.

1. **Instruction Cycle 관리**
    - Fetch
    - Decode
    - Operand Fetch
    - Execute
    - Write Back
    - Next Instruction
    현재 단계가 무엇인지 관리하고 다음 단계로 전이

2. **Micro-operation sequence 제어**
    각 명령어는 여러 micro step으로 이루어진다.\
    ex)
    - MAR <- PC
    - MDR <- Memory[MAR]
    - IR <- MDR
    - PC <- PC + 1
    Control Unit은 micro operaion 실행 순서를 결정한다.

3. **Program Counter 제어**
    다음 명령어 위치를 결정한다.
    - 정상 흐름 -> PC 증가
    - Branch -> PC 변경
    - Call -> PC 저장 후 점프
    - Return -> PC 복구

4. **장치 간 데이터 이동 제어**
    - Register -> ALU
    - ALU -> TEMP
    - TEMP -> Register
    - Register -> MDR -> Memory
    이러한 데이터 이동이 올바른 순서로 수행되도록 제어

5. **명령어 해석 결과 따른 실행 경로 결정**
    decode 단계에서
    - ALU 연산인지
    - 메모리 접근인지
    - 분기인지
    - stack 명령인지 
    실행 루틴 선택

6. **CPU 상태**
    - HALT 상태 진입
    - Interrupt 발생 시 처리 흐름 변경
    - Pipeline flush
