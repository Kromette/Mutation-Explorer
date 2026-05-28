
import py3Dmol


def render_protein(pdb_path):

    with open(pdb_path, "r") as f:
        pdb_data = f.read()

    view = py3Dmol.view(
        width=800,
        height=600
    )

    view.addModel(pdb_data, "pdb")

    view.setStyle({
        "cartoon": {
            "color": "spectrum"
        }
    })

    view.zoomTo()

    return view