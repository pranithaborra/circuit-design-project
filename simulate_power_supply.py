import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# DC POWER SUPPLY CIRCUIT SIMULATION
# 230 V AC -> Transformer -> Bridge Rectifier
# -> Capacitor Filter -> 7805 Regulator -> 5 V DC
# ==========================================

# Circuit parameters
f = 50                    # AC frequency (Hz)
Vrms_primary = 230        # Primary voltage (V)
transformer_ratio = 230 / 9
Vrms_secondary = Vrms_primary / transformer_ratio

diode_drop = 0.7          # Voltage drop of each diode (V)
num_diodes = 2            # Two diodes conduct in bridge
C = 1000e-6               # Filter capacitor (F)
R_load = 100              # Load resistance (ohms)
V_regulated = 5           # 7805 output voltage (V)

# Simulation time
t = np.linspace(0, 0.1, 5000)

# ==========================================
# 1. Transformer secondary voltage
# ==========================================

Vpeak_secondary = Vrms_secondary * np.sqrt(2)

Vac = Vpeak_secondary * np.sin(2 * np.pi * f * t)

# ==========================================
# 2. Bridge rectifier
# ==========================================

Vrectified = np.maximum(np.abs(Vac) - num_diodes * diode_drop, 0)

# ==========================================
# 3. Capacitor filter
# ==========================================

Vcapacitor = np.zeros_like(t)

for i in range(1, len(t)):
    dt = t[i] - t[i - 1]

    # Capacitor discharge through load
    Vdischarge = Vcapacitor[i - 1] * np.exp(-dt / (R_load * C))

    # Recharge when rectifier voltage is higher
    Vcapacitor[i] = max(Vdischarge, Vrectified[i])

# ==========================================
# 4. 7805 Voltage Regulator
# ==========================================

Voutput = np.minimum(Vcapacitor, V_regulated)

# ==========================================
# 5. Electrical calculations
# ==========================================

Vout_avg = np.mean(Voutput)
I_load = V_regulated / R_load
P_load = V_regulated * I_load

ripple_voltage = np.max(Vcapacitor) - np.min(Vcapacitor)

print("=" * 50)
print("DC POWER SUPPLY SIMULATION RESULTS")
print("=" * 50)

print(f"Primary voltage       : {Vrms_primary:.2f} V AC")
print(f"Secondary voltage     : {Vrms_secondary:.2f} V AC RMS")
print(f"Secondary peak        : {Vpeak_secondary:.2f} V")
print(f"Diode drop            : {num_diodes * diode_drop:.2f} V")
print(f"Load resistance       : {R_load:.2f} ohms")
print(f"Filter capacitance    : {C * 1e6:.0f} uF")
print(f"Regulated output      : {V_regulated:.2f} V DC")
print(f"Load current          : {I_load * 1000:.2f} mA")
print(f"Load power            : {P_load:.2f} W")
print(f"Output average        : {Vout_avg:.2f} V")
print(f"Ripple voltage        : {ripple_voltage:.2f} V")
print("=" * 50)

# ==========================================
# 6. Plot input AC voltage
# ==========================================

plt.figure(figsize=(10, 5))
plt.plot(t, Vac)
plt.title("Transformer Secondary AC Voltage")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.show()

# ==========================================
# 7. Plot bridge rectifier output
# ==========================================

plt.figure(figsize=(10, 5))
plt.plot(t, Vrectified)
plt.title("Full-Wave Bridge Rectifier Output")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.show()

# ==========================================
# 8. Plot capacitor filtered voltage
# ==========================================

plt.figure(figsize=(10, 5))
plt.plot(t, Vcapacitor)
plt.title("Capacitor Filter Output")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.show()

# ==========================================
# 9. Plot final regulated output
# ==========================================

plt.figure(figsize=(10, 5))
plt.plot(t, Voutput)
plt.title("Final 5 V Regulated DC Output")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.show()