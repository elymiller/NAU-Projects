import csv
import math

def binom(n, k):
    if 0 <= k <= n:
        return math.comb(n, k)
    return 0

def compute_PATV(Si, Vn, P_TV, P_TS):
    total = 0.0
    for J in range(0, Vn):
        coeff = binom(Si - 1, J)
        total += coeff * (P_TV ** J) * (P_TS ** (Si - 1 - J))
    return total

def compute_PATS(Si, Tn, P_TS, P_TV):
    total = 0.0
    for K in range(0, Tn):
        coeff = binom(Si - 1, K)
        total += coeff * (P_TS ** K) * (P_TV ** (Si - 1 - K))
    return total

def main():
    print("=== Analytical Solution to mutS ===")

    Vn = int(input("Enter maximum number of transversions (Vn): "))  # e.g., 5
    Tn = int(input("Enter maximum number of transitions (Tn): "))    # e.g., 38
    P_TV = float(input("Enter initial probability of choosing a transversion (PTV): "))  # 0.5
    P_TS = float(input("Enter initial probability of choosing a transition (PTS): "))    # 0.5

    PM = 1 / Vn                   # mutS share of Tv bucket
    P_non_mutS = (Vn - 1) / Vn    # other Tvs' share of Tv bucket

    total_steps = Vn + Tn
    results = []

    for Si in range(1, total_steps + 1):
        patv = compute_PATV(Si, Vn, P_TV, P_TS)
        pats = compute_PATS(Si, Tn, P_TS, P_TV)

        P_tv = P_TV * P_non_mutS * patv
        P_ts = P_TS * pats
        P_mutS = P_TV * PM * patv + P_TS * PM * (1 - pats)

        results.append({
            "Step": Si,
            "P(Ts)": round(P_ts, 6),
            "P(Tv)": round(P_tv, 6),
            "P(mutS)": round(P_mutS, 6)
        })

    filename = "50%_Tv_analytical.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Step", "P(Ts)", "P(Tv)", "P(mutS)"])
        writer.writeheader()
        writer.writerows(results)

    print(f"Results saved to '{filename}'.")

if __name__ == "__main__":
    main()
