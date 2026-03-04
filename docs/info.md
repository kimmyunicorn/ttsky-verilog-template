<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

Explain how your project works

This project impelemnts a 4-bit full adder. It takes two 4-bit inputs (A and B) and a 1 bit carry-in, and produces a 4-bit sum and a 1-bit carry-out.

The pin mapping is:
ui_in[3:0] - input A
ui_in[4] - carry-in
uio_in[3:0] - input B
uo_out[3:0] - sum output
uo_out[4] - carry out

The adder is implemented using an always_comb block that computes a 5-bit result from the two 4-bit inputs and carry-in, then splits it into a 4-bit sum and a 1-bit carry-out.

## How to test

Explain how to use your project

the cocotb testbench in test/test.py tests the adder with 8 tests cases:

0+0+0 = 0 - basic zero test
1+1+0 =2 - basic addition test
7+8+0 = 15 - mid range values test
15+15+0 = 30 max values, verifies carry out test
15+15+1 = 31 - max values with carry-in test
5+3+1 = 9 carry in propagation test
0+0+1 =1 - carry in only test
8+7+1 = 16 - carry out with carry in

Each test checks both 4 bit sum and carry out against the expected result. The testbench is self-checking and reports PASS or FAIL for each case.



## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any

None.
