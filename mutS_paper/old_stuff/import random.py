import random
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def simulate_draws_per_position(num_simulations, num_Tv, num_mutS, num_Ts, ts_weight=50):
    tv_weight = 100 - ts_weight
    outcomes_per_draw = [defaultdict(int) for _ in range(num_Tv + num_Ts)]
    print('Simulating...')

    for _ in range(num_simulations):
        Ts_bucket = ['Ts'] * num_Ts
        Tv_bucket = ['Tv'] * (num_Tv - num_mutS) + ['mutS'] * num_mutS
        draw_sequence = []

        for draw_index in range(num_Tv + num_Ts):
            if not Tv_bucket:
                chosen_ball = random.choice(Ts_bucket)
                Ts_bucket.remove(chosen_ball)
            elif not Ts_bucket:
                chosen_ball = random.choice(Tv_bucket)
                Tv_bucket.remove(chosen_ball)
            else:
                chosen_bucket = random.choices(['Ts', 'Tv'], weights=[ts_weight, tv_weight], k=1)[0]
                if chosen_bucket == 'Ts':
                    chosen_ball = random.choice(Ts_bucket)
                    Ts_bucket.remove(chosen_ball)
                else:
                    chosen_ball = random.choice(Tv_bucket)
                    Tv_bucket.remove(chosen_ball)

            draw_sequence.append(chosen_ball)
            outcomes_per_draw[draw_index][chosen_ball] += 1

    print('Simulation complete!')

    csv_filename = (f"{num_Tv}-Tv_{num_simulations}-samples.csv")
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Draw Number", "P(Ts)", "P(Tv)", "P(mutS)"])
        for i, outcome in enumerate(outcomes_per_draw):
            total = sum(outcome.values())
            red = outcome.get('Tv', 0)
            blue = outcome.get('Ts', 0)
            mutant = outcome.get('mutS', 0)
            writer.writerow([
                i + 1,
                blue / total,
                red / total,
                mutant / total
            ])

    print(f"\nProbabilities saved to: {csv_filename}")

    p_Ts = []
    p_Tv = []
    p_mutS = []

    for outcome in outcomes_per_draw:
        total = sum(outcome.values())
        p_Ts.append(outcome.get('Ts', 0) / total)
        p_Tv.append(outcome.get('Tv', 0) / total)
        p_mutS.append(outcome.get('mutS', 0) / total)

    max_mutant_prob = max(p_mutS)
    max_mutant_step = p_mutS.index(max_mutant_prob) + 1

    print("Plotting...")
    plt.figure(figsize=(12, 6))
    plt.plot(range(num_Tv + num_Ts), p_Ts, label='P(Ts)', color='blue')
    plt.plot(range(num_Tv + num_Ts), p_Tv, label='P(Tv)', color='black')
    plt.plot(range(num_Tv + num_Ts), p_mutS, label='P(mutS)', color='red')
    plt.axvline(max_mutant_step, color='gray', linestyle='--', alpha=0.6, label=f'Max P(mutS) @ Draw {max_mutant_step}')
    plt.xlabel("Draw Number")
    plt.ylabel("Probability")
    plt.title(f"Draw Probabilities Over {num_simulations} Simulations ({num_Tv} Transversions)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{num_Tv}_Tv_{num_simulations}-samples.tiff", dpi=500)
    print("Plotting complete!")
    print('Thanks for simulating :)')

if __name__ == "__main__":
    try:
        print("Welcome to the mutS Simulator!")
        num_simulations = int(input("Enter the number of simulations to run: "))
        num_Tv = int(input("Enter the number of TOTAL Transversions (Tv) (include your mutants here): "))
        num_mutS = int(input("Enter the number of mutS Transversions (Tv) (mutants are a subset of Tv): "))
        num_Ts = int(input("Enter the number of Transitions (Ts): "))
        ts_weight = float(input("Enter the weight for drawing from Ts (0-100, default 50): ") or 50)

        if num_mutS > num_Tv:
            raise ValueError("Number of mutS Transversions cannot exceed number of total Transversions.")

        simulate_draws_per_position(num_simulations, num_Tv, num_mutS, num_Ts, ts_weight)

    except ValueError as e:
        print(f"Invalid input: {e}")
