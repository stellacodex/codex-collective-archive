# /core/gate_mapper.py

def get_gate_and_line(degree):
    gate_width = 5.625
    line_width = gate_width / 6

    gate_number = int(degree // gate_width) + 1
    line_number = int((degree % gate_width) // line_width) + 1

    return {"gate": gate_number, "line": line_number}