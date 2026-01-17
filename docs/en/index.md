# Synopsis

## About scmRTOS

**scmRTOS** is compact Real-Time Preemptive Operating System intended for use with Single-Chip Microcontrollers. 

**scmRTOS** is capable to run on tiny uCs with as small amount of RAM as 512 bytes. The RTOS is written on C++ and supports [various platforms](#index-supported-targets). See next sections and for more details. Additionally, the documentation is also available in [PDF format](https://github.com/scmrtos/scmrtos-doc).


Source code can be cloned or downloaded from [Github](https://github.com/scmrtos/scmrtos). There are a [number of sample projects](https://github.com/scmrtos/scmrtos-sample-projects) that demonstrates RTOS usage.

Full distribution including RTOS sources, sample projects, documentation, etc available on [releases page](https://github.com/scmrtos/scmrtos/releases/).

## Features

  * Written entirely on C++.
    * High reliability.
    * Simplicity and ease-of-use.

  * Introduce Extensions mechanism at kernel level.
    * User defined extensions.
    * Debug features.

  * Minimal process switching latency[^index-1].
    * 900 ns on Cortex-M4 @ 168 MHz.
    * 1.8 us on Blackfin @ 200 MHz.
    * 2.7 us on Cortex-M3 @ 72 MHz.
    * 700 ns on Cortex-A9 @ 400 MHz (with full FPU context save/restore).
    * 5 us on ARM7 @ 50 MHz.
    * 38-42 us on AVR @ 8 MHz.
    * 45-50 us on MSP430 @ 5 MHz.
    * 18-20 us on STM8 @ 16 MHz.

  * Small footprint.
    * From 512 bytes of RAM.
    * From ~1K code.

[^index-1]: This includes overall control transfer time, not only context switch

## Supported Target Platforms <span id="index-supported-targets"></span>

The following target platforms are supported for now.

| CPU/MCU  | GCC | EW (IAR) | VDSP++ (ADI)| CCES (ADI) |
|----------|:---:|:--------:|:-----------:|:----------:|
| MSP430   |  ✔  |     ✔    |      –      |      –     |
| AVR      |  ✔  |     ✔    |      –      |      –     |
| ARM7     |  ✔  |     ✘    |      –      |      –     |
| Cortex-M |  ✔  |     ✔    |      –      |      –     |
| Cortex-A |  ✔  |     ✘    |      –      |      –     |
| Blackfin |  ✔  |     –    |      ✔      |      ✔     |
| STM8     |  –  |     ✔    |      –      |      –     |


<br>
'–' means toolchain does not support CPU/MCU
