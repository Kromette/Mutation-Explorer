SELECT
    pdb_id,
    wild_type,
    mutation,
    position,
    ddg
FROM raw_mutations
WHERE ddg IS NOT NULL