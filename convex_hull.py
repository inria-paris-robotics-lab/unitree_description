import os
import argparse
import xml.etree.ElementTree as ET
import trimesh

def get_mesh_filenames_from_urdf(urdf_path):
    """
    Parse the URDF and return a set of mesh filenames (not full paths)
    used in <visual> elements.
    """
    tree = ET.parse(urdf_path)
    root = tree.getroot()
    mesh_filenames = set()

    for link in root.findall('link'):
        for visual in link.findall('visual'):
            geometry = visual.find('geometry')
            if geometry is not None:
                mesh = geometry.find('mesh')
                if mesh is not None and 'filename' in mesh.attrib:
                    filename = mesh.attrib['filename']
                    filename = filename.replace('package://', '').replace('\\', '/')
                    filename = os.path.basename(filename.strip())
                    mesh_filenames.add(filename)
    return mesh_filenames


def compute_and_save_convex_hull(mesh_path, output_dir=None):
    """
    Load a mesh, compute its convex hull, and save it with _collision suffix.
    """
    try:
        mesh = trimesh.load(mesh_path, force='mesh')
        if not isinstance(mesh, trimesh.Trimesh):
            print(f"⚠️ Skipped (not a valid mesh): {mesh_path}")
            return

        hull = mesh.convex_hull

        dirname, fname = os.path.split(mesh_path)
        name, ext = os.path.splitext(fname)
        output_dir = output_dir or dirname
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"{name}_collision{ext}")
        hull.export(output_path)
        print(f"✅ Convex hull saved: {output_path}")
    except Exception as e:
        print(f"❌ Failed to process {mesh_path}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Compute convex hulls of meshes used by a URDF, using mesh filenames from a given directory."
    )
    parser.add_argument("--urdf", required=True, help="Path to the URDF file.")
    parser.add_argument("--input_dir", required=True, help="Directory where meshes are stored.")
    parser.add_argument("--output_dir", default=None, help="Output directory (optional). Defaults to same as mesh directory.")
    parser.add_argument("--ext", default=None, help="Optional override for mesh file extension (e.g., .stl).")

    args = parser.parse_args()

    mesh_filenames = get_mesh_filenames_from_urdf(args.urdf)

    if not mesh_filenames:
        print("No meshes found in URDF.")
        return

    print(f"Found {len(mesh_filenames)} mesh file(s) in URDF:")
    for f in mesh_filenames:
        print(f"  {f}")

    print("\nProcessing meshes...")
    for filename in mesh_filenames:
        mesh_path = os.path.join(args.input_dir, filename)
        if not os.path.exists(mesh_path):
            # try with overridden extension if provided
            if args.ext:
                base, _ = os.path.splitext(mesh_path)
                mesh_path = base + args.ext
            if not os.path.exists(mesh_path):
                print(f"❌ Mesh file not found: {filename}")
                continue
        compute_and_save_convex_hull(mesh_path, args.output_dir)


if __name__ == "__main__":
    main()