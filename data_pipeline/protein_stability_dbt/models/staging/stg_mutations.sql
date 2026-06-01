SELECT
    pdb_id,
    wild_type,
    protein_name,
    mutation,
    position,
    ddG,
    sequence
FROM raw_mutations
WHERE ddG IS NOT NULL