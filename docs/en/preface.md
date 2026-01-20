# Preface

The acronym **scmRTOS** stands for **Single-Chip Microcontroller Real-Time Operating System**.

As indicated by the name, **scmRTOS** is targeted at single-chip microcontrollers (MCUs), although it can also be used with processors such as Blackfin or Cortex-A.

## Purpose

One of the primary objectives in developing this RTOS was to provide the simplest, most minimal, fastest, and most resource-efficient implementation of preemptive multitasking for single-chip MCUs with limited resources that generally cannot be expanded. Although advancements in technology since the introduction of **scmRTOS** have reduced the emphasis on RTOS efficiency, simplicity, speed, and compact size continue to be advantageous in many applications.

A second key motivation for **scmRTOS** is its implementation in the C++ programming language. While contemporary C++ has increased in complexity, **scmRTOS** employs only the fundamental concepts and constructs from the C++98 standard: classes, templates, inheritance, and function name overloading.

In embedded systems development, C++ is sometimes viewed unfavorably due to misconceptions regarding overhead and controllability. In practice, appropriate use of C++ can simplify software development and maintenance, although inappropriate application may produce the opposite result.

**scmRTOS** prioritizes ease of use. This is facilitated by object-based design, where classes encapsulate internal details and expose only a well-defined interface, thereby minimizing the risk of incorrect usage of operating system components.

!!! tip "**TIP**"

    The history of **scmRTOS** and certain "philosophical" considerations regarding real-time operating systems are detailed in the [PDF document](https://github.com/scmrtos/scmrtos-doc/blob/master/attic/pdf/scmRTOS.en.pdf).
