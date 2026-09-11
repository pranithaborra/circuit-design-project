def line():
    print("=" * 70)
def get_positive_number(message):
    while True:
        try:
            value = float(input(message))
            if value >= 0:
                return value
            print("Please enter a positive value.")
        except ValueError:
            print("Please enter a valid number.")
line()
print("RESIDENTIAL ELECTRICAL WIRING DESIGN")
line()
print("\nBUILDING INFORMATION")
rooms = int(get_positive_number("Enter number of rooms: "))
area = get_positive_number("Enter building area in square meters: ")
print("\nSupply Details")
voltage = get_positive_number("Enter supply voltage (V) [230]: ")
if voltage == 0:
    voltage = 230
frequency = get_positive_number("Enter supply frequency (Hz) [50]: ")
if frequency == 0:
    frequency = 50
power_factor = get_positive_number(
    "Enter assumed power factor [0.9]: "
)
if power_factor == 0:
    power_factor = 0.9
print("\n" + "=" * 70)
print("LOAD DETAILS")
print("=" * 70)
loads = []
number_of_loads = int(
    get_positive_number("Enter number of different load types: ")
)
for i in range(number_of_loads):
    print(f"\nLoad {i + 1}")
    name = input("Enter load name: ")
    quantity = int(
        get_positive_number("Enter quantity: ")
    )
    rating = get_positive_number(
        "Enter rating of one unit (W): "
    )
    total = quantity * rating
    loads.append({
        "name": name,
        "quantity": quantity,
        "rating": rating,
        "total": total
    })
connected_load = sum(load["total"] for load in loads)
line()
print("CONNECTED LOAD CALCULATION")
line()
print(
    f"{'Load':<25}"
    f"{'Qty':>8}"
    f"{'Rating(W)':>15}"
    f"{'Total(W)':>15}"
)
print("-" * 70)
for load in loads:

    print(
        f"{load['name']:<25}"
        f"{load['quantity']:>8}"
        f"{load['rating']:>15.1f}"
        f"{load['total']:>15.1f}"
    )
print("-" * 70)
print(f"TOTAL CONNECTED LOAD = {connected_load:.2f} W")
print(f"TOTAL CONNECTED LOAD = {connected_load / 1000:.2f} kW")
print("\n" + "=" * 70)
print("MAXIMUM DEMAND CALCULATION")
print("=" * 70)
demand_factor = get_positive_number(
    "Enter demand/diversity factor [0.70]: "
)
if demand_factor == 0:
    demand_factor = 0.70
maximum_demand = connected_load * demand_factor
print(
    f"\nMaximum Demand = Connected Load × Demand Factor"
)
print(
    f"Maximum Demand = {connected_load:.2f} × "
    f"{demand_factor:.2f}"
)
print(f"Maximum Demand = {maximum_demand:.2f} W")
print(f"Maximum Demand = {maximum_demand / 1000:.2f} kW")
design_current = maximum_demand / (
    voltage * power_factor
)
print("\nDESIGN CURRENT")
print(
    "I = P / (V × Power Factor)"
)
print(
    f"I = {maximum_demand:.2f} / "
    f"({voltage:.0f} × {power_factor:.2f})"
)
print(f"Design Current = {design_current:.2f} A")
print("\n" + "=" * 70)
print("CIRCUIT DISTRIBUTION")
print("=" * 70)
lighting_load = 0
socket_load = 0
high_power_load = 0
for load in loads:
    name = load["name"].lower()
    if (
        "light" in name
        or "lamp" in name
        or "fan" in name
    ):
        lighting_load += load["total"]
    elif (
        "socket" in name
        or "plug" in name
    ):
        socket_load += load["total"]
    else:
        high_power_load += load["total"]
print(f"Lighting and Fan Load : {lighting_load:.2f} W")
print(f"Socket Load           : {socket_load:.2f} W")
print(f"Other/Power Load      : {high_power_load:.2f} W")
print("\n" + "=" * 70)
print("PROPOSED DISTRIBUTION BOARD")
print("=" * 70)

print("""
MAIN SUPPLY
     |
     v
ENERGY METER
     |
     v
MAIN ISOLATOR
     |
     v
RCCB / RCBO
     |
     v
DISTRIBUTION BOARD
     |
     +---- MCB 1 ---- Lighting and Fans
     |
     +---- MCB 2 ---- General Socket Outlets
     |
     +---- MCB 3 ---- Kitchen Loads
     |
     +---- MCB 4 ---- Refrigerator
     |
     +---- MCB 5 ---- Washing Machine
     |
     +---- MCB 6 ---- Geyser
     |
     +---- MCB 7 ---- Air Conditioner
     |
     +---- MCB 8 ---- Future Expansion
     |
     v
PROTECTIVE EARTHING
""")
print("=" * 70)
print("ELECTRICAL SAFETY CHECKLIST")
print("=" * 70)
safety_points = [
    "Proper protective earthing",
    "MCB protection against overload and short circuit",
    "RCCB/RCBO protection against earth leakage",
    "Separate circuits for major high-power appliances",
    "Correct cable size according to design current",
    "Voltage-drop verification",
    "Avoid overloading socket outlets",
    "Proper insulation of conductors",
    "Distribution board circuit labeling",
    "Testing before energizing"
]
for number, point in enumerate(safety_points, 1):
    print(f"{number:02d}. {point}")
line()
print("ENGINEERING DESIGN SUMMARY")
line()
print(f"Number of rooms       : {rooms}")
print(f"Building area         : {area:.2f} m²")
print(f"Supply voltage        : {voltage:.0f} V")
print(f"Supply frequency      : {frequency:.0f} Hz")
print(f"Power factor          : {power_factor:.2f}")
print(f"Connected load        : {connected_load / 1000:.2f} kW")
print(f"Demand factor         : {demand_factor:.2f}")
print(f"Maximum demand        : {maximum_demand / 1000:.2f} kW")
print(f"Design current        : {design_current:.2f} A")
line()
print("""
CONCLUSION:
The program calculates the representative electrical load of a
residential building and provides a basic distribution arrangement.
For an actual installation, cable sizes, MCB/RCCB/RCBO ratings,
earthing details and service capacity must be verified using the
actual building layout, appliance nameplate ratings, installation
conditions, applicable Indian electrical standards and utility
requirements.
""")
line()
print("END OF RESIDENTIAL ELECTRICAL WIRING DESIGN PROGRAM")
line()