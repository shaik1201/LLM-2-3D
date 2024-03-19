import rhinoinside
rhinoinside.load()

# System and Rhino can only be loaded after rhinoinside is initialized
# import System  # noqa
import Rhino
import Rhino.Geometry as rg  # noqa
import traceback

prompt = "" #get from ui
file_name = run_all_agents(prompt)
generated_code = get_file_content("Files_Generated_By_Agents\Full_Programs_Generated",f"{file_name}.py")
prefix_code = get_file_content("Utils","prefix_full_program_grasshopper.py") #change to relevant prefix to implement the function create_params(input_list)
code = f"{prefix_code}\n\n{generated_code}"
ex_locals = {}

old_stdout = sys.stdout
redirected_output = sys.stdout = StringIO()
exec(code, None, ex_locals)
sys.stdout = old_stdout

print(redirected_output.getvalue())

geometry = ex_locals['a'] # array of breps
#how to present the brep in we ui: 
#maybe: https://developer.rhino3d.com/api/rhinocommon/rhino.runtime.commonobject/tojson