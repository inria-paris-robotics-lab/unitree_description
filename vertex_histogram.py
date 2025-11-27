import os
import argparse
import trimesh
import matplotlib.pyplot as plt

def get_mesh_vertex_counts(directory, ext=None):
    """
    Load all mesh files in the given directory (recursively)
    and return a list of (filename, vertex_count) tuples.
    """
    mesh_info = []
    supported = ('.stl', '.obj', '.ply', '.dae', '.glb', '.gltf')

    for root, _, files in os.walk(directory):
        for f in files:
            if ext:
                if not f.lower().endswith(ext.lower()):
                    continue
            else:
                if not f.lower().endswith(supported):
                    continue

            path = os.path.join(root, f)
            try:
                mesh = trimesh.load(path, force='mesh')
                if not isinstance(mesh, trimesh.Trimesh):
                    print(f"⚠️ Skipped non-mesh: {f}")
                    continue
                vertex_count = len(mesh.vertices)
                mesh_info.append((f, vertex_count))
            except Exception as e:
                print(f"❌ Failed to load {f}: {e}")

    return mesh_info


def main():
    parser = argparse.ArgumentParser(
        description="Print mesh files sorted by number of vertices and plot a histogram."
    )
    parser.add_argument("--path", required=True, help="Path to directory containing meshes.")
    parser.add_argument("--ext", default=None, help="Optional mesh extension filter, e.g., .stl, .obj")
    parser.add_argument("--bins", type=int, default=20, help="Number of bins in the histogram.")
    args = parser.parse_args()

    mesh_info = get_mesh_vertex_counts(args.path, args.ext)
    if not mesh_info:
        print("No valid meshes found.")
        return

    # Sort descending by vertex count
    mesh_info.sort(key=lambda x: x[1], reverse=True)

    # Print the table
    print("\nMeshes sorted by vertex count:\n")
    print(f"{'Vertices':>10} | Filename")
    print("-" * 50)
    for fname, vcount in mesh_info:
        print(f"{vcount:>10} | {fname}")

    # Plot histogram
    counts = [vcount for _, vcount in mesh_info]
    plt.figure(figsize=(8, 5))
    plt.hist(counts, bins=args.bins, color='skyblue', edgecolor='black')
    plt.title("Histogram of Mesh Vertex Counts")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Number of Meshes")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()