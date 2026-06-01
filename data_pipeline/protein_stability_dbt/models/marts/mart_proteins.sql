SELECT DISTINCT
    pdb_id,
    protein_name,
    sequence_length
FROM {{ ref('int_proteins') }}