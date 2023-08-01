# Data-Free Knowledge Distillation for Heterogeneous Federated Learning

Credits
We would like to give credit to the following repositories for their code and resources that we used in our project:
 [Data-Free Knowledge Distillation for Heterogeneous Federated](https://arxiv.org/pdf/2105.10056.pdf).

We used their repository and added our algorithm : FedGenP
 
## Install Requirements:
```pip3 install -r requirements.txt```

  
## Prepare Dataset: 
* To generate *non-iid* **Mnist** Dataset following the Dirichlet distribution D(&alpha;=0.1) for 20 clients, using 50% of the total available training samples:
<pre><code>cd FedGen/data/Mnist
python generate_niid_dirichlet.py --n_class 10 --sampling_ratio 0.5 --alpha 0.1 --n_user 20
### This will generate a dataset located at FedGen/data/Mnist/u20c10-alpha0.1-ratio0.5/
</code></pre>
    

- Similarly, to generate *non-iid* **EMnist** Dataset, using 10% of the total available training samples:
<pre><code>cd FedGen/data/EMnist
python generate_niid_dirichlet.py --sampling_ratio 0.1 --alpha 0.1 --n_user 20 
### This will generate a dataset located at FedGen/data/EMnist/u20-letters-alpha0.1-ratio0.1/
</code></pre> 

## Run Experiments: 

There is a "Run_multiple_setting.py" where you can specify the setting; It will run main.py.

#### To run experiments: 
python Run_multiple_setting.py

### Plot
For the input attribute **algorithms**, list the name of algorithms and separate them by comma, e.g. `--algorithms FedAvg,FedGen,FedProx`
```
python main_plot.py --dataset EMnist-alpha0.1-ratio0.1 --algorithms FedAvg,FedGen --batch_size 32 --local_epochs 20 --num_users 10 --num_glob_iters 200 --plot_legend 1
```
