SELECT
    *,
    
    CASE
        WHEN wild_type IN ('A', 'V', 'L', 'I')
        THEN 1
        ELSE 0
    END AS hydrophobic_wild_type,

    CASE
        WHEN mutation IN ('A', 'V', 'L', 'I')
        THEN 1
        ELSE 0
    END AS hydrophobic_mutation

FROM {{ ref('stg_mutations') }}