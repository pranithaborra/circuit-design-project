import math
# Industrial Plant Electrical Design
V = 415
transformer = 250  # kVA
loads = [45, 30, 15, 20, 30, 30]
demand = [0.8, 0.7, 0.8, 0.9, 0.6, 0.5]
connected = sum(loads)
total_demand = sum(p * d for p, d in zip(loads, demand))
kVA = total_demand / 0.9
current = transformer * 1000 / (math.sqrt(3) * V)
print("SMALL INDUSTRIAL PLANT DESIGN")
print("--------------------------------")
print("Connected Load :", connected, "kW")
print("Demand Load    :", total_demand, "kW")
print("Required kVA   :", round(kVA, 2), "kVA")
print("Transformer    :", transformer, "kVA")
print("LV Current     :", round(current, 2), "A")
print("\nCIRCUIT:")
print("11 kV Supply")
print("     ↓")
print("VCB")
print("     ↓")
print("11/0.415 kV Transformer")
print("     ↓")
print("ACB")
print("     ↓")
print("415 V Busbar")
print(" ↓    ↓    ↓    ↓")
print("MCCB MCCB MCCB Lighting")
print(" ↓    ↓    ↓")
print("M1   M2   M3")
print("\nSafety: Earthing, MCCB, ACB, Overload Relay")