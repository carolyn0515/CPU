### **역할: Memory access interface 제공**

> Memory Unit은 CPU와 Main Memory 사이의 중개 계층
> CPU는 메모리를 직접 접근하지 않고 MAR/MDR를 통해 접근한다.

1. **Memory Address Register (MAR)**
    - 접근할 메모리 주소 저장
    - Fetch/Load/Store 시 사용

2. **Memory Data Register (MDR)**
    - 메모리에서 읽은 데이터 저장
    - 메모리에 쓸 데이터 저장

3. **Memory**
    - 명령어 및 데이터 저장 공간
    - Address 기반 접근

4. **Memory I/O Logic**
    - read(address)
    - write(address, value)
    메모리 latency나 cache 확장 시 이 계층에서 구현 가능

    