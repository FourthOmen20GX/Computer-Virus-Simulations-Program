# Name: Gerardo Rivera
# Date: 12/02/24
# Email: grivera14@student.gsu.edu

# N Simulations for Computer Project 5.10

import random

def simulate_virus_spread(computers, virus_probability, daily_repairs):
    infected = {0}  # The first computer on the network is infected with the virus 
    ever_infected = {0}  # Tracks any computers that have been infected at least once
    days = 0

    while infected:
        days += 1
        # Morning: Virus spreads
        new_infected = set(infected)  # Copy current infections
        for i in range(len(computers)):
            if i not in infected:
                for j in infected:
                    if random.random() < virus_probability:
                        new_infected.add(i)
                        ever_infected.add(i)
                        break
        infected = new_infected

        # Afternoon: Technician shows up and tries to clean
        if len(infected) <= daily_repairs:
            infected = set()  # All infected computers cleaned, the simulation ends
        else:
            infected = set(random.sample(list(infected), len(infected) - daily_repairs)) # randomly chooses 5 infected computers to clean

    return days, len(ever_infected)

def monte_carlo_simulation(num_computers, virus_probability, daily_repairs, num_simulations):
    total_days = 0
    total_ever_infected = 0
    all_infected_count = 0

    for _ in range(num_simulations):
        days, ever_infected_count = simulate_virus_spread(
            range(num_computers), virus_probability, daily_repairs
        )
        total_days += days
        total_ever_infected += ever_infected_count
        if ever_infected_count == num_computers:
            all_infected_count += 1

    average_days = total_days / num_simulations
    prob_all_infected = all_infected_count / num_simulations
    avg_ever_infected = total_ever_infected / num_simulations

    return average_days, prob_all_infected, avg_ever_infected

def main():
    print("--- Welcome to the Computer Virus Simulation Program! ---")
    num_computers = int(input("\nEnter the number of computers on the network: "))
    virus_probability = float(input("\nEnter the probability the virus spreads (0-1): "))
    daily_repairs = int(input("\nEnter the number of computers repaired daily: "))
    num_simulations = int(input("\nEnter the number of simulations to run: "))

    avg_days, prob_all_infected, avg_ever_infected = monte_carlo_simulation(
        num_computers, virus_probability, daily_repairs, num_simulations
    )

    print("\nSimulation Results:")
    print(f"Average days to clean the network: {int(avg_days)}")
    print(f"Probability of all computers to get infected at least once: {prob_all_infected}")
    print(f"Expected number of computers ever infected: {round(avg_ever_infected,2)}")

if __name__ == "__main__":
    main()