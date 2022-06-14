## MDemo Example


### Install [Lightning](https://lightning.ai/lightning-docs/installation.html)

Follow the steps below to setup the project

```
git clone https://github.com/krishnakalyan3/mdemo
cd mdemo
conda create -n mars python=3.8
conda activate mars
pip3 install -r requirements.txt

# Deploy app in cloud
lightning run app app.py --cloud

# Deploy app locally
lightning run app app.py 
```

### GPU Setup
Right now this demo launches a `cpu`. 

```
L.CloudCompute("cpu-small")
```

This can be changed to use `gpu`.
```
L.CloudCompute("gpu")
```

For more information on machines supported please look at our [documentation](https://ideal-potato-417c066a.pages.github.io/core_api/lightning_work/compute.html?highlight=cpu%20small).
