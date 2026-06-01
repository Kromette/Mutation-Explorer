SELECT DISTINCT
    pdb_id,
    protein_name,
    LENGTH(sequence) AS sequence_length
FROM {{ ref('stg_mutations') }}