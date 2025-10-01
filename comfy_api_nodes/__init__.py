import os


def custom_nodes_list() -> list[tuple[str, str]]:
    """Returns list of tuples with [AbsolutePathToTheNodeFile, ModuleParent]"""

    api_nodes_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy_api_nodes")
    api_nodes_files = [
        "canary.py",  # not a node - but required for now (keep number of changes minimum for demo)
        "nodes_ideogram.py",
        "nodes_openai.py",
        "nodes_minimax.py",
        "nodes_veo2.py",
        "nodes_kling.py",
        "nodes_bfl.py",
        "nodes_bytedance.py",
        "nodes_luma.py",
        "nodes_recraft.py",
        "nodes_pixverse.py",
        "nodes_stability.py",
        "nodes_pika.py",
        "nodes_runway.py",
        "nodes_tripo.py",
        "nodes_moonvalley.py",
        "nodes_rodin.py",
        "nodes_gemini.py",
        "nodes_vidu.py",
        "nodes_wan.py",
    ]
    return [(os.path.join(api_nodes_dir, r), "comfy_api_nodes") for r in api_nodes_files]
