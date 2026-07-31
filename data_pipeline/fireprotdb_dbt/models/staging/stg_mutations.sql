SELECT
    CAST(p.id AS TEXT) AS pdb_id,
    s.source_aa AS wild_type,
    p.name AS protein_name,
    s.target_aa AS mutation,
    s.position,
    NULL::DOUBLE PRECISION AS ddG,
    seq.sequence
FROM {{ source('fireprotdb', 'substitution') }} AS s
JOIN {{ source('fireprotdb', 'mutant') }} AS m
    ON m.id = s.mutant_id
JOIN {{ source('fireprotdb', 'protein') }} AS p
    ON p.id = m.source_id
LEFT JOIN {{ source('fireprotdb', 'protein_sequence') }} AS ps
    ON ps.protein_id = p.id
LEFT JOIN {{ source('fireprotdb', 'sequence') }} AS seq
    ON seq.id = ps.sequence_id
WHERE s.source_aa IS NOT NULL
  AND s.target_aa IS NOT NULL