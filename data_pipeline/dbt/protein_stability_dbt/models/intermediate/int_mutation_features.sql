SELECT
    *,
    
    CASE
        WHEN wild_type IN ('A', 'V', 'L', 'I')
        THEN 1
        ELSE 0
    END AS hydrophobic_wild_type

FROM {{ ref('stg_mutations') }}