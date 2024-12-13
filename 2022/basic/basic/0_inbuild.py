# compile() returns a Python code object. We use Python in built function to convert a string code into object code.
exec(compile('a=5\nb=7\nprint(a+b)','','exec'))
# We use exec() to dynamically execute Python code- this can be a string or some object code. When it is a string, Python parses it as a set of statements and executes it if there is no syntax error.
# When it is object code, Python executes it. But exec() doesn’t return a value; it returns None. Hence, we cannot use return and yield statements outside function definitions.
#eval function does evaluation of string it does not compile
eval('if 3>1: print("Okay")')

# repr('hello')
###### Problem: Calculating Current in an AC Circuit
# An AC circuit has:

# Voltage: V=10+0j volts (pure real voltage).
# impedance Z=3+4j ohms.
# the current I  in the circuit can be calculated using Ohm's Law: I=V/Z.

# Additionally, we'll calculate:

# The magnitude of the current.
# The phase angle of the current.

# Python Code

import cmath  # For handling complex numbers

# Given values
voltage = 10 + 0j  # Voltage in volts (pure real)
impedance = 3 + 4j  # Impedance in ohms (complex)

# Calculate current using Ohm's Law: I = V / Z
current = voltage / impedance

# Calculate magnitude and phase of the current
magnitude = abs(current)  # Magnitude of the current
phase = cmath.phase(current)  # Phase angle in radians

# Convert phase angle to degrees for easier interpretation
phase_degrees = phase * (180 / cmath.pi)

# Output the results
print(f"Voltage (V): {voltage}")
print(f"Impedance (Z): {impedance}")
print(f"Current (I): {current} (complex form)")
print(f"Magnitude of Current: {magnitude:.2f} A")
print(f"Phase Angle of Current: {phase_degrees:.2f} degrees")

# Output: Voltage (V): (10+0j)
# Impedance (Z): (3+4j)
# Current (I): (0.48-0.64j) (complex form)
# Magnitude of Current: 0.80 A
# Phase Angle of Current: -53.13 degrees

# Explanation of Results
# Current (I): The result is a complex number 
# 0.48−0.64j, which represents the current in the circuit. The real part is in phase with the voltage, and the imaginary part represents the phase difference due to reactance.
# Magnitude: The magnitude of the current is 0.80 A, which is the effective current flowing through the circuit.
# Phase Angle: The phase angle of −53.13 shows that the current lags behind the voltage (common in inductive circuits).


# set(zip([1,2,3],['a','b','c'])) gives me {(1, ‘a’), (3, ‘c’), (2, ‘b’)} question here why 3,'c' are not in order 
# When you use set(zip([1, 2, 3], ['a', 'b', 'c'])), Python creates a sequence of tuples [(1, 'a'), (2, 'b'), (3, 'c')] first.
# When this sequence is converted into a set, Python stores the tuples in an order determined by their hash values, not their insertion order.
# Thus, {(1, 'a'), (3, 'c'), (2, 'b')} appears unordered because of the set's internal structure.

print(set(zip([1,2,8,9],[3,4,5])))
print(list(zip([1,2,8,9],[3,4,5])))
print(list(zip([1,2],[3,4,5])))
print(set(zip([1,2],[3,4,5])))
for i in zip([1,2],[3,4,5]):
    for j in i:
        print(hash(j))
    print(hash(i))




