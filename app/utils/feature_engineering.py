HYDROPHOBIC = ["A", "V", "L", "I", "F", "Y"]

def build_features(position, wild_type, mutation):

    hydrophobic_wt = int(wild_type in HYDROPHOBIC)
    hydrophobic_mut = int(mutation in HYDROPHOBIC)


    return {
        "position": position,
        "hydrophobic_wild_type": hydrophobic_wt,
        "hydrophobic_mutation": hydrophobic_mut,
    }