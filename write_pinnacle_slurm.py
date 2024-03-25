# Variables
job_name = "write_pinnacle_slurm"
partition = "comp72"
nodes = 1
time = "72:00:00"

# Printing the SLURM script with variables
print("#!/bin/bash")
print()
print(f"#SBATCH --job-name={job_name}")
print(f"#SBATCH --partition={partition}")
print(f"#SBATCH --nodes={nodes}")
print("#SBATCH --qos=comp")
print("#SBATCH --tasks-per-node=32")
print(f"#SBATCH --time={time}")
print("#SBATCH -o example_%j.out")
print("#SBATCH -e example_%j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=email@uark.edu")
print()
print("module purge")
print("module load intel/18.0.1 impi/18.0.1 mkl/18.0.1")
print()
print("cd $SLURM_SUBMIT_DIR")
print("# job command here")
