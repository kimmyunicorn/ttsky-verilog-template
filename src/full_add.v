module full_add (
    input logic [3:0] a_i,
    input logic [3:0] b_i,
    input logic [3:0] carry_i,
    output logic [0:0] carry_o,
    output logic [3:0] sum_o
    );

    logic [4:0] result;

    always_comb begin
        result = {1'b0, a_i} + {1'b0, b_i} + {4'b0, carry_i};
        sum_o = result[3:0];
        carry_o = result[4];
    end

endmodule