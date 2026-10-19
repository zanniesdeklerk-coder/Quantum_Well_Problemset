import numpy as np
import matplotlib.pyplot as plt


# function to calculate the actual wavefunction (psi)
def infinite_square_well_wavefunction(x, n, L):
    # just plugging in the standard formula: sqrt(2/L) * sin(n * pi * x / L)
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)


# setup parameters for our box
L = 1.0  # width of the well (keeping it simple at 1)
num_points = 1000  # resolution for the x-axis so the plots look smooth
x = np.linspace(0, L, num_points)

# pick which energy levels we want to look at
energy_levels = [1, 2, 3]

# side-by-side plots: one for psi, one for probability density
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

for n in energy_levels:
    psi = infinite_square_well_wavefunction(x, n, L)
    prob_density = psi ** 2  # born rule: just square the wavefunction

    # throw them onto the plots
    ax1.plot(x, psi, label=f'n = {n}')
    ax2.plot(x, prob_density, label=f'n = {n}')

# styling the wavefunction plot
ax1.set_title('Wavefunctions $\psi_n(x)$')
ax1.set_xlabel('Position (x)')
ax1.set_ylabel('Amplitude')
ax1.axhline(0, color='black', linestyle='--', linewidth=0.5)  # zero line for reference
ax1.legend()
ax1.grid(True, alpha=0.3)

# styling the probability plot
ax2.set_title('Probability Densities $|\psi_n(x)|^2$')
ax2.set_xlabel('Position (x)')
ax2.set_ylabel('Probability Density')
ax2.legend()
ax2.grid(True, alpha=0.3)

# make sure nothing overlaps and show it
plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt


# function to calculate the actual wavefunction (psi)
def infinite_square_well_wavefunction(x, n, L):
    # just plugging in the standard formula: sqrt(2/L) * sin(n * pi * x / L)
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)


# setup parameters for our box
L = 1.0  # width of the well (keeping it simple at 1)
num_points = 1000  # resolution for the x-axis so the plots look smooth
x = np.linspace(0, L, num_points)

# pick which energy levels we want to look at
energy_levels = [1, 2, 3]

# side-by-side plots: one for psi, one for probability density
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

for n in energy_levels:
    psi = infinite_square_well_wavefunction(x, n, L)
    prob_density = psi ** 2  # born rule: just square the wavefunction

    # throw them onto the plots
    ax1.plot(x, psi, label=f'n = {n}')
    ax2.plot(x, prob_density, label=f'n = {n}')

    # --- PROBLEM 2 STUFF ---
    # check for the first excited state (n = 2)
    if n == 2:
        # grab only the x values from 0 to L/4
        prob_region_mask = x <= (L / 4)
        x_left_quarter = x[prob_region_mask]
        prob_density_left_quarter = prob_density[prob_region_mask]

        # integrate the area under the curve for this chunk
        numerical_prob = np.trapz(prob_density_left_quarter, x_left_quarter)

        # shade the region on the plot so we can see it
        ax2.fill_between(x_left_quarter, prob_density_left_quarter, alpha=0.3,
                         label=f'n=2 Left Quarter (Prob: {numerical_prob:.3f})')

# styling the wavefunction plot
ax1.set_title('Wavefunctions $\psi_n(x)$')
ax1.set_xlabel('Position (x)')
ax1.set_ylabel('Amplitude')
ax1.axhline(0, color='black', linestyle='--', linewidth=0.5)  # zero line for reference
ax1.legend()
ax1.grid(True, alpha=0.3)

# styling the probability plot
ax2.set_title('Probability Densities $|\psi_n(x)|^2$')
ax2.set_xlabel('Position (x)')
ax2.set_ylabel('Probability Density')
ax2.legend()
ax2.grid(True, alpha=0.3)

# make sure nothing overlaps and show it
plt.tight_layout()
plt.show()

# print the final answer to the terminal to check against pen-and-paper math
print(f"--- Problem 2 Verification ---")
print(f"Numerical probability for n=2 between x=0 and x=L/4: {numerical_prob:.4f}")
import numpy as np
import matplotlib.pyplot as plt


# function to calculate the actual wavefunction (psi)
def infinite_square_well_wavefunction(x, n, L):
    # just plugging in the standard formula: sqrt(2/L) * sin(n * pi * x / L)
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)


# setup parameters for our box
L = 1.0  # width of the well (keeping it simple at 1)
num_points = 1000  # resolution for the x-axis so the plots look smooth
x = np.linspace(0, L, num_points)

# pick which energy levels we want to look at
energy_levels = [1, 2, 3]

# side-by-side plots: one for psi, one for probability density
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

for n in energy_levels:
    psi = infinite_square_well_wavefunction(x, n, L)
    prob_density = psi ** 2  # born rule: just square the wavefunction

    # throw them onto the plots
    ax1.plot(x, psi, label=f'n = {n}')
    ax2.plot(x, prob_density, label=f'n = {n}')

    # --- PROBLEM 2 STUFF ---
    # check for the first excited state (n = 2)
    if n == 2:
        # grab only the x values from 0 to L/4
        prob_region_mask = x <= (L / 4)
        x_left_quarter = x[prob_region_mask]
        prob_density_left_quarter = prob_density[prob_region_mask]

        # integrate the area under the curve for this chunk
        numerical_prob = np.trapz(prob_density_left_quarter, x_left_quarter)

        # shade the region on the plot so we can see it
        ax2.fill_between(x_left_quarter, prob_density_left_quarter, alpha=0.3,
                         label=f'n=2 Left Quarter (Prob: {numerical_prob:.3f})')

# styling the wavefunction plot
ax1.set_title('Wavefunctions $\psi_n(x)$')
ax1.set_xlabel('Position (x)')
ax1.set_ylabel('Amplitude')
ax1.axhline(0, color='black', linestyle='--', linewidth=0.5)  # zero line for reference
ax1.legend()
ax1.grid(True, alpha=0.3)

# styling the probability plot
ax2.set_title('Probability Densities $|\psi_n(x)|^2$')
ax2.set_xlabel('Position (x)')
ax2.set_ylabel('Probability Density')
ax2.legend()
ax2.grid(True, alpha=0.3)

# make sure nothing overlaps and show it
plt.tight_layout()
plt.show()

# print the final answer to the terminal to check against pen-and-paper math
print(f"--- Problem 2 Verification ---")
print(f"Numerical probability for n=2 between x=0 and x=L/4: {numerical_prob:.4f}")
