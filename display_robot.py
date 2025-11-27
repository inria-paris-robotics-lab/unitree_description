import pinocchio as pin
from go2_description.loader import loadG1
from pinocchio.visualize import MeshcatVisualizer

robot = loadG1()

# --- Create Meshcat visualizer ---
viz = MeshcatVisualizer(robot.model, robot.collision_model, robot.visual_model)

# Start a new Meshcat server and connect
viz.initViewer(open=True)

# Load models into the viewer
viz.loadViewerModel()

viz.display_collisions = True
viz.displayCollisions(True)

# --- Display the robot at neutral configuration ---
q0 = pin.neutral(robot.model)
viz.display(q0)

print("Meshcat viewer is ready. Visit the displayed URL to see the robot.")
input('...')