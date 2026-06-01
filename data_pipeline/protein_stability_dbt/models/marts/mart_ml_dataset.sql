SELECT
    pdb_id,
    position,
    hydrophobic_wild_type,
    hydrophobic_mutation,
    ddg
FROM {{ ref('int_mutation_features') }}