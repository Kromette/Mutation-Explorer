import py3Dmol
from stmol import showmol

def render_mutation(pdb_path, mutation_resi):

    with open(pdb_path, "r") as f:
        pdb_data = f.read()

    view = py3Dmol.view(width=800, height=600)
    view.addModel(pdb_data, "pdb")

    # 🔹 Protéine entière en lightgray
    view.setStyle({}, {
        "cartoon": {"color": "lightgray"}
    })

    # 🔴 ou 🟢 Mutation en highlight
    view.addStyle(
        {"resi": mutation_resi},
        {
            "stick": {"colorscheme": "greenCarbon"}  # ou "greenCarbon"
        }
    )

    # zoom sur la mutation
    ##view.zoomTo({"resi": mutation_resi})

    return view