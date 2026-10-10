import os
import numpy as np
import pandas as pd

def audit(path, name):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    df = pd.read_csv(path)
    p_err = np.abs(df["picard_price"] - df["ref_price"])
    n_err = np.abs(df["nsde_price"] - df["ref_price"])
    print(f"=== {name} ===")
    print(f"Picard  | RMSE: {np.sqrt(np.mean(p_err**2)):.6f} | MaxAE: {p_err.max():.6f} | Arb Fail: {df['picard_arb_violation'].mean()*100:.1f}%")
    print(f"NSDE    | RMSE: {np.sqrt(np.mean(n_err**2)):.6f} | MaxAE: {n_err.max():.6f} | Arb Fail: {df['nsde_arb_violation'].mean()*100:.1f}%\n")

if __name__ == "__main__":
    audit("outputs/raw/block_a_bsm_test_in_results.csv", "Block A (In-Domain)")
    audit("outputs/raw/block_a_bsm_test_ext_results.csv", "Block A (OOD Extrapolation)")
    audit("outputs/raw/block_b_tfbsm_test_in_results.csv", "Block B (In-Domain)")
    audit("outputs/raw/block_b_tfbsm_test_ext_results.csv", "Block B (Low-Alpha OOD)")