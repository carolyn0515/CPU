### **역할: 연산 수행 및 상태 플래그 생성**

1. **ALU (Arithmetic Logic Unit)**
    - ADD
    - SUB
    - AND
    - OR
    - XOR
    - NOT
    - CMP

    입력:
    - Register 값
    - Immediate 값
    - Memory 값

    출력:
    - 연산 결과
    - Flag 상태

2. **TEMP Register**
    - ALU 결과 임시 저장
    - Write Back 이전 단계에서 사용

3. **FLAGS Register**
    연산 결과 상태 저장
    - Zero Flag (Z)
    - Carry Flag (C)
    - Sign Flag (S)
    - Overflow Flag (O)
    Branch 명령어 실행 시 사용