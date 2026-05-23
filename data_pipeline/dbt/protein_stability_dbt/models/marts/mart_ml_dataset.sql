SELECT
    pdb_id,
    position,
    hydrophobic_wild_type,
    ddg
FROM {{ ref('int_mutation_features') }}