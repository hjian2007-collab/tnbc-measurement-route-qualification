#!/usr/bin/env python3
from pathlib import Path
import hashlib, json
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = json.loads((ROOT/"outputs/expected_headline_results.json").read_text())

def close(a,b,tol=1e-6):
    return abs(float(a)-float(b)) <= tol

def check_registry():
    reg=pd.read_csv(ROOT/"config/frozen_registry_v1.csv")
    lines=[EXPECTED["registry"]["version"]]
    for _,r in reg.iterrows():
        genes=str(r["Frozen gene membership"]).replace(", ",",")
        lines.append(f"{int(r['ID']):02d}\t{r['Signature']}\t{genes}")
    sha=hashlib.sha256("\n".join(lines).encode()).hexdigest()
    assert sha==EXPECTED["registry"]["canonical_sha256"], (sha,EXPECTED["registry"]["canonical_sha256"])
    routes=pd.read_csv(ROOT/"config/route_assignments_v1.csv")
    counts=routes["Route"].value_counts().to_dict()
    for k,v in EXPECTED["registry"]["routes"].items():
        assert int(counts.get(k,0))==int(v), (k,counts.get(k,0),v)
    return "registry"

def check_raw_benchmark():
    df=pd.read_csv(ROOT/"data/processed/raw_cell_benchmark/primary_known_truth_results.csv")
    pure=df[df["truth"].isin(["abundance","state"])]
    correct=int(pure.loc[pure["truth"]=="abundance","Abundance_call"].sum()+pure.loc[pure["truth"]=="state","State_call"].sum())
    total=int(pure["n"].sum())
    opposite=int(pure.loc[pure["truth"]=="abundance","State_call"].sum()+pure.loc[pure["truth"]=="state","Abundance_call"].sum())
    mixed=df[df["truth"]=="mixed"]
    assert correct==EXPECTED["raw_cell_benchmark"]["pure_correct"]
    assert total==EXPECTED["raw_cell_benchmark"]["pure_total"]
    assert opposite==EXPECTED["raw_cell_benchmark"]["opposite_route_errors"]
    assert int(mixed["Unresolved_call"].sum())==EXPECTED["raw_cell_benchmark"]["mixed_unresolved"]
    mix=pd.read_csv(ROOT/"data/processed/raw_cell_benchmark/mixture_continuum_results.csv")
    fifty=mix[mix["abundance_weight"]==0.5]
    assert int(fifty["Unresolved_call"].sum())==EXPECTED["raw_cell_benchmark"]["fifty_fifty_unresolved"]
    return "raw benchmark"

def check_neotrip():
    wf=pd.read_csv(ROOT/"data/processed/neotrip/workflow_summary.csv")
    def row(name): return wf[wf["Workflow"]==name].iloc[0]
    assert int(row("Naive bulk")["Generic_response_hits"])==EXPECTED["neotrip"]["naive_hits"]
    assert int(row("Naive bulk")["Measurement_mismatched_hits"])==EXPECTED["neotrip"]["naive_mismatched_hits"]
    assert int(row("Cell-composition-adjusted bulk")["Generic_response_hits"])==EXPECTED["neotrip"]["adjusted_hits"]
    assert int(row("MRQ route-matched")["Generic_response_hits"])==EXPECTED["neotrip"]["mrq8_hits"]
    return "NeoTRIP"

def check_semisynthetic():
    s=(ROOT/"data/processed/semi_synthetic/Summary.csv").read_text(encoding="utf-8")
    for t in [91.7,91.0,91.3,79.9,57.7,2.3]:
        assert f"{t:.1f}%" in s, t
    return "semi-synthetic"

def check_ispy2():
    wf=pd.read_csv(ROOT/"data/processed/ispy2/Step4C_final_workflow_summary.csv")
    def row(name): return wf[wf["Workflow"]==name].iloc[0]
    assert int(row("Naïve bulk")["N"])==EXPECTED["ispy2"]["n"]
    assert int(row("Naïve bulk")["Generic_q05"])==EXPECTED["ispy2"]["naive_q05"]
    assert int(row("Naïve bulk")["Generic_q10"])==EXPECTED["ispy2"]["naive_q10"]
    assert int(row("MRQ route-matched")["Generic_q05"])==EXPECTED["ispy2"]["mrq8_generic_q05"]
    assert int(row("MRQ route-matched")["Generic_q10"])==EXPECTED["ispy2"]["mrq8_generic_q10"]
    assert int(row("Cell-composition-adjusted bulk")["Generic_q10"])==EXPECTED["ispy2"]["adjusted_all23_generic_q10"]
    assert int(row("Composition-adjusted MRQ8 sensitivity")["Generic_q05"])==EXPECTED["ispy2"]["adjusted_mrq8_generic_q05"]
    assert int(row("Composition-adjusted MRQ8 sensitivity")["Generic_q10"])==EXPECTED["ispy2"]["adjusted_mrq8_generic_q10"]
    unadj=pd.read_csv(ROOT/"data/processed/ispy2/MRQ_unadjusted_primary_n114_MRQ8.csv")
    h=unadj[unadj["Signature"]=="Hammerl_Excluded8"].iloc[0]
    assert close(h["Interaction OR/SD"],EXPECTED["ispy2"]["hammerl_interaction_or"])
    assert close(h["Interaction_BH8_q"],EXPECTED["ispy2"]["hammerl_interaction_bh8_q"])
    adj=pd.read_csv(ROOT/"data/processed/ispy2/composition_adjusted_primary_n114_MRQ8.csv")
    h=adj[adj["Signature"]=="Hammerl_Excluded8"].iloc[0]
    assert close(h["Interaction_OR"],EXPECTED["ispy2"]["hammerl_adjusted_interaction_or"])
    assert close(h["Interaction_BH8_q"],EXPECTED["ispy2"]["hammerl_adjusted_interaction_bh8_q"])
    g=pd.read_csv(ROOT/"data/processed/ispy2/composition_adjusted_GPL20078_n85_MRQ8.csv")
    h=g[g["Signature"]=="Hammerl_Excluded8"].iloc[0]
    assert close(h["Interaction_BH8_q"],EXPECTED["ispy2"]["hammerl_gpl20078_interaction_bh8_q"])
    return "I-SPY2"

def main():
    done=[fn() for fn in [check_registry,check_raw_benchmark,check_neotrip,check_semisynthetic,check_ispy2]]
    print("Verified:",", ".join(done))
    print("Archive self-test complete: all headline checks passed.")
if __name__=="__main__": main()
