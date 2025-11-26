import os
import xml.etree.ElementTree as ET
import argparse

def get_mesh_files_from_urdf(urdf_path):
    """
    Parse a URDF file and extract all mesh filenames used for visuals.
    """
    tree = ET.parse(urdf_path)
    root = tree.getroot()

    mesh_files = set()
    for visual in root.findall('.//visual'):
        geometry = visual.find('geometry')
        if geometry is not None:
            mesh = geometry.find('mesh')
            if mesh is not None and 'filename' in mesh.attrib:
                filename = mesh.attrib['filename']

                # Clean up and keep only the filename
                filename = filename.replace('package://', '').replace('\\', '/')
                filename = os.path.basename(filename.strip())
                mesh_files.add(filename)
    return mesh_files


def list_all_files_in_directory(directory):
    """
    Return a set of filenames (not full paths) in the directory and subdirectories.
    """
    all_files = set()
    for root, _, files in os.walk(directory):
        for f in files:
            all_files.add(f)  # only the filename
    return all_files


def main():
    parser = argparse.ArgumentParser(description="Compare URDF visual meshes with asset directory contents (by filename).")
    parser.add_argument("--urdf", required=True, help="Path to the URDF file.")
    parser.add_argument("--assets", required=True, help="Path to the asset directory containing mesh files.")
    args = parser.parse_args()

    urdf_mesh_filenames = get_mesh_files_from_urdf(args.urdf)
    asset_filenames = list_all_files_in_directory(args.assets)

    unused_assets = asset_filenames - urdf_mesh_filenames

    print("Mesh filenames used by URDF:")
    for m in sorted(urdf_mesh_filenames):
        print(f"  {m}")

    print("\nAll filenames in asset directory:")
    for f in sorted(asset_filenames):
        print(f"  {f}")

    print("\nFiles in asset directory NOT used by URDF visuals:")
    for f in sorted(unused_assets):
        print(f"  {f}")


if __name__ == "__main__":
    main()