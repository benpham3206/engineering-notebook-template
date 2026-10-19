"""Hand calculation for the example curtain bot: two enclosures, one per curtain panel.

Run from the repo root:  python example/calc/curtain.py
Every number printed here is the one written in the notebook.
Units: N, m, s, V, A, W, J.
"""
import math
import statistics as st

# T001 pull force per panel, spring scale with 0.1 N divisions
start = {"left": [3.4, 3.6, 3.3, 3.5, 3.4], "right": [3.9, 4.1, 3.8, 4.0, 3.9]}
run = {"left": [2.1, 2.0, 2.2, 1.9, 2.0], "right": [2.6, 2.4, 2.5, 2.7, 2.5]}
print("T001 pull force")
for side in ("left", "right"):
    s, r_ = start[side], run[side]
    print(f"  {side:5} start mean {st.mean(s):.2f} +/- {st.stdev(s)/math.sqrt(len(s)):.2f} N, "
          f"max {max(s):.1f} N; run mean {st.mean(r_):.2f} N")

# Entry 2025-10-20 sizing, worst panel sets the design for both enclosures
margin = 2.0
r = 0.010          # m, drive pulley pitch radius
travel = 0.60      # m, one panel, open to closed
t_target = 15.0    # s
F_max = max(max(start["left"]), max(start["right"]))
F_design = margin * F_max
T_design = F_design * r
v = travel / t_target
omega = v / r
rpm = omega * 60 / (2 * math.pi)
P_mech = max(st.mean(run["left"]), st.mean(run["right"])) * v
print("Sizing")
print(f"  F_design {F_design:.1f} N, T_design {T_design:.3f} N m")
print(f"  v {v:.3f} m/s, omega {omega:.1f} rad/s = {rpm:.0f} rpm, P_mech {P_mech:.2f} W")

# Entry 2025-10-27: current of one enclosure at 5.00 V, bench multimeter
V, I_idle, I_run, t_move, moves = 5.00, 0.030, 0.21, 14.8, 2
E_move = V * I_run * t_move * moves
E_idle = V * I_idle * 86400
print("Entry 2025-10-27 current, per enclosure")
print(f"  E_move {E_move:.0f} J/day, E_idle {E_idle:.0f} J/day, idle share {E_idle/(E_idle+E_move)*100:.1f} %")
print(f"  charge per 30 days {(I_idle*86400 + I_run*t_move*moves)*30/3600:.1f} A h")
