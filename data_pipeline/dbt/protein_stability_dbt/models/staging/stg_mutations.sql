SELECT
    pdb_id,
    wild_type,
    mutation,
    position,
    ddG
FROM raw_mutations
WHERE ddG IS NOT NULL