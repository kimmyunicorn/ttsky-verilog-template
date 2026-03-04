# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test 4-bit adder")

    #Test cases: (a, b, carry_in) -> expected (carry_out, sum)
    tests = [
        (0,0,0), #0+0+0 = 0
        (1,1,0), #1+1+0 = 2
        (7,8,0), #7+8+0 = 15
        (15,15,0) #15+15+0 = 30 (carry_out =1, sum = 14)
        (15,15,1) #15+15+1 = 31 (carry_out=1, sume=15)
        (5,3,1) #5+3+1 = 9
        (0,0,1) # 0+0+1 = 1
        (8,7,1) #8+7+1 = 16 (carry_out = 1, sume = 0)
    ]

    for (a,b,cin) in tests:
        #a on ui_in[3:0], carry_in on ui_in[4], b on uio_in[3:0
        dut.ui_in.value = a| (cin <<4)
        dut.uio_in.value = b
        await ClockCycle(dut.clk, 1)

        total a + b + cin
        exp_sum = total & 0xF #lower 4 bits
        exp_cout = (total >> 4) & 1
        expected = (exp_cout << 4) | exp_sum
        
        assert dut.uo_out.value == expected, \
            f"FAIL: a={a} b={b} cin={cin} => got {int(dut.uo_out.value)}, expected {expected}"
        dut._log.info(f"PASS: a={a} b={b} cin={cin} = {total} (cout = {exp_count} sum ={exp_sum})")

    dut._log.info("All tests passed")
        
