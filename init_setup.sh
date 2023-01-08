echo [$(date)]: "START"
echo [$(date)]: "CREATING ENV"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating the environment"
conda activate ./env
echo [$(date)]: "installing requirements"
pip install -r requirements.txt
mkdir logs
echo [$(date)]: "first commit"
echo [$(date)]: "END"