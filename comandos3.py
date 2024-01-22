import subprocess
import time

def run_command(command):
    subprocess.call(command, shell=True)


# Iniciar cluster 
run_command("minikube start --driver=docker -p pc2 --nodes 5")

# Cambiamos al perfil pc2
run_command("minikube profile pc2")

# Desplegamos la aplicación
run_command("minikube kubectl apply -- -f .")

# Esperamos a que los nods se inicien
while (str(subprocess.check_output(["minikube kubectl get pods"], shell=True)).count("Running") < 9):
    time.sleep(1)

# Abrimos la web 
run_command("minikube service product-page")
