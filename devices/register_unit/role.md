### **역할: CPU 내부 상태 저장**

> CPU 실행에 필요한 모든 핵심 상태값을 저장하는 저장소
> CPU가 수행하는 모든 연산은 결국 레지스터 값을 읽고 쓰는 과정

1. **Program Counter(PC)**
    - 다음에 fetch할 명령어 주소 저장
    - Instruction flow의 시작점
2. **Instruction Register (IR)**
    - 현재 실행 중인 명령어 저장
    - Decode 단계의 입력
3. **Stack Pointer (SP)**
    - Stack top 주소 저장
    - PUSH/POP/CALL/RET 수행에 사용
4. **General Purpose Registers (GPR)**
    - 연산 대상 데이터 저장
    - ALU 입력값 제공
    - 연산 결과 저장
5. **Register File**
    - 여러 GPR을 통합 관리
    - read/write interface 제공 

