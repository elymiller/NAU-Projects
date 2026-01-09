import random
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def simulate_draws(num_simulations, num_Tv, num_mutS, num_Ts, ts_weight, post_ts_weight):
    tv_weight = 100 - ts_weight
    post_tv_weight = 100 - post_ts_weight

    outcomes = [defaultdict(int) for _ in range(num_Tv + num_Ts)]
    mutS_positions = []

    print('Simulating...')
    for _ in range(num_simulations):
        Ts_bucket = ['Ts'] * num_Ts
        Tv_bucket = ['Tv'] * (num_Tv - num_mutS) + ['mutS'] * num_mutS
        draw_sequence = []
        weights_switched = False
        current_ts_weight = ts_weight
        current_tv_weight = tv_weight

        for draw_index in range(num_Tv + num_Ts):
            if not Tv_bucket:
                chosen = random.choice(Ts_bucket)
                Ts_bucket.remove(chosen)
            elif not Ts_bucket:
                chosen = random.choice(Tv_bucket)
                Tv_bucket.remove(chosen)
            else:
                bucket = random.choices(['Ts', 'Tv'], weights=[current_ts_weight, current_tv_weight])[0]
                if bucket == 'Ts':
                    chosen = random.choice(Ts_bucket)
                    Ts_bucket.remove(chosen)
                else:
                    chosen = random.choice(Tv_bucket)
                    Tv_bucket.remove(chosen)

            draw_sequence.append(chosen)
            outcomes[draw_index][chosen] += 1

            if not weights_switched and chosen == 'mutS':
                mutS_positions.append(draw_index)
                current_ts_weight = post_ts_weight
                current_tv_weight = post_tv_weight
                weights_switched = True

    print('Simulation complete!')
    export_results(outcomes, num_Tv, num_simulations)
    plot_histograms(outcomes, mutS_positions, num_Tv, num_simulations)

def export_results(outcomes, num_Tv, num_simulations):
    #filename = f"{num_Tv}-Tv_{num_simulations}-samples.csv"
    filename = "/Users/elymiller/Desktop/Research/mutS_paper/mutS_model_output/data/variable_Tv_Ti_50%_initial/50%_initial_23Tv_23Ti.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Draw Number", "P(Ts)", "P(Tv)", "P(mutS)"])
        for i, outcome in enumerate(outcomes):
            total = sum(outcome.values())
            writer.writerow([
                i + 1,
                outcome.get('Ts', 0) / total,
                outcome.get('Tv', 0) / total,
                outcome.get('mutS', 0) / total
            ])
    print(f"Probabilities saved to: {filename}")

def plot_histograms(outcomes, mutS_positions, num_Tv, num_simulations):
    print("Plotting histograms...")
    p_Ts, p_Tv, p_mutS = [], [], []

    for outcome in outcomes:
        total = sum(outcome.values())
        p_Ts.append(outcome.get('Ts', 0) / total)
        p_Tv.append(outcome.get('Tv', 0) / total)
        p_mutS.append(outcome.get('mutS', 0) / total)

    mutS_peak = max(p_mutS)
    mutS_draw = p_mutS.index(mutS_peak)

    fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
    labels = ['mutS', 'Ts', 'Tv']
    probs = [p_mutS, p_Ts, p_Tv]
    colors = ['red', 'blue', 'black']

    for ax, label, prob, color in zip(axes, labels, probs, colors):
        ax.bar(range(1, len(prob)+1), prob, color=color)
        #ax.axvline(mutS_draw+1, color='black', linestyle='--', alpha=0.8, label=f"mutS event at step {mutS_draw+1}")
        ax.set_ylabel(f"P({label})")
        ax.legend()

    axes[-1].set_xlabel("Draw Number")
    #plt.suptitle(f"Draw Probabilities Across {num_simulations} Simulations ({num_Tv} Tv)")
    plt.tight_layout()
    #plt.savefig(f"{num_Tv}_Tv_{num_simulations}_histograms.tiff", dpi=500)
    plt.savefig("36%_Tv_stochastic.png", dpi=500)
    print("Plotting complete!\nThanks for simulating :)")

if __name__ == "__main__":
    try:
        print("Welcome to the mutS Simulator!")
        num_simulations = int(input("Enter number of simulations: "))
        num_Tv = int(input("Enter TOTAL number of Transversions (Tv): "))
        num_mutS = int(input("Enter number of mutS (subset of Tv): "))
        num_Ts = int(input("Enter number of Transitions (Ts): "))
        ts_weight = float(input("Enter initial weight for Ts (0-100, default 50): ") or 50)
        post_ts_weight = float(input("Enter Ts weight AFTER mutS is drawn (e.g., 95): ") or 95)

        if num_mutS > num_Tv:
            raise ValueError("mutS count cannot exceed total Tv count.")

        simulate_draws(num_simulations, num_Tv, num_mutS, num_Ts, ts_weight, post_ts_weight)

    except ValueError as e:
        print(f"Invalid input: {e}")
